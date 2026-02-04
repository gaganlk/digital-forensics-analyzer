import sqlite3
from datetime import datetime

DB_PATH = "database/forensic.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS cases (
        case_id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_name TEXT,
        investigator TEXT,
        created_at TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_id INTEGER,
        file_name TEXT,
        file_path TEXT,
        size INTEGER,
        created TEXT,
        modified TEXT,
        accessed TEXT,
        hash TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS anomalies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_id INTEGER,
        type TEXT,
        file TEXT,
        severity TEXT,
        reason TEXT
    )
    """)

    conn.commit()
    conn.close()


def create_case(name, investigator):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO cases VALUES(NULL, ?, ?, ?)",
        (name, investigator, datetime.now())
    )

    cid = cur.lastrowid
    conn.commit()
    conn.close()
    return cid


def store_files(case_id, files):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for f in files:
        cur.execute("""
        INSERT INTO files VALUES(NULL,?,?,?,?,?,?,?,?)
        """, (
            case_id,
            f["file_name"],
            f["file_path"],
            f["size"],
            str(f["created"]),
            str(f["modified"]),
            str(f["accessed"]),
            f["hash"]
        ))

    conn.commit()
    conn.close()


def store_anomalies(case_id, anomalies):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for a in anomalies:
        cur.execute("""
        INSERT INTO anomalies VALUES(NULL,?,?,?,?,?)
        """, (
            case_id,
            a["type"],
            a["file"],
            a["severity"],
            a["reason"]
        ))

    conn.commit()
    conn.close()
