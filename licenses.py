import sqlite3

conn = sqlite3.connect('licenses.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS licenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    license_code TEXT NOT NULL,
    email TEXT NOT NULL,
    active INTEGER DEFAULT 0
)
''')

# Тестові ліцензії
cursor.execute("INSERT OR IGNORE INTO licenses (license_code, email, active) VALUES ('ABC123','test@mail.com',0)")
cursor.execute("INSERT OR IGNORE INTO licenses (license_code, email, active) VALUES ('XYZ789','user@mail.com',0)")

conn.commit()
conn.close()

print("Database initialized!")
