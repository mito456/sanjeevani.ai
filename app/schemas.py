from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class ActivityLogRequest(BaseModel):
    source: str = Field(default="mobile", min_length=2, max_length=50)
    notes: str | None = Field(default=None, max_length=250)
    timestamp: datetime | None = None


class ReminderRequest(BaseModel):
    title: str = Field(min_length=2, max_length=120)
    remind_at: datetime
    repeat_daily: bool = False


class TriggerAlertRequest(BaseModel):
    reason: str = Field(min_length=3, max_length=180)
    emergency: bool = False


class MoodStatusRequest(BaseModel):
    text: str = Field(min_length=1, max_length=1200)


class MoodStatusResponse(BaseModel):
    label: Literal["Happy", "Neutral", "Low"]
    score: float
    model_used: str


class VocalToneResponse(BaseModel):
    label: Literal["Happy", "Neutral", "Low"]
    confidence: float
    model_used: str
    features: dict[str, float]


class MoodComponent(BaseModel):
    label: Literal["Happy", "Neutral", "Low"]
    confidence: float
    source: str


class CombinedMoodResponse(BaseModel):
    final_label: Literal["Happy", "Neutral", "Low"]
    final_confidence: float
    fusion_strategy: str
    text_component: MoodComponent | None
    vocal_component: MoodComponent | None
    vocal_features: dict[str, float] | None


class FallRiskResponse(BaseModel):
    score: float
    level: Literal["Low", "Medium", "High"]
    factors: dict[str, float]


class ReminderResponse(BaseModel):
    reminder_id: int
    title: str
    remind_at: datetime
    repeat_daily: bool
