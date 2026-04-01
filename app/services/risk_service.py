from datetime import datetime, timedelta, timezone

from app.database import fetch_all, fetch_one


def _to_utc(dt_str: str) -> datetime:
    return datetime.fromisoformat(dt_str.replace("Z", "+00:00")).astimezone(timezone.utc)


def get_last_activity_iso() -> str | None:
    row = fetch_one(
        "SELECT timestamp FROM activity_logs ORDER BY timestamp DESC LIMIT 1"
    )
    return None if row is None else row["timestamp"]


def compute_routine_pattern() -> dict:
    rows = fetch_all("SELECT timestamp FROM activity_logs ORDER BY timestamp ASC")
    if not rows:
        return {
            "message": "No activity data yet",
            "average_checkin_hour": None,
            "average_gap_minutes": None,
            "sample_size": 0,
        }

    times = [_to_utc(row["timestamp"]) for row in rows]
    avg_hour = round(sum(t.hour + (t.minute / 60.0) for t in times) / len(times), 2)

    gaps = []
    for idx in range(1, len(times)):
        gap = (times[idx] - times[idx - 1]).total_seconds() / 60.0
        if gap >= 0:
            gaps.append(gap)

    avg_gap = round(sum(gaps) / len(gaps), 2) if gaps else None

    return {
        "average_checkin_hour": avg_hour,
        "average_gap_minutes": avg_gap,
        "sample_size": len(times),
    }


def check_deviation() -> dict:
    settings = fetch_one(
        "SELECT inactivity_threshold_minutes FROM user_settings WHERE id = 1"
    )
    threshold = 180 if settings is None else int(settings["inactivity_threshold_minutes"])

    last_activity = get_last_activity_iso()
    if last_activity is None:
        return {
            "deviation": True,
            "reason": "No activity recorded yet",
            "minutes_since_last_activity": None,
            "threshold_minutes": threshold,
            "should_trigger_alert": False,
        }

    last_dt = _to_utc(last_activity)
    now_utc = datetime.now(timezone.utc)
    minutes_inactive = int((now_utc - last_dt).total_seconds() / 60)

    reminder_row = fetch_one(
        "SELECT COALESCE(SUM(missed_count), 0) AS total_missed FROM reminders WHERE is_active = 1"
    )
    total_missed = 0 if reminder_row is None else int(reminder_row["total_missed"])

    deviation = minutes_inactive > threshold
    should_trigger = deviation or total_missed >= 3

    reason = "Within normal pattern"
    if deviation:
        reason = "Inactivity threshold exceeded"
    if total_missed >= 3:
        reason = "Repeated missed reminders"

    return {
        "deviation": deviation,
        "reason": reason,
        "minutes_since_last_activity": minutes_inactive,
        "threshold_minutes": threshold,
        "total_missed_reminders": total_missed,
        "should_trigger_alert": should_trigger,
    }


def compute_fall_risk() -> dict:
    settings = fetch_one("SELECT age FROM user_settings WHERE id = 1")
    age = 68 if settings is None else int(settings["age"])

    now_utc = datetime.now(timezone.utc)
    window_start = (now_utc - timedelta(hours=24)).isoformat()

    activity_row = fetch_one(
        "SELECT COUNT(*) AS cnt FROM activity_logs WHERE timestamp >= ?",
        (window_start,),
    )
    reminders_row = fetch_one(
        "SELECT COALESCE(SUM(missed_count), 0) AS total FROM reminders WHERE is_active = 1"
    )

    activity_count_24h = 0 if activity_row is None else int(activity_row["cnt"])
    missed_reminders = 0 if reminders_row is None else int(reminders_row["total"])

    deviation = check_deviation()

    activity_factor = 0.0 if activity_count_24h >= 8 else min((8 - activity_count_24h) * 5.0, 40.0)
    irregular_factor = 25.0 if deviation.get("deviation") else 5.0
    age_factor = 10.0 if age < 70 else 18.0 if age < 80 else 28.0
    reminder_factor = min(missed_reminders * 4.0, 20.0)

    risk_score = round(min(activity_factor + irregular_factor + age_factor + reminder_factor, 100.0), 2)

    if risk_score < 35:
        level = "Low"
    elif risk_score < 65:
        level = "Medium"
    else:
        level = "High"

    return {
        "score": risk_score,
        "level": level,
        "factors": {
            "activity_factor": activity_factor,
            "irregular_pattern_factor": irregular_factor,
            "age_factor": age_factor,
            "missed_reminder_factor": reminder_factor,
        },
    }
