CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    email VARCHAR(150)
);

INSERT INTO users (name, age, email)
VALUES
('Ana', 25, 'ana@email.com'),
('Carlos', 17, 'carlos@email.com'),
('Maria', 30, 'maria@email.com'),
('Pedro', 40, 'pedro@email.com');

SELECT * FROM users;

SELECT * FROM users WHERE age >= 18;

SELECT * FROM users WHERE age > 30;

SELECT name, email FROM users;

SELECT * FROM users ORDER BY age;

SELECT * FROM users ORDER BY age DESC;

SELECT name FROM users;

SELECT * FROM users WHERE age > 20;

SELECT * FROM users ORDER by name;

SELECT name, age FROM users ORDER by name;