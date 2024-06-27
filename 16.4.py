import sqlite3

# Step 16.4
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Create books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()