#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intel Station - Smart Backup
智能备份：对比哈希，无变化不备份
"""

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path

STATION_DIR = Path(__file__).parent
DB_PATH = STATION_DIR / "intel.db"
SNAPSHOT_FILE = STATION_DIR / "snapshot.json"
BACKUP_DIR = STATION_DIR / "backups"

def get_db_hash():
    """计算数据库文件的MD5哈希"""
    if not DB_PATH.exists():
        return None
    with open(DB_PATH, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def get_snapshot():
    """加载上次快照"""
    if SNAPSHOT_FILE.exists():
        with open(SNAPSHOT_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def save_snapshot(db_hash, stats):
    """保存当前快照"""
    with open(SNAPSHOT_FILE, 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'db_hash': db_hash,
            'stats': stats
        }, f, ensure_ascii=False, indent=2)

def get_backup_stats():
    """获取数据库统计"""
    import sqlite3
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM intel')
    total = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM intel WHERE date(created_at) = date("now")')
    today = c.fetchone()[0]
    c.execute('SELECT category, COUNT(*) FROM intel GROUP BY category')
    by_category = c.fetchall()
    conn.close()
    return {'total': total, 'today': today, 'by_category': by_category}

def backup():
    """执行智能备份"""
    print("=" * 50)
    print("Intel Station - Smart Backup")
    print("=" * 50)
    
    # 确保备份目录存在
    BACKUP_DIR.mkdir(exist_ok=True)
    
    # 获取当前状态
    current_hash = get_db_hash()
    if current_hash is None:
        print("Database not found, skipping backup")
        return False
    
    current_stats = get_backup_stats()
    print(f"Current: {current_stats['total']} records, {current_stats['today']} today")
    
    # 检查快照
    old_snapshot = get_snapshot()
    
    if old_snapshot:
        old_hash = old_snapshot.get('db_hash', '')
        print(f"Last backup hash: {old_hash[:16]}...")
        print(f"Current hash:     {current_hash[:16]}...")
        
        if old_hash == current_hash:
            print("\nNo changes detected, skipping backup")
            return False
        else:
            print("\nChanges detected, creating backup...")
    else:
        print("\nFirst backup...")
    
    # 创建备份
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = BACKUP_DIR / f"intel_backup_{timestamp}.db"
    
    # 复制数据库
    import shutil
    shutil.copy2(DB_PATH, backup_file)
    
    # 同时导出JSON
    export_file = BACKUP_DIR / f"intel_export_{timestamp}.json"
    import sqlite3
    conn = sqlite3.connect(str(DB_PATH))
    c = conn.cursor()
    c.execute('SELECT * FROM intel ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    
    with open(export_file, 'w', encoding='utf-8') as f:
        json.dump({
            'backup_time': timestamp,
            'stats': current_stats,
            'records': [
                {'id': r[0], 'content': r[1], 'keywords': r[2], 'category': r[3], 'created_at': r[4]}
                for r in rows
            ]
        }, f, ensure_ascii=False, indent=2)
    
    # 更新快照
    save_snapshot(current_hash, current_stats)
    
    print(f"Backup created: {backup_file.name}")
    print(f"Export created: {export_file.name}")
    return True

def restore(backup_file):
    """恢复备份"""
    import shutil
    if DB_PATH.exists():
        # 先备份当前
        current_hash = get_db_hash()
        save_snapshot(current_hash, get_backup_stats())
    
    shutil.copy2(backup_file, DB_PATH)
    print(f"Restored from: {backup_file}")

def list_backups():
    """列出所有备份"""
    if not BACKUP_DIR.exists():
        print("No backups found")
        return
    
    backups = list(BACKUP_DIR.glob("*.db"))
    backups.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    print(f"Found {len(backups)} backups:\n")
    for b in backups[:10]:
        mtime = datetime.fromtimestamp(b.stat().st_mtime).strftime('%Y-%m-%d %H:%M')
        size = b.stat().st_size
        print(f"  {mtime}  {b.name}  ({size/1024:.1f} KB)")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Intel Station Backup Tool")
        print("Usage: backup.py [backup|restore|list]")
        sys.exit(1)
    
    cmd = sys.argv[1].lower()
    
    if cmd == "backup":
        backup()
    elif cmd == "restore":
        if len(sys.argv) < 3:
            print("Usage: backup.py restore <backup_file>")
        else:
            restore(sys.argv[2])
    elif cmd == "list":
        list_backups()
    else:
        print(f"Unknown command: {cmd}")
