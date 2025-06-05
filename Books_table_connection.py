
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
        print("1. Insert a Book")
        print("2. Update Book Price")
        print("3. Delete a Book")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter book Title: ")
            author_id = input("Enter AuthorID: ")
            category = input("Enter book Category: ")
            price = input("Enter book Price: ")
            
            insert_query = "INSERT INTO Books (Title, AuthorID, Category, Price) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (title, author_id, category, price))
            conn.commit()
            print("Book inserted successfully!")

        elif choice == "2":
            book_id = input("Enter Book ID to update price: ")
            new_price = input("Enter new price: ")
            
            update_query = "UPDATE Books SET Price = %s WHERE BookID = %s"
            cursor.execute(update_query, (new_price, book_id))
            conn.commit()
            print("Book price updated successfully!")

        elif choice == "3":
            delete_book_id = input("Enter Book ID to delete: ")
            
            delete_query = "DELETE FROM Books WHERE BookID = %s"
            cursor.execute(delete_query, (delete_book_id,))
            conn.commit()
            print("Book deleted successfully!")

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
