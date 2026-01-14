import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    telegram_id TEXT,
    amount INTEGER,
    status TEXT
)
""")
conn.commit()

def mark_paid(order_id):
    cur.execute(
        "UPDATE orders SET status='PAID' WHERE order_id=?",
        (order_id,)
    )
    conn.commit()