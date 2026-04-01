from datetime import datetime, timezone


def trigger_alert(reason: str, emergency: bool, caregiver_contact: str | None) -> dict:
    """
    Placeholder alert service.
    Replace with Twilio SMS or call automation for production.
    """
    channel = "sms" if caregiver_contact else "app-notification"
    severity = "high" if emergency else "normal"
    timestamp = datetime.now(timezone.utc).isoformat()

    message = (
        f"[ALERT::{severity}] {reason}. "
        f"Contact: {caregiver_contact or 'not configured'}"
    )

    return {
        "triggered": True,
        "timestamp": timestamp,
        "channel": channel,
        "severity": severity,
        "message": message,
    }
