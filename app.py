import streamlit as st
import mysql.connector
from mysql.connector import Error
import pandas as pd

# DB Connection
def get_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database='Library',
        port=3307
    )

# UI
st.set_page_config(page_title="Library Management System", layout="wide")
st.title("📚 Library Management System")

tabs = st.tabs(["Authors", "Books", "Members", "Borrowing"])

# ----------------------- Authors -----------------------
with tabs[0]:
    st.header("👤 Manage Authors")

    with st.form("author_form", clear_on_submit=True):
        action = st.selectbox("Action", ["Insert", "Update", "Delete"])
        author_id = st.text_input("Author ID (for Update/Delete)")
        name = st.text_input("Author Name")
        country = st.text_input("Country")
        submitted = st.form_submit_button("Submit")

        if submitted:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                if action == "Insert":
                    query = "INSERT INTO Authors (Name, Country) VALUES (%s, %s)"
                    cursor.execute(query, (name, country))
                    st.success("Author inserted.")
                elif action == "Update":
                    query = "UPDATE Authors SET Name = %s WHERE AuthorID = %s"
                    cursor.execute(query, (name, author_id))
                    st.success("Author updated.")
                elif action == "Delete":
                    query = "DELETE FROM Authors WHERE AuthorID = %s"
                    cursor.execute(query, (author_id,))
                    st.success("Author deleted.")

                conn.commit()
                cursor.close()
                conn.close()
            except Error as e:
                st.error(f"Database Error: {e}")

# ----------------------- Books -----------------------
with tabs[1]:
    st.header("📖 Manage Books")

    with st.form("book_form", clear_on_submit=True):
        action = st.selectbox("Action", ["Insert", "Update", "Delete"])
        book_id = st.text_input("Book ID (for Update/Delete)")
        title = st.text_input("Book Title")
        author_id = st.text_input("Author ID")
        category = st.text_input("Category")
        price = st.text_input("Price")
        submitted = st.form_submit_button("Submit")

        if submitted:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                if action == "Insert":
                    query = "INSERT INTO Books (Title, AuthorID, Category, Price) VALUES (%s, %s, %s, %s)"
                    cursor.execute(query, (title, author_id, category, price))
                    st.success("Book inserted.")
                elif action == "Update":
                    query = "UPDATE Books SET Price = %s WHERE BookID = %s"
                    cursor.execute(query, (price, book_id))
                    st.success("Book price updated.")
                elif action == "Delete":
                    query = "DELETE FROM Books WHERE BookID = %s"
                    cursor.execute(query, (book_id,))
                    st.success("Book deleted.")

                conn.commit()
                cursor.close()
                conn.close()
            except Error as e:
                st.error(f"Database Error: {e}")

# ----------------------- Members -----------------------
with tabs[2]:
    st.header("🧑 Manage Members")

    with st.form("member_form", clear_on_submit=True):
        action = st.selectbox("Action", ["Insert", "Update", "Delete"])
        member_id = st.text_input("Member ID (for Update/Delete)")
        member_name = st.text_input("Member Name")
        join_date = st.date_input("Join Date")
        submitted = st.form_submit_button("Submit")

        if submitted:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                if action == "Insert":
                    query = "INSERT INTO Members (Name, JoinDate) VALUES (%s, %s)"
                    cursor.execute(query, (member_name, join_date))
                    st.success("Member inserted.")
                elif action == "Update":
                    query = "UPDATE Members SET Name = %s WHERE MemberID = %s"
                    cursor.execute(query, (member_name, member_id))
                    st.success("Member name updated.")
                elif action == "Delete":
                    query = "DELETE FROM Members WHERE MemberID = %s"
                    cursor.execute(query, (member_id,))
                    st.success("Member deleted.")

                conn.commit()
                cursor.close()
                conn.close()
            except Error as e:
                st.error(f"Database Error: {e}")

# ----------------------- Borrowing -----------------------
with tabs[3]:
    st.header("📅 Manage Borrowing Records")

    with st.form("borrow_form", clear_on_submit=True):
        action = st.selectbox("Action", ["Insert", "Update", "Delete"])
        borrow_id = st.text_input("Borrow ID (for Update/Delete)")
        member_id = st.text_input("Member ID")
        book_id = st.text_input("Book ID")
        borrow_date = st.date_input("Borrow Date")
        return_date = st.date_input("Return Date")
        submitted = st.form_submit_button("Submit")

        if submitted:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                if action == "Insert":
                    query = "INSERT INTO Borrowing (MemberID, BookID, BorrowDate, ReturnDate) VALUES (%s, %s, %s, %s)"
                    cursor.execute(query, (member_id, book_id, borrow_date, return_date))
                    st.success("Borrowing record inserted.")
                elif action == "Update":
                    query = "UPDATE Borrowing SET ReturnDate = %s WHERE BorrowID = %s"
                    cursor.execute(query, (return_date, borrow_id))
                    st.success("Return date updated.")
                elif action == "Delete":
                    query = "DELETE FROM Borrowing WHERE BorrowID = %s"
                    cursor.execute(query, (borrow_id,))
                    st.success("Borrowing record deleted.")

                conn.commit()
                cursor.close()
                conn.close()
            except Error as e:
                st.error(f"Database Error: {e}")
