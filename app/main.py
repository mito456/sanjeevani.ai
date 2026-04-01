from datetime import datetime, timezone

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from app.database import execute, fetch_one, init_db
from app.schemas import (
    ActivityLogRequest,
    CombinedMoodResponse,
    FallRiskResponse,
    MoodComponent,
    MoodStatusRequest,
    MoodStatusResponse,
    ReminderRequest,
    ReminderResponse,
    TriggerAlertRequest,
    VocalToneResponse,
)
from app.services.alert_service import trigger_alert
from app.services.mood_service import analyze_mood_text
from app.services.risk_service import check_deviation, compute_fall_risk, compute_routine_pattern
from app.services.voice_tone_service import analyze_vocal_tone


def _label_value(label: str) -> int:
    mapping = {"Low": -1, "Neutral": 0, "Happy": 1}
    return mapping.get(label, 0)


def _value_label(value: float) -> str:
    if value >= 0.33:
        return "Happy"
    if value <= -0.33:
        return "Low"
    return "Neutral"

app = FastAPI(
    title="Sanjeevani AI Backend",
    description="Mobile-first healthcare assistant backend for hackathon demo",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "chaitanya-ai-backend"}


@app.post("/log-activity")
def log_activity(payload: ActivityLogRequest) -> dict:
    ts = payload.timestamp or datetime.now(timezone.utc)
    activity_id = execute(
        "INSERT INTO activity_logs (timestamp, source, notes) VALUES (?, ?, ?)",
        (ts.isoformat(), payload.source, payload.notes),
    )

    return {
        "activity_id": activity_id,
        "timestamp": ts.isoformat(),
        "source": payload.source,
    }


@app.get("/get-routine-pattern")
def get_routine_pattern() -> dict:
    return compute_routine_pattern()


@app.get("/check-deviation")
def get_deviation_status() -> dict:
    return check_deviation()


@app.post("/set-reminder", response_model=ReminderResponse)
def set_reminder(payload: ReminderRequest) -> ReminderResponse:
    reminder_id = execute(
        """
        INSERT INTO reminders (title, remind_at, repeat_daily, is_active, missed_count, last_triggered)
        VALUES (?, ?, ?, 1, 0, NULL)
        """,
        (payload.title, payload.remind_at.isoformat(), int(payload.repeat_daily)),
    )

    return ReminderResponse(
        reminder_id=reminder_id,
        title=payload.title,
        remind_at=payload.remind_at,
        repeat_daily=payload.repeat_daily,
    )


@app.post("/trigger-alert")
def api_trigger_alert(payload: TriggerAlertRequest) -> dict:
    row = fetch_one("SELECT caregiver_contact FROM user_settings WHERE id = 1")
    caregiver_contact = None if row is None else row["caregiver_contact"]
    return trigger_alert(payload.reason, payload.emergency, caregiver_contact)


@app.post("/get-mood-status", response_model=MoodStatusResponse)
def get_mood_status(payload: MoodStatusRequest) -> MoodStatusResponse:
    result = analyze_mood_text(payload.text)
    now_utc = datetime.now(timezone.utc)

    execute(
        "INSERT INTO mood_logs (timestamp, text, sentiment_label, score) VALUES (?, ?, ?, ?)",
        (now_utc.isoformat(), payload.text, result.label, result.score),
    )

    return MoodStatusResponse(
        label=result.label,
        score=result.score,
        model_used=result.model_used,
    )


@app.post("/get-vocal-tone", response_model=VocalToneResponse)
async def get_vocal_tone(audio: UploadFile = File(...)) -> VocalToneResponse:
    if not audio.content_type or not audio.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Please upload a valid audio file")

    payload = await audio.read()
    if not payload:
        raise HTTPException(status_code=400, detail="Empty audio file")

    tone = analyze_vocal_tone(payload)
    return VocalToneResponse(
        label=tone.label,
        confidence=tone.confidence,
        model_used=tone.model_used,
        features=tone.features,
    )


@app.post("/get-combined-mood-status", response_model=CombinedMoodResponse)
async def get_combined_mood_status(
    text: str | None = Form(default=None),
    audio: UploadFile | None = File(default=None),
) -> CombinedMoodResponse:
    if not text and audio is None:
        raise HTTPException(status_code=400, detail="Provide text, audio, or both")

    text_component: MoodComponent | None = None
    vocal_component: MoodComponent | None = None
    vocal_features: dict[str, float] | None = None

    weighted_sum = 0.0
    total_weight = 0.0

    if text:
        text_result = analyze_mood_text(text)
        text_conf = max(0.05, min(float(text_result.score), 1.0))
        text_weight = 0.6
        weighted_sum += _label_value(text_result.label) * text_conf * text_weight
        total_weight += text_conf * text_weight
        text_component = MoodComponent(
            label=text_result.label,
            confidence=round(text_conf, 3),
            source=text_result.model_used,
        )

    if audio is not None:
        if not audio.content_type or not audio.content_type.startswith("audio/"):
            raise HTTPException(status_code=400, detail="Audio file must be a valid audio MIME type")
        payload = await audio.read()
        if not payload:
            raise HTTPException(status_code=400, detail="Empty audio file")

        tone_result = analyze_vocal_tone(payload)
        tone_conf = max(0.05, min(float(tone_result.confidence), 1.0))
        tone_weight = 0.4
        weighted_sum += _label_value(tone_result.label) * tone_conf * tone_weight
        total_weight += tone_conf * tone_weight
        vocal_component = MoodComponent(
            label=tone_result.label,
            confidence=round(tone_conf, 3),
            source=tone_result.model_used,
        )
        vocal_features = tone_result.features

    if total_weight == 0:
        final_scalar = 0.0
    else:
        final_scalar = weighted_sum / total_weight

    final_label = _value_label(final_scalar)
    final_confidence = round(min(1.0, abs(final_scalar) + 0.45), 3)

    execute(
        "INSERT INTO mood_logs (timestamp, text, sentiment_label, score) VALUES (?, ?, ?, ?)",
        (
            datetime.now(timezone.utc).isoformat(),
            text,
            final_label,
            final_confidence,
        ),
    )

    return CombinedMoodResponse(
        final_label=final_label,
        final_confidence=final_confidence,
        fusion_strategy="weighted-label-fusion(text=0.6,vocal=0.4)",
        text_component=text_component,
        vocal_component=vocal_component,
        vocal_features=vocal_features,
    )


@app.get("/get-fall-risk", response_model=FallRiskResponse)
def get_fall_risk() -> FallRiskResponse:
    risk = compute_fall_risk()
    return FallRiskResponse(
        score=risk["score"],
        level=risk["level"],
        factors=risk["factors"],
    )


@app.post("/simulate-missed-reminder/{reminder_id}")
def simulate_missed_reminder(reminder_id: int) -> dict:
    reminder = fetch_one("SELECT id, missed_count FROM reminders WHERE id = ?", (reminder_id,))
    if reminder is None:
        raise HTTPException(status_code=404, detail="Reminder not found")

    execute(
        "UPDATE reminders SET missed_count = missed_count + 1 WHERE id = ?",
        (reminder_id,),
    )

    updated = fetch_one("SELECT missed_count FROM reminders WHERE id = ?", (reminder_id,))
    return {
        "reminder_id": reminder_id,
        "missed_count": 0 if updated is None else updated["missed_count"],
    }
