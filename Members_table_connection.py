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
        print("1. Insert a Member")
        print("2. Update Member Name")
        print("3. Delete a Member")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter member name: ")
            join_date = input("Enter join date (YYYY-MM-DD): ")
            
            insert_query = "INSERT INTO Members (Name, JoinDate) VALUES (%s, %s)"
            cursor.execute(insert_query, (name, join_date))
            conn.commit()
            print("Member inserted successfully!")

        elif choice == "2":
            member_id = input("Enter Member ID to update name: ")
            new_name = input("Enter new name: ")
            
            update_query = "UPDATE Members SET Name = %s WHERE MemberID = %s"
            cursor.execute(update_query, (new_name, member_id))
            conn.commit()
            print("Member name updated successfully!")

        elif choice == "3":
            delete_member_id = input("Enter Member ID to delete: ")
            
            delete_query = "DELETE FROM Members WHERE MemberID = %s"
            cursor.execute(delete_query, (delete_member_id,))
            conn.commit()
            print("Member deleted successfully!")

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
