import sqlite3

# Step 16.7
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Select and print all columns in order of publication
cursor.execute('SELECT title, author, year FROM books ORDER BY year ASC')
books = cursor.fetchall()
for book in books:
    print(book)

conn.close()