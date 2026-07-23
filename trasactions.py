from database import get_connection
from datetime import date, timedelta


def issue_book():

    connection = get_connection()
    cursor = connection.cursor()

    book_id = int(input("Enter Book ID: "))
    member_id = int(input("Enter Member ID: "))

    cursor.execute(
        "SELECT quantity FROM books WHERE book_id=%s",
        (book_id,)
    )

    book = cursor.fetchone()

    if book is None:

        print("❌ Book ID does not exist.")

    elif book[0] <= 0:

        print("❌ Book Out of Stock!")

    else:

        cursor.execute(
            "SELECT * FROM members WHERE member_id=%s",
            (member_id,)
        )

        member = cursor.fetchone()

        if member is None:

            print("❌ Member ID does not exist.")

        else:

            cursor.execute(
                """
                SELECT *
                FROM transactions
                WHERE book_id=%s
                AND member_id=%s
                AND status='Issued'
                """,
                (book_id, member_id)
            )

            issued = cursor.fetchone()

            if issued:

                print("❌ This member already has this book.")

            else:

                issue_date = date.today()
                due_date = issue_date + timedelta(days=14)

                cursor.execute(
                    """
                    INSERT INTO transactions
                    (book_id,member_id,issue_date,due_date,return_date,status)
                    VALUES(%s,%s,%s,%s,%s,%s)
                    """,
                    (
                        book_id,
                        member_id,
                        issue_date,
                        due_date,
                        None,
                        "Issued"
                    )
                )

                cursor.execute(
                    """
                    UPDATE books
                    SET quantity=quantity-1
                    WHERE book_id=%s
                    """,
                    (book_id,)
                )

                connection.commit()

                print("✅ Book Issued Successfully!")
                print(f"📅 Due Date : {due_date}")

    connection.close()


def return_book():

    connection = get_connection()
    cursor = connection.cursor()

    transaction_id = int(input("Enter Transaction ID: "))

    cursor.execute(
        """
        SELECT
            book_id,
            due_date,
            status
        FROM transactions
        WHERE transaction_id=%s
        """,
        (transaction_id,)
    )

    transaction = cursor.fetchone()

    if transaction is None:

        print("❌ Transaction ID does not exist.")

    elif transaction[2] == "Returned":

        print("❌ Book already returned.")

    else:

        return_date = date.today()

        due_date = transaction[1]

        fine = 0

        if return_date > due_date:

            late_days = (return_date - due_date).days

            fine = late_days * 10

            print(f"⚠️ Late by {late_days} days")
            print(f"💰 Fine : ₹{fine}")

        else:

            print("✅ Returned on time.")
            print("💰 Fine : ₹0")

        cursor.execute(
            """
            UPDATE transactions
            SET return_date=%s,
                status=%s
            WHERE transaction_id=%s
            """,
            (
                return_date,
                "Returned",
                transaction_id
            )
        )

        cursor.execute(
            """
            UPDATE books
            SET quantity=quantity+1
            WHERE book_id=%s
            """,
            (transaction[0],)
        )

        connection.commit()

        print("✅ Book Returned Successfully!")

    connection.close()


def view_issued_books():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            t.transaction_id,
            b.title,
            m.name,
            t.issue_date,
            t.due_date,
            t.return_date,
            t.status
        FROM transactions t
        INNER JOIN books b
        ON t.book_id=b.book_id
        INNER JOIN members m
        ON t.member_id=m.member_id
        """
    )

    rows = cursor.fetchall()

    if len(rows) == 0:

        print("❌ No Transactions Found.")

    else:

        for row in rows:

            print("-"*50)
            print(f"Transaction ID : {row[0]}")
            print(f"Book           : {row[1]}")
            print(f"Member         : {row[2]}")
            print(f"Issue Date     : {row[3]}")
            print(f"Due Date       : {row[4]}")
            print(f"Return Date    : {row[5]}")
            print(f"Status         : {row[6]}")

    connection.close()
