-- Tasks
-- 1. Create a Database
-- Create a database named Library.

show databases;
create database Library;
show databases;
use Library;


-- 2. Create TablesCreate the following tables with appropriate columns and data types:
-- Books: 
-- BookID (Primary Key, Auto Increment), Title (VARCHAR), AuthorID (Foreign Key), Category (VARCHAR), Price (DECIMAL)
-- Authors: 
-- AuthorID (Primary Key, Auto Increment), Name (VARCHAR), Country (VARCHAR)
-- Members: 
-- MemberID (Primary Key, Auto Increment), Name (VARCHAR), JoinDate (DATE)
-- Borrowing: 
-- BorrowID (Primary Key, Auto Increment), MemberID (Foreign Key), BookID (Foreign Key), BorrowDate (DATE), ReturnDate (DATE)

create table Books(BookID int(8) not null primary key auto_increment, Title varchar(50), AuthorID int(8), Category varchar(50), Price decimal(10,2) not null, foreign key(AuthorID) references Authors(AuthorID));

create table Authors(AuthorID int(8) not null primary key auto_increment, Name varchar(50), Country varchar(20));

show tables;

create table Members(MemberID int(8) not null primary key auto_increment, Name varchar(50), JoinDate date);

create table Borrowing(BorrowID int(8) not null primary key auto_increment, MemberID int(8),foreign key(memberID)references Members(MemberID), BookID int(8), foreign key(BookID) references Books(BookID), BorrowDate date, ReturnDate date);

desc Books;
desc Authors;
desc Members;
desc Borrowing;

-- 3. Insert Data
-- Add sample data into each table.

insert into Books values
(01, "The Great Gatsby",  101, "Classic Fiction", 350.00),
(02, "To Kill a Mockingbird",  102, "Classic Fiction", 450.00),
(03, "The Hitchhiker's Guido to the Galaxy",  103, "Science Fiction", 550.00),
(04, "Pride and Prejudice",  104, "Classic Fiction", 550.00),
(05, "The Lion, the Witch and the Wordrobe",  105, "Fantasy", 550.00);

insert into Books values
(06, "1984",  106, "Dystopian Fiction", 330.00),
(07, "The Handmaid's Tale",  107, "Dystopian Fiction", 430.00),
(08, "The Nightingale",  108, "Historical Fiction", 510.00),
(09, "The Power",  109, "Science Fiction", 540.00),
(10, "The Song of Achilles",  110, "Historical Fiction", 420.00);

insert into Authors values
(101, "F.Scott Fitzgerald","US"),
(102, "Harper Lee","US"),
(103, "Douglas Adams","UK"),
(104, "Jane Austen","UK"),
(105, "C.S. Lewis","UK");

insert into Authors values
(106, "George Orwell","UK"),
(107, "Harper Lee","Canada"),
(108, "Kristin Hannah","US"),
(109, "Naomi Alderman","UK"),
(110, "Madeline Miller","Us");

insert into Members (Name, JoinDate) values
('Aarav Sharma', '2023-06-15'),
('Meera Iyer', '2023-07-22'),
('Kabir Das', '2023-08-10'),
('Priya Patel', '2023-09-05'),
('Sanjay Gupta', '2023-10-18'),
('Ananya Rao', '2023-11-30'),
('Rohan Mehta', '2024-01-12'),
('Neha Verma', '2024-02-25'),
('Vikram Singh', '2024-03-19'),
('Ishita Bose', '2024-04-07');

insert into Borrowing (BorrowID, MemberID, BookID, BorrowDate, ReturnDate) values
(1, 1, 3, '2024-05-01', '2024-05-15'),
(2, 2, 7, '2024-05-02', '2024-05-16'),
(3, 3, 2, '2024-05-03', '2024-05-17'),
(4, 4, 10, '2024-05-04', '2024-05-18'),
(5, 5, 5, '2024-05-05', '2024-05-19'),
(6, 6, 8, '2024-05-06', '2024-05-20'),
(7, 7, 1, '2024-05-07', '2024-05-21'),
(8, 8, 9, '2024-05-08', '2024-05-22'),
(9, 9, 4, '2024-05-09', '2024-05-23'),
(10, 10, 6, '2024-05-10', '2024-05-24');

-- 4. Queries
-- a. List all books and their authors
SELECT Books.Title, Authors.Name 
FROM Books 
JOIN Authors ON Books.AuthorID = Authors.AuthorID;

-- b. Find all books borrowed by "Alice"
SELECT Books.Title 
FROM Borrowing 
JOIN Books ON Borrowing.BookID = Books.BookID 
JOIN Members ON Borrowing.MemberID = Members.MemberID 
WHERE Members.Name = 'Alice';

-- c. Find all books that cost more than $20
SELECT Title, Price 
FROM Books 
WHERE Price > 20;

-- 5. Bonus Queries
-- a. Add a column 'Fine' in the Borrowing table to calculate late fees
ALTER TABLE Borrowing ADD COLUMN Fine DECIMAL(10,2) DEFAULT 0;

-- b. Update the Fine column based on overdue days (assuming $2 per day after 7 days)
UPDATE Borrowing 
SET Fine = 
    CASE 
        WHEN DATEDIFF(ReturnDate, BorrowDate) > 7 
        THEN (DATEDIFF(ReturnDate, BorrowDate) - 7) * 2 
        ELSE 0 
    END;

-- c. Find the most expensive book in the library
SELECT Title, Price 
FROM Books 
ORDER BY Price DESC 
LIMIT 1;

-- d. Calculate the total revenue generated if all books were sold
SELECT SUM(Price) AS TotalRevenue 
FROM Books;

-- e. Find the total number of books in each category
SELECT Category, COUNT(*) AS TotalBooks 
FROM Books 
GROUP BY Category;

-- f. Calculate the average price of books in each category
SELECT Category, AVG(Price) AS AvgPrice 
FROM Books 
GROUP BY Category;

-- g. Find the total fine collected for late returns
SELECT SUM(Fine) AS TotalFineCollected 
FROM Borrowing;

-- h. List all members who joined the library in 2025
SELECT * 
FROM Members 
WHERE YEAR(JoinDate) = 2025;

-- i. Find which category generates the highest revenue
SELECT Category, SUM(Price) AS TotalCategoryRevenue 
FROM Books 
GROUP BY Category 
ORDER BY TotalCategoryRevenue DESC 
LIMIT 1;


