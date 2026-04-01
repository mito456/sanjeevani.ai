# Chaitanya AI Backend (FastAPI)

Backend prototype for the Chaitanya AI elderly-care assistant.

## Features

- Activity logging and routine baseline detection
- Reminder creation with escalation-compatible missed-count tracking
- Mood status API using HuggingFace sentiment model (with fallback)
- Fall risk estimation using explainable heuristic scoring
- Alert trigger endpoint (mock channel, Twilio-ready extension point)
- SQLite persistence for hackathon simplicity

## API Endpoints

- `POST /log-activity`
- `GET /get-routine-pattern`
- `GET /check-deviation`
- `POST /set-reminder`
- `POST /trigger-alert`
- `POST /get-mood-status`
- `POST /get-vocal-tone`
- `POST /get-combined-mood-status`
- `GET /get-fall-risk`

## Quick Start

1. Create and activate a Python virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the API server:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Open docs:

   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Example Requests

### Log activity

```bash
curl -X POST http://127.0.0.1:8000/log-activity \
  -H "Content-Type: application/json" \
  -d '{"source": "voice-checkin", "notes": "Morning response"}'
```

### Set reminder

```bash
curl -X POST http://127.0.0.1:8000/set-reminder \
  -H "Content-Type: application/json" \
  -d '{"title":"Take blood pressure medicine","remind_at":"2026-04-01T09:00:00Z","repeat_daily":true}'
```

### Mood status

```bash
curl -X POST http://127.0.0.1:8000/get-mood-status \
  -H "Content-Type: application/json" \
  -d '{"text": "I feel tired and lonely today"}'
```

### Vocal tone recognition

```bash
curl -X POST http://127.0.0.1:8000/get-vocal-tone \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "audio=@sample.wav"
```

### Combined mood (text + voice)

```bash
curl -X POST http://127.0.0.1:8000/get-combined-mood-status \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "text=I am feeling okay but slightly tired" \
  -F "audio=@sample.wav"
```

## Notes

- Whisper and transformer models may download on first run.
- The sentiment pipeline fails gracefully to rule-based mode if model dependencies are unavailable.
- `simulate-missed-reminder` is a helper endpoint for demo/testing escalation logic.
