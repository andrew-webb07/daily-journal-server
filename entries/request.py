import sqlite3
import json
from models import Entry, Mood

def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.journal_entry,
            e.mood_id,
            m.label
        FROM entry e
        JOIN Mood m
        ON m.id = e.mood_id
        """)

        entries = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            entry = Entry(row['id'], row['date'], row['concept'], row['journal_entry'], row['mood_id'])

            mood = Mood(row['mood_id'], row['label'])
            entry.mood = mood.__dict__

            entries.append(entry.__dict__)
    return json.dumps(entries)


def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.journal_entry,
            e.mood_id,
            m.label
        FROM entry e
        JOIN Mood m
        ON m.id = e.mood_id
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()
        entry = Entry(data['id'], data['date'], data['concept'], data['journal_entry'], data['mood_id'])
        mood = Mood(data['id'], data['label'])
        entry.mood = mood.__dict__
        
    return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entry
        WHERE id = ?
        """, (id, ))

def search_entries(search_terms):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(f"""
        SELECT
            e.id,
            e.date,
            e.concept,
            e.journal_entry,
            e.mood_id
        FROM entry e
        WHERE concept LIKE "%{search_terms}%" OR journal_entry LIKE "%{search_terms}%" OR date LIKE "%{search_terms}%"
        """)

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['date'], row['concept'], row['journal_entry'], row['mood_id'])
            entries.append(entry.__dict__)

    return json.dumps(entries)