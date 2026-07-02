/* 
	SOME UTILS QUERIES 
*/

/* Create table users */

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    email VARCHAR(150)
);

/* Insert into table some values */

INSERT INTO users (name, age, email)
VALUES
('Ana', 25, 'ana@email.com'),
('Carlos', 17, 'carlos@email.com'),
('Maria', 30, 'maria@email.com'),
('Pedro', 40, 'pedro@email.com');

/* Show all values in the table */

SELECT * FROM users;

/* show users aged 18 or older  */

SELECT * FROM users WHERE age >= 18;

/* Show users older than 30 years of age  */

SELECT * FROM users WHERE age > 30;

/* Show name and email of users  */

SELECT name, email FROM users;

/* Show all users order by age  */

SELECT * FROM users ORDER BY age;

/* Show all users sorted by age in descending order. */

SELECT * FROM users ORDER BY age DESC;

/* Update age and email of Maria */

UPDATE users SET age=28, email='maria.nova@email.com' WHERE name='Maria'

/* Show all users names */

SELECT name FROM users;

/* Exclude user Carlos */

DELETE FROM users WHERE name='Carlos'

/* Exclude all users from table -- ATENTION !!! */

DELETE FROM users;

/* Show all users with age equal 28 years */

SELECT * FROM users WHERE age = 28;

/* Show all users over 25 and under 35 years of age. */

SELECT * FROM users WHERE age > 25 AND age < 35;

/* Show all users over 25 or under 35 years of age. */

SELECT * FROM users WHERE age > 25 OR age < 35;
