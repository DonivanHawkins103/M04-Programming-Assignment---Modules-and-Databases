from sqlalchemy import create_engine, Table, MetaData, select

# Step 16.8
# Connect to SQLite database using SQLAlchemy
engine = create_engine('sqlite:///books.db')
connection = engine.connect()

# Reflect the existing books table
metadata = MetaData()
books_table = Table('books', metadata, autoload=True, autoload_with=engine)

# Select and print title column in alphabetical order using SQLAlchemy
query = select([books_table.columns.title]).order_by(books_table.columns.title)
results = connection.execute(query).fetchall()
for result in results:
    print(result[0])

# Close connection
connection.close()