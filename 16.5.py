import csv
import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Read and insert data from books2.csv
with open('books2.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', row)

# Commit changes and close connection
conn.commit()
conn.close()