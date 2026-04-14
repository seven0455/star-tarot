#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intel Station - Local Knowledge Base
Based on SQLite + FTS5
"""

import sqlite3
import sys
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "intel.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS intel (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            keywords TEXT,
            category TEXT DEFAULT 'general',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    c.execute('''
        CREATE VIRTUAL TABLE IF NOT EXISTS intel_fts USING fts5(
            content, keywords, category,
            content='intel',
            content_rowid='id'
        )
    ''')
    c.execute('''
        CREATE TRIGGER IF NOT EXISTS intel_ai AFTER INSERT ON intel BEGIN
            INSERT INTO intel_fts(rowid, content, keywords, category)
            VALUES (new.id, new.content, new.keywords, new.category);
        END
    ''')
    c.execute('''
        CREATE TRIGGER IF NOT EXISTS intel_ad AFTER DELETE ON intel BEGIN
            INSERT INTO intel_fts(intel_fts, rowid, content, keywords, category)
            VALUES ('delete', old.id, old.content, old.keywords, old.category);
        END
    ''')
    c.execute('''
        CREATE TRIGGER IF NOT EXISTS intel_au AFTER UPDATE ON intel BEGIN
            INSERT INTO intel_fts(intel_fts, rowid, content, keywords, category)
            VALUES ('delete', old.id, old.content, old.keywords, old.category);
            INSERT INTO intel_fts(rowid, content, keywords, category)
            VALUES (new.id, new.content, new.keywords, new.category);
        END
    ''')
    conn.commit()
    conn.close()

def add(content, keywords="", category="general"):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        'INSERT INTO intel (content, keywords, category) VALUES (?, ?, ?)',
        (content, keywords, category)
    )
    conn.commit()
    intel_id = c.lastrowid
    conn.close()
    return intel_id

def search(query, limit=10):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    try:
        c.execute('''
            SELECT i.id, i.content, i.keywords, i.category, i.created_at
            FROM intel_fts f
            JOIN intel i ON f.rowid = i.id
            WHERE intel_fts MATCH ?
            LIMIT ?
        ''', (query, limit))
        results = c.fetchall()
    except:
        c.execute('''
            SELECT id, content, keywords, category, created_at
            FROM intel
            WHERE content LIKE ? OR keywords LIKE ?
            LIMIT ?
        ''', ('%' + query + '%', '%' + query + '%', limit))
        results = c.fetchall()
    conn.close()
    return results

def get_by_id(intel_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM intel WHERE id = ?', (intel_id,))
    result = c.fetchone()
    conn.close()
    return result

def list_all(category=None, limit=50):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    if category:
        c.execute(
            'SELECT * FROM intel WHERE category = ? ORDER BY id DESC LIMIT ?',
            (category, limit)
        )
    else:
        c.execute('SELECT * FROM intel ORDER BY id DESC LIMIT ?', (limit,))
    results = c.fetchall()
    conn.close()
    return results

def stats():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM intel')
    total = c.fetchone()[0]
    c.execute('SELECT category, COUNT(*) FROM intel GROUP BY category')
    by_category = c.fetchall()
    c.execute('SELECT COUNT(*) FROM intel WHERE date(created_at) = date("now")')
    today = c.fetchone()[0]
    conn.close()
    return {"total": total, "by_category": by_category, "today": today}

def main():
    init_db()
    if len(sys.argv) < 2:
        print("Intel Station - Local Knowledge Base")
        print("Usage: station.py <command> [args]")
        print("Commands: add, search, get, list, stats")
        return
    
    cmd = sys.argv[1].lower()
    
    if cmd == "add":
        if len(sys.argv) < 3:
            print("Usage: station.py add <content> [keywords] [category]")
            return
        content = sys.argv[2]
        keywords = sys.argv[3] if len(sys.argv) > 3 else ""
        category = sys.argv[4] if len(sys.argv) > 4 else "general"
        intel_id = add(content, keywords, category)
        print(f"[OK] Added (ID: {intel_id})")
    
    elif cmd == "search":
        if len(sys.argv) < 3:
            print("Usage: station.py search <query>")
            return
        query = sys.argv[2]
        results = search(query)
        if results:
            print(f"Found {len(results)} results:\n")
            for r in results:
                print(f"[{r[0]}] {r[1][:80]}")
                print(f"    Keywords: {r[2]} | Category: {r[3]}\n")
        else:
            print("No results found")
    
    elif cmd == "get":
        if len(sys.argv) < 3:
            print("Usage: station.py get <id>")
            return
        intel_id = int(sys.argv[2])
        result = get_by_id(intel_id)
        if result:
            print(f"ID: {result[0]}")
            print(f"Content: {result[1]}")
            print(f"Keywords: {result[2]}")
            print(f"Category: {result[3]}")
            print(f"Created: {result[4]}")
        else:
            print("Not found")
    
    elif cmd == "list":
        category = sys.argv[2] if len(sys.argv) > 2 else None
        results = list_all(category)
        if results:
            print(f"Total {len(results)}:\n")
            for r in results:
                print(f"[{r[0]}] {r[1][:60]}")
                print(f"    Keywords: {r[2]} | Category: {r[3]}\n")
        else:
            print("Empty")
    
    elif cmd == "stats":
        s = stats()
        print("== Intel Station Stats ==")
        print(f"Total: {s['total']}")
        print(f"Today: {s['today']}")
        print("\nBy category:")
        for cat, count in s['by_category']:
            print(f"  {cat}: {count}")
    
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
