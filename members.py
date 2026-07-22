from database import get_connection


def add_member():

    connection = get_connection()
    cursor = connection.cursor()

    name = input("Enter Member Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    query = """
    INSERT INTO members(name, phone, email)
    VALUES (%s, %s, %s)
    """

    values = (name, phone, email)

    cursor.execute(query, values)

    connection.commit()

    print("✅ Member Added Successfully!")

    connection.close()


def view_members():

    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM members"

    cursor.execute(query)

    members = cursor.fetchall()

    if len(members) == 0:

        print("❌ No Members Found.")

    else:

        for member in members:

            print("-" * 40)
            print(f"Member ID : {member[0]}")
            print(f"Name      : {member[1]}")
            print(f"Phone     : {member[2]}")
            print(f"Email     : {member[3]}")

    connection.close()


def update_member():

    connection = get_connection()
    cursor = connection.cursor()

    member_id = int(input("Enter Member ID: "))
    new_phone = input("Enter New Phone Number: ")

    query = """
    UPDATE members
    SET phone = %s
    WHERE member_id = %s
    """

    values = (new_phone, member_id)

    cursor.execute(query, values)

    connection.commit()

    if cursor.rowcount > 0:
        print("✅ Member Updated Successfully!")
    else:
        print("❌ Member ID Not Found!")

    connection.close()


def delete_member():

    connection = get_connection()
    cursor = connection.cursor()

    member_id = int(input("Enter Member ID to Delete: "))

    query = """
    DELETE FROM members
    WHERE member_id = %s
    """

    values = (member_id,)

    cursor.execute(query, values)

    connection.commit()

    if cursor.rowcount > 0:
        print("✅ Member Deleted Successfully!")
    else:
        print("❌ Member ID Not Found!")

    connection.close()


def search_member():

    connection = get_connection()
    cursor = connection.cursor()

    name = input("Enter Member Name to Search: ")

    query = """
    SELECT *
    FROM members
    WHERE name LIKE %s
    """

    values = ("%" + name + "%",)

    cursor.execute(query, values)

    members = cursor.fetchall()

    if len(members) == 0:

        print("❌ No Member Found.")

    else:

        for member in members:

            print("-" * 40)
            print(f"Member ID : {member[0]}")
            print(f"Name      : {member[1]}")
            print(f"Phone     : {member[2]}")
            print(f"Email     : {member[3]}")

    connection.close()
