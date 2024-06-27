import csv

#Step 16.2
with open('books.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    books = list(reader)

print(books)