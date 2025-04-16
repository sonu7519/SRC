import sqlite3

# Connect (or create) database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insert some sample users
cursor.executemany('''
INSERT INTO users (username, email)
VALUES (?, ?)
''', [
    ('alice', 'alice@example.com'),
    ('bob', 'bob@example.com'),
    ('admin', 'admin@domain.com')
])

conn.commit()
conn.close()

print("Database created with sample users.")