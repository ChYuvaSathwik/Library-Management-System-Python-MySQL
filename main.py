from books import (
    add_book,
    view_books,
    update_book,
    delete_book,
    search_book
)

from members import (
    add_member,
    view_members,
    update_member,
    delete_member,
    search_member
)

from transactions import (
    issue_book,
    return_book,
    view_issued_books
)

from dashboard import dashboard


while True:

    print("\n===================================")
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("===================================")

    print("\n📚 BOOK MANAGEMENT")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Book")

    print("\n👤 MEMBER MANAGEMENT")
    print("6. Add Member")
    print("7. View Members")
    print("8. Update Member")
    print("9. Delete Member")
    print("10. Search Member")

    print("\n📖 TRANSACTION MANAGEMENT")
    print("11. Issue Book")
    print("12. Return Book")
    print("13. View Issued Books")

    print("\n📊 DASHBOARD")
    print("14. Dashboard")

    print("\n15. Exit")

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        add_book()

    elif choice == 2:
        view_books()

    elif choice == 3:
        update_book()

    elif choice == 4:
        delete_book()

    elif choice == 5:
        search_book()

    elif choice == 6:
        add_member()

    elif choice == 7:
        view_members()

    elif choice == 8:
        update_member()

    elif choice == 9:
        delete_member()

    elif choice == 10:
        search_member()

    elif choice == 11:
        issue_book()

    elif choice == 12:
        return_book()

    elif choice == 13:
        view_issued_books()

    elif choice == 14:
        dashboard()

    elif choice == 15:
        print("👋 Thank You!")
        break

    else:
        print("❌ Invalid Choice!")
