CREATE TABLE table2(
    user_id            INTEGER,
    username           TEXT,
    encrypted_password TEXT,
    email              TEXT,
    salary             INT,
    date_joined        DATE
);

INSERT INTO table2
    (user_id, username, encrypted_password, email, salary, date_joined)
VALUES
    ('1', 'Guigo', 'asdasdadsdasd', 'guilhermeviegas1993@gmail.com', 3000, '2020-07-30');

SELECT * FROM table2;

INSERT INTO table2
    (user_id, username, encrypted_password, email, salary, date_joined)
VALUES
    ('2', 'Guigo', 'asdasdadsdasd', 'guilhermeviegas1993@gmail.com', 3000, '2020-07-30'),
    ('3', 'Go', 'asdasdasdasfd', 'gogo@gmail.com', 8000, '2012-02-20'),
    ('4', 'Julia', 'dsadadadasdad', 'julia@gmail.com', 2000, '2019-01-23'),
    ('5', 'Simone', 'qweqasdqwqwdq', 'moni@gmail.com', 1500, '2016-04-12'),
    ('6', 'Lol', 'qwdqsdqwdqwdq', 'lol@gmail.com', 313000, '2013-07-12');

UPDATE table2
SET username = 'Guilherme'
WHERE user_id = 2;

UPDATE table2
SET 
    username = 'Guilhermeee',
    encrypted_password = '12345'
WHERE user_id = 2;

UPDATE table2
SET 
    username = 'Guigomon',
    encrypted_password = '5432'
WHERE user_id IN (1, 2, 3);

SELECT *
FROM table2
ORDER BY user_id;

UPDATE table2
SET salary = 1.1*salary;

SELECT *
FROM table2
ORDER BY user_id;

SELECT SUM(salary)
FROM table2;