import sqlite3
import os

DB_PATH = "bot_database.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Users table: progress and cooldown
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        phone TEXT,
        is_verified INTEGER DEFAULT 0,
        last_file_index INTEGER DEFAULT 0,
        last_received_at DATETIME
    )
    ''')
    
    # Files table: sequence of files with settings
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_id TEXT NOT NULL,
        file_type TEXT NOT NULL,
        caption TEXT,
        file_index INTEGER UNIQUE,
        cooldown_seconds INTEGER DEFAULT 3600,
        protect_content INTEGER DEFAULT 0,
        auto_delete_seconds INTEGER DEFAULT 0
    )
    ''')
    
    # Global settings table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    ''')
    
    # Broadcast log table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS broadcast_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sent_at DATETIME,
        success_count INTEGER,
        fail_count INTEGER
    )
    ''')
    
    # Default global settings
    cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('global_cooldown', '3600')")
    cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('admin_secret', 'admin123')")
    cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('welcome_img', 'https://via.placeholder.com/800x400?text=Premium+Verification')")
    cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('welcome_caption', 'Welcome to the most advanced bot! 🚀\nPlease verify yourself to continue.')")
    cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('skip_timer_link', 'https://t.me/your_channel')")
    
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
