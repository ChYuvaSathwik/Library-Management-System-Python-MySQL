from database import get_connection


def add_book():

    connection = get_connection()
    cursor = connection.cursor()

    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    category = input("Enter Category: ")
    quantity = int(input("Enter Quantity: "))

    query = """
    INSERT INTO books(title, author, category, quantity)
    VALUES (%s, %s, %s, %s)
    """

    values = (title, author, category, quantity)

    cursor.execute(query, values)

    connection.commit()

    print("✅ Book Added Successfully!")

    connection.close()


def view_books():

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM books"

    cursor.execute(query)

    books = cursor.fetchall()

    if len(books) == 0:
        print("❌ No Books Found.")

    else:

        for book in books:

            print("-" * 40)
            print(f"Book ID   : {book[0]}")
            print(f"Title     : {book[1]}")
            print(f"Author    : {book[2]}")
            print(f"Category  : {book[3]}")
            print(f"Quantity  : {book[4]}")

    connection.close()


def update_book():

    connection = get_connection()
    cursor = connection.cursor()

    book_id = int(input("Enter Book ID: "))
    new_quantity = int(input("Enter New Quantity: "))

    query = """
    UPDATE books
    SET quantity = %s
    WHERE book_id = %s
    """

    values = (new_quantity, book_id)

    cursor.execute(query, values)

    connection.commit()

    if cursor.rowcount > 0:
        print("✅ Book Updated Successfully!")
    else:
        print("❌ Book ID Not Found!")

    connection.close()


def delete_book():

    connection = get_connection()
    cursor = connection.cursor()

    book_id = int(input("Enter Book ID to Delete: "))

    query = """
    DELETE FROM books
    WHERE book_id = %s
    """

    values = (book_id,)

    cursor.execute(query, values)

    connection.commit()

    if cursor.rowcount > 0:
        print("✅ Book Deleted Successfully!")
    else:
        print("❌ Book ID Not Found!")

    connection.close()


def search_book():

    connection = get_connection()
    cursor = connection.cursor()

    title = input("Enter Book Title to Search: ")

    query = """
    SELECT *
    FROM books
    WHERE title LIKE %s
    """

    values = ("%" + title + "%",)

    cursor.execute(query, values)

    books = cursor.fetchall()

    if len(books) == 0:

        print("❌ No Book Found.")

    else:

        for book in books:

            print("-" * 40)
            print(f"Book ID   : {book[0]}")
            print(f"Title     : {book[1]}")
            print(f"Author    : {book[2]}")
            print(f"Category  : {book[3]}")
            print(f"Quantity  : {book[4]}")

    connection.close()
