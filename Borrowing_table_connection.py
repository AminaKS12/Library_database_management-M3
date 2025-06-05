import mysql.connector
from mysql.connector import Error

# Database Credentials
host1 = '127.0.0.1'
user1 = 'root'
password1 = 'root'
database1 = 'Library'
port1 = 3307

# Establish connection
try:
    conn = mysql.connector.connect(host=host1, user=user1, password=password1, database=database1, port=port1)
    
    if conn.is_connected():
        print("Connection successful")
    
    cursor = conn.cursor()

    while True:
        print("\nChoose an operation:")
        print("1. Insert a Borrowing Record")
        print("2. Update Return Date")
        print("3. Delete a Borrowing Record")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            member_id = input("Enter Member ID: ")
            book_id = input("Enter Book ID: ")
            borrow_date = input("Enter Borrow Date (YYYY-MM-DD): ")
            return_date = input("Enter Return Date (YYYY-MM-DD): ")
            
            insert_query = "INSERT INTO Borrowing (MemberID, BookID, BorrowDate, ReturnDate) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (member_id, book_id, borrow_date, return_date))
            conn.commit()
            print("Borrowing record inserted successfully!")

        elif choice == "2":
            borrow_id = input("Enter BorrowID to update return date: ")
            new_return_date = input("Enter new return date (YYYY-MM-DD): ")
            
            update_query = "UPDATE Borrowing SET ReturnDate = %s WHERE BorrowID = %s"
            cursor.execute(update_query, (new_return_date, borrow_id))
            conn.commit()
            print("Return date updated successfully!")

        elif choice == "3":
            delete_borrow_id = input("Enter BorrowID to delete record: ")
            
            delete_query = "DELETE FROM Borrowing WHERE BorrowID = %s"
            cursor.execute(delete_query, (delete_borrow_id,))
            conn.commit()
            print("Borrowing record deleted successfully!")

        elif choice == "4":
            print("Exiting... ")
            break

        else:
            print("Invalid choice. Please try again.")

    # Close Cursor & Connection
    cursor.close()
    conn.close()
    print("Database connection closed.")

except Error as e:
    print("Connection error:", e)
