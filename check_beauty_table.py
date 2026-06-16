import sqlite3
from pathlib import Path

db = Path(r'c:\wamp64\www\SDI STORE 1\sdi_market\db.sqlite3')
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='marketplace_beautyappointment'")
print(cur.fetchone())
conn.close()
