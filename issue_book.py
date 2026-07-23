import mysql.connector
from datetime import date

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sathwik@2004",
    database="library_management_system"
)

cursor = connection.cursor()

book_id = int(input("Enter Book ID: "))
member_id = int(input("Enter Member ID: "))

# Check if Book Exists
cursor.execute(
    "SELECT quantity FROM books WHERE book_id = %s",
    (book_id,)
)

book = cursor.fetchone()

if book is None:
    print("❌ Book ID does not exist.")

# Check Book Quantity
elif book[0] <= 0:
    print("❌ Book is Out of Stock!")

else:
    # Check if Member Exists
    cursor.execute(
        "SELECT * FROM members WHERE member_id = %s",
        (member_id,)
    )

    member = cursor.fetchone()

    if member is None:
        print("❌ Member ID does not exist.")

    else:
        # Check if the member already has this book
        cursor.execute(
            """
            SELECT *
            FROM transactions
            WHERE book_id = %s
            AND member_id = %s
            AND status = %s
            """,
            (book_id, member_id, "Issued")
        )

        already_issued = cursor.fetchone()

        if already_issued is not None:
            print("❌ This member has already issued this book.")

        else:
            issue_date = date.today()

            insert_query = """
            INSERT INTO transactions
            (book_id, member_id, issue_date, return_date, status)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                book_id,
                member_id,
                issue_date,
                None,
                "Issued"
            )

            cursor.execute(insert_query, values)

            update_query = """
            UPDATE books
            SET quantity = quantity - 1
            WHERE book_id = %s
            """

            cursor.execute(update_query, (book_id,))

            connection.commit()

            print("✅ Book Issued Successfully!")

connection.close()
