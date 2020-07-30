CREATE TABLE table1(
    column1 TEXT,
    nome    TEXT,
    age     INT,
    address CHAR(50),
    salary  REAL
);

INSERT INTO table1
    (column1, nome, age, address, salary)
VALUES
    ('value1', 'Guigo', 28, 'Res. Athenas, Carvoeira', 3000);

SELECT * FROM table1;