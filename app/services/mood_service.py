import importlib
from dataclasses import dataclass


@dataclass
class MoodResult:
    label: str
    score: float
    model_used: str


def _fallback_sentiment(text: str) -> MoodResult:
    content = text.lower()

    positive_words = {
        "happy",
        "good",
        "great",
        "fine",
        "better",
        "thankful",
        "excited",
        "joy",
    }
    negative_words = {
        "sad",
        "bad",
        "tired",
        "lonely",
        "upset",
        "anxious",
        "depressed",
        "pain",
    }

    positive_hits = sum(1 for token in positive_words if token in content)
    negative_hits = sum(1 for token in negative_words if token in content)

    if negative_hits > positive_hits:
        return MoodResult(label="Low", score=0.25, model_used="fallback-rules")
    if positive_hits > negative_hits:
        return MoodResult(label="Happy", score=0.85, model_used="fallback-rules")
    return MoodResult(label="Neutral", score=0.55, model_used="fallback-rules")


def analyze_mood_text(text: str) -> MoodResult:
    """
    Uses HuggingFace sentiment model when available and falls back to a
    deterministic rule-based classifier for offline demo reliability.
    """
    try:
        transformers = importlib.import_module("transformers")
        pipeline = getattr(transformers, "pipeline")

        sentiment_pipe = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
        )
        result = sentiment_pipe(text[:512])[0]
        label = result.get("label", "NEUTRAL").upper()
        score = float(result.get("score", 0.5))

        if label == "POSITIVE":
            mood = "Happy"
        elif score < 0.6:
            mood = "Neutral"
        else:
            mood = "Low"

        return MoodResult(label=mood, score=round(score, 3), model_used="hf-sst2")
    except Exception:
        return _fallback_sentiment(text)
