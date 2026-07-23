import mysql.connector
from datetime import date

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sathwik@2004",
    database="library_management_system"
)

cursor = connection.cursor()

transaction_id = int(input("Enter Transaction ID: "))

# Check Transaction

cursor.execute(
    """
    SELECT book_id, status
    FROM transactions
    WHERE transaction_id = %s
    """,
    (transaction_id,)
)

transaction = cursor.fetchone()

if transaction is None:

    print("❌ Transaction ID does not exist.")

elif transaction[1] == "Returned":

    print("❌ Book has already been returned.")

else:

    book_id = transaction[0]

    # Update Transaction

    cursor.execute(
        """
        UPDATE transactions
        SET return_date = %s,
            status = %s
        WHERE transaction_id = %s
        """,
        (
            date.today(),
            "Returned",
            transaction_id
        )
    )

    # Increase Quantity

    cursor.execute(
        """
        UPDATE books
        SET quantity = quantity + 1
        WHERE book_id = %s
        """,
        (book_id,)
    )

    connection.commit()

    print("✅ Book Returned Successfully!")

connection.close()
