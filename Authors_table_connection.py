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
    conn = mysql.connector.connect(host=host1, user=user1, password=user1, database=database1, port=port1)
    
    if conn.is_connected():
        print("Connection successful")
    
    cursor = conn.cursor()

    while True:
        print("\nChoose an operation:")
        print("1. Insert an Author")
        print("2. Update Author Name")
        print("3. Delete an Author")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter author name: ")
            country = input("Enter author's country: ")
            
            insert_query = "INSERT INTO Authors (Name, Country) VALUES (%s, %s)"
            cursor.execute(insert_query, (name, country))
            conn.commit()
            print("Author inserted successfully!")

        elif choice == "2":
            author_id = input("Enter Author ID to update name: ")
            new_name = input("Enter new name: ")
            
            update_query = "UPDATE Authors SET Name = %s WHERE AuthorID = %s"
            cursor.execute(update_query, (new_name, author_id))
            conn.commit()
            print("Author name updated successfully!")

        elif choice == "3":
            delete_author_id = input("Enter Author ID to delete: ")
            
            delete_query = "DELETE FROM Authors WHERE AuthorID = %s"
            cursor.execute(delete_query, (delete_author_id,))
            conn.commit()
            print("Author deleted successfully!")

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
