import sqlite3

# Step 16.6
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Select and print title column in alphabetical order
cursor.execute('SELECT title FROM books ORDER BY title ASC')
titles = cursor.fetchall()
for title in titles:
    print(title[0])

conn.close()