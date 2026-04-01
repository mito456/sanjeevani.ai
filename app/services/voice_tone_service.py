import importlib
from dataclasses import dataclass


@dataclass
class VocalToneResult:
    label: str
    confidence: float
    model_used: str
    features: dict[str, float]


def _score_to_label(score: float) -> tuple[str, float]:
    if score >= 0.33:
        return "Happy", min(0.95, 0.55 + score)
    if score <= -0.25:
        return "Low", min(0.95, 0.55 + abs(score))
    return "Neutral", 0.62


def analyze_vocal_tone(audio_bytes: bytes) -> VocalToneResult:
    """
    Lightweight heuristic vocal tone recognizer.
    Uses acoustic signals only (pitch, energy, speaking rate proxy) for
    explainable hackathon behavior.
    """
    try:
        import io

        librosa = importlib.import_module("librosa")
        np = importlib.import_module("numpy")
        sf = importlib.import_module("soundfile")

        audio_buffer = io.BytesIO(audio_bytes)
        waveform, sample_rate = sf.read(audio_buffer, dtype="float32")

        if waveform.ndim > 1:
            waveform = np.mean(waveform, axis=1)

        # Keep analysis stable across noisy recordings.
        waveform = librosa.util.normalize(waveform)

        if len(waveform) < sample_rate:
            return VocalToneResult(
                label="Neutral",
                confidence=0.5,
                model_used="heuristic-tone",
                features={
                    "duration_sec": round(len(waveform) / sample_rate, 3),
                    "avg_pitch_hz": 0.0,
                    "rms_energy": 0.0,
                    "speech_rate_proxy": 0.0,
                },
            )

        f0, _, _ = librosa.pyin(
            waveform,
            fmin=librosa.note_to_hz("C2"),
            fmax=librosa.note_to_hz("C7"),
            sr=sample_rate,
        )
        pitch_values = f0[~np.isnan(f0)]
        avg_pitch = float(np.mean(pitch_values)) if len(pitch_values) else 0.0

        rms = librosa.feature.rms(y=waveform)
        rms_energy = float(np.mean(rms))

        onset_env = librosa.onset.onset_strength(y=waveform, sr=sample_rate)
        tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sample_rate)
        speech_rate_proxy = float(tempo)

        # Heuristic score: positive if voice is energetic and dynamic.
        pitch_component = (avg_pitch - 170.0) / 120.0
        energy_component = (rms_energy - 0.035) * 12.0
        tempo_component = (speech_rate_proxy - 95.0) / 110.0
        score = 0.45 * pitch_component + 0.4 * energy_component + 0.15 * tempo_component

        label, confidence = _score_to_label(score)
        return VocalToneResult(
            label=label,
            confidence=round(float(confidence), 3),
            model_used="heuristic-tone",
            features={
                "duration_sec": round(len(waveform) / sample_rate, 3),
                "avg_pitch_hz": round(avg_pitch, 3),
                "rms_energy": round(rms_energy, 5),
                "speech_rate_proxy": round(speech_rate_proxy, 3),
            },
        )
    except Exception:
        return VocalToneResult(
            label="Neutral",
            confidence=0.45,
            model_used="heuristic-tone-fallback",
            features={
                "duration_sec": 0.0,
                "avg_pitch_hz": 0.0,
                "rms_energy": 0.0,
                "speech_rate_proxy": 0.0,
            },
        )
