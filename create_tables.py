import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Create SecurityEvent table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS marketplace_securityevent (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_type VARCHAR(50) NOT NULL,
        source_ip VARCHAR(50),
        path VARCHAR(255),
        method VARCHAR(10),
        status_code INTEGER,
        response_time_ms INTEGER,
        user_agent VARCHAR(500),
        description TEXT,
        created_at DATETIME NOT NULL,
        user_id INTEGER REFERENCES marketplace_user(id)
    )
''')

# Create IPBlocklist table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS marketplace_ipblocklist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ip_address VARCHAR(50) NOT NULL UNIQUE,
        reason VARCHAR(255),
        is_active BOOLEAN NOT NULL DEFAULT 1,
        created_at DATETIME NOT NULL,
        blocked_until DATETIME,
        created_by_id INTEGER REFERENCES marketplace_user(id)
    )
''')

conn.commit()
print('Tables created successfully')

# Verify tables exist
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%security%'")
print('Security tables:', cursor.fetchall())

conn.close()