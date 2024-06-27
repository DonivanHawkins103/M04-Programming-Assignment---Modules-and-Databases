import csv

books = [
    ['Author', 'Book'], 
    ['J R R Tolkien', 'The Hobbit'], 
    ['Lynne Truss', '"Eats, Shoots & Leaves"'],
    ]
with open('books', 'wt') as fout:  # a context manager
    csvout = csv.writer(fout)
    csvout.writerows(books)