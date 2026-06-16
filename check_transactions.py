import sqlite3

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
cur.execute('SELECT id, sender_id, receiver_id, amount, type, status FROM marketplace_transaction')
rows = cur.fetchall()
print('nb', len(rows))
bad = []
for r in rows:
    amount = r[3]
    try:
        if amount is None:
            continue
        float(amount)
    except Exception:
        bad.append(r)
print('bad', bad)
con.close()
