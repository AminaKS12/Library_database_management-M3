show databases;
use library;

-- Assignment based on library database management
-- 1. Joins 
-- a. List all books with their authors
SELECT Books.Title, Authors.Name 
FROM Books 
JOIN Authors ON Books.AuthorID = Authors.AuthorID;

-- b. Show all books borrowed along with the member’s name
SELECT Borrowing.BorrowID, Books.Title, Members.Name, Borrowing.BorrowDate, Borrowing.ReturnDate
FROM Borrowing 
JOIN Books ON Borrowing.BookID = Books.BookID
JOIN Members ON Borrowing.MemberID = Members.MemberID;

-- c. Find members who have borrowed Fantasy books
SELECT DISTINCT Members.Name 
FROM Borrowing 
JOIN Books ON Borrowing.BookID = Books.BookID 
JOIN Members ON Borrowing.MemberID = Members.MemberID
WHERE Books.Category = 'Fantasy';


-- 2. Indexing for Optimization
-- a. Create an index on AuthorID in Books for faster lookup
CREATE INDEX idx_authorID ON Books(AuthorID);

-- b. Create an index on BookID in Borrowing for faster lookup
CREATE INDEX idx_bookID ON Borrowing(BookID);


-- 3. Views
-- a. Create a view to display borrowed books and their members
CREATE VIEW BorrowedBooks AS
SELECT Borrowing.BorrowID, Books.Title, Members.Name, Borrowing.BorrowDate, Borrowing.ReturnDate
FROM Borrowing 
JOIN Books ON Borrowing.BookID = Books.BookID
JOIN Members ON Borrowing.MemberID = Members.MemberID;

-- b. Query the view
SELECT * FROM BorrowedBooks;


-- 4. Stored Procedure
-- a. Create a stored procedure to list books by category
DELIMITER //
CREATE PROCEDURE GetBooksByCategory(IN book_category VARCHAR(50))
BEGIN
    SELECT * FROM Books WHERE Category = book_category;
END //
DELIMITER ;

-- Call the procedure
CALL GetBooksByCategory('Science Fiction');


-- 5. User-defined Function
-- a. Create a function to calculate late fine (₹5 per day after 7 days)
DELIMITER //
CREATE FUNCTION CalculateLateFine(return_date DATE, borrow_date DATE) 
RETURNS DECIMAL(10,2) DETERMINISTIC
BEGIN
    DECLARE days_late INT;
    DECLARE fine_amount DECIMAL(10,2);
    
    SET days_late = DATEDIFF(return_date, borrow_date) - 7;
    
    IF days_late > 0 THEN
        SET fine_amount = days_late * 5;
    ELSE
        SET fine_amount = 0;
    END IF;
    
    RETURN fine_amount;
END //
DELIMITER ;

-- Example usage
SELECT CalculateLateFine('2024-05-20', '2024-05-05') AS FineAmount;

-- 6. Triggers
-- a. Create a trigger to update fine when a book is returned late
DELIMITER //
CREATE TRIGGER UpdateFine 
BEFORE UPDATE ON Borrowing
FOR EACH ROW
BEGIN
    IF NEW.ReturnDate > DATE_ADD(NEW.BorrowDate, INTERVAL 7 DAY) THEN
        SET @fine = CalculateLateFine(NEW.ReturnDate, NEW.BorrowDate);
        UPDATE Members SET FineAmount = @fine WHERE MemberID = NEW.MemberID;
    END IF;
END //
DELIMITER ;

-- Test the trigger by updating ReturnDate to a late value
UPDATE Borrowing SET ReturnDate = '2024-05-25' WHERE BorrowID = 1;



-- Test the trigger by updating ReturnDate to a late value
UPDATE Borrowing SET ReturnDate = '2024-05-25' WHERE BorrowID = 1;

