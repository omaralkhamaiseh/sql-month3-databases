from database import create_database
import sqlite3
from books import add_book,get_all_books,find_book,update_book,delete_book
create_database()
# # add_book("Machine Learning","Omar",30.0)
# get_all_books()
# delete_book(1)
# get_all_books()
# # find_book(99)
# # update_book(1,40.0)
# # find_book(1)
while True:
    try:
        print("===== LIBRARY MANAGEMENT =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Find Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Exit")
        print()
        choice=int(input("Choose an option:")) 
        if choice == 1:
            title=input("Enter book title:")
            author=input("Enter author:")
            price=float(input("Enter price:"))
            add_book(title,author,price)
            print("Book added successfully!")
        elif choice == 2:
            get_all_books()
        elif choice == 3:
            id=int(input("Enter book ID:"))
            find_book(id)
        elif choice == 4:
            id=int(input("Enter book ID:"))
            new_price=float(input("Enter new price:"))
            result=update_book(id,new_price)
            if result:
                print("Book updated successfully!")
            else:
                print("Book not found!")    
        elif choice == 5:
            id=int(input("Enter book ID:"))
            result=delete_book(id)
            if result:
                print("Book deleted successfully!")
            else:
                print("Book not found!")
        elif choice == 6:
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")
    except sqlite3.Error as error:
        print("The error is :",error)