/* SOME AVANCED SQL QUERIES */

/* Inserting a few more values to populate the table */

INSERT INTO users (name, age, email)
VALUES
('Lucas', 22, 'lucas@email.com'),
('Mariana', 31, 'mariana@email.com'),
('Juliana', 27, 'juliana@email.com'),
('Rafael', 45, 'rafael@email.com');

/* 
	LIKE
	Search for users than name starting with M
*/

SELECT * FROM users WHERE name LIKE 'M%';

/* 
	LIKE
	Search for users than name ending with A
*/

SELECT * FROM users WHERE name LIKE '%a';

/* 
	LIKE
	Search for users than name that contain 'ar'
*/

SELECT * FROM users WHERE name LIKE '%ar%';

/* 
	IN
	Search for users than age eaquals at 22, 27 or 31
*/

SELECT * FROM users WHERE age IN (22, 27, 31);

/* 
	BETWEEN
	Search for users than age between 25 and 32 years
*/

SELECT * FROM users WHERE age BETWEEN 25 AND 35;

/* 
	LIMIT
	Show only the first three users
*/

SELECT * FROM users LIMIT 3;

/*
	AGGREGATION FUNCTIONS - COUNT
	number of users
*/

SELECT COUNT(*) FROM users;

/*
	AGGREGATION FUNCTIONS - AVERAGE
	age average of all users
*/

SELECT AVG(age) FROM users;

/*
	AGGREGATION FUNCTIONS - MAX
	oldest user 
*/

SELECT MAX(age) FROM users;

/*
	AGGREGATION FUNCTIONS - MIN
	undarage user
*/

SELECT MIN(age) FROM users;