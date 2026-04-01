import sqlite3
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "chaitanya_ai.db"


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS activity_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            source TEXT NOT NULL,
            notes TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            remind_at TEXT NOT NULL,
            repeat_daily INTEGER NOT NULL DEFAULT 0,
            is_active INTEGER NOT NULL DEFAULT 1,
            missed_count INTEGER NOT NULL DEFAULT 0,
            last_triggered TEXT
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS mood_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            text TEXT,
            sentiment_label TEXT NOT NULL,
            score REAL NOT NULL
        )
        """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS user_settings (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            age INTEGER NOT NULL DEFAULT 68,
            inactivity_threshold_minutes INTEGER NOT NULL DEFAULT 180,
            caregiver_contact TEXT,
            emergency_contact_name TEXT,
            emergency_contact_phone TEXT
        )
        """
    )

    cur.execute(
        """
        INSERT OR IGNORE INTO user_settings (
            id,
            age,
            inactivity_threshold_minutes,
            caregiver_contact,
            emergency_contact_name,
            emergency_contact_phone
        )
        VALUES (1, 68, 180, NULL, NULL, NULL)
        """
    )

    conn.commit()
    conn.close()


def fetch_one(query: str, params: tuple[Any, ...] = ()) -> sqlite3.Row | None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    row = cur.fetchone()
    conn.close()
    return row


def fetch_all(query: str, params: tuple[Any, ...] = ()) -> list[sqlite3.Row]:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return rows


def execute(query: str, params: tuple[Any, ...] = ()) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    last_id = cur.lastrowid
    conn.close()
    return last_id
