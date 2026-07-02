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
	Search for names starting with M
*/

SELECT * FROM users WHERE name LIKE 'M%';