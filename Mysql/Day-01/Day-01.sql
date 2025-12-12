USE mysql;

-- Creating a table 
CREATE TABLE users (
 id INT AUTO_INCREMENT PRIMARY KEY,
 username VARCHAR(50) NOT NULL,
 email VARCHAR(100) NOT NULL UNIQUE,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Cheaking if the table is created 
SELECT * FROM users;

-- Droppint the data base 
DROP TABLE users;

-- Data types 
-- Used for defining the type of data that can be stored in a column.
-- Int: used for whole numbers.
-- Varchar(size): used for variable-length strings.
-- Enum: used for a object with a value chosen from a list of permitted values.
-- Date: used for date values.
-- Timestamp: stores date and time, automatically set to the current timestamp when the row is created or updated.

-- Constraints
-- Constraints are rules applied to colums to ensure integrity and accuracy of data.
-- Auto_increment: automatically generate a new unique value for each new row.
-- Primary key: uniquely identifies each row in a table.
-- Not null: ensures that a column cannot have a NULL value.
-- Unique: ensures that all values in a column are different.
-- Default: sets a default value for a column when no value is specified.
-- Boolean: represents true or false values, typically stored as 1(true) and 0(false).

-- Selction in sql 

-- Selecting sepcific columns form a table 
SELECT username, email FROM users;
SELECT id, username FROM users;

-- Renaming the column names 
RENAME TABLE users TO members;
RENAME TABLE members TO users;

-- Altering in sql 
-- Adding a new column to an existing table 
ALTER TABLE users ADD COLUMN status;

-- Removing altered column from the table 
ALTER TABLE users DROP COLUMN status;

-- Modifying the data in existing column 
ALTER TABLE users MODIFY username VARCHAR(30);

-- Modifying column sequence 
ALTER TABLE users MODIFY COLUMN email VARCHAR(150) AFTER username;

-- Inserting data into table 
INSERT INTO users VALUES
(1, 'RAVEN', 'RVEN@GMAIL.COM', '2012-05-12');

-- Inserting data into specifc columns 
INSERT INTO users (username, email) VALUES
('TONY', 'TONY@STARK.COM');

-- Inserting multiple data (ID ordered 2–12)
INSERT INTO users VALUES
(2, 'RAVEN1', 'RVEN@GMAIL.COM1', '2012-05-12'),
(3, 'RAVEN2', 'RVEN@GMAIL.COM2', '2012-05-12'),
(4, 'RAVEN3', 'RVEN@GMAIL.COM3', '2012-05-12'),
(5, 'RAVEN4', 'RVEN@GMAIL.COM4', '2012-05-12'),
(6, 'RAVEN5', 'RVEN@GMAIL.COM5', '2012-05-12'),
(7, 'RAVEN6', 'RVEN@GMAIL.COM6', '2012-05-12'),
(8, 'RAVEN7', 'RVEN@GMAIL.COM7', '2012-05-12'),
(9, 'RAVEN8', 'RVEN@GMAIL.COM8', '2012-05-12'),
(10, 'RAVEN9', 'RVEN@GMAIL.COM9', '2012-05-12'),
(11, 'RAVEN10', 'RVEN@GMAIL.COM10', '2012-05-12'),
(12, 'RAVEN11', 'RVEN@GMAIL.COM11', '2012-05-12');
