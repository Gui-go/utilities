DROP TABLE MyTable;
CREATE TABLE MyTable (MyValue int);
INSERT INTO MyTable VALUES (1);
WHILE (SELECT MyValue FROM MyTable) < 5
BEGIN
	UPDATE MyTable SET MyValue = MyValue + 1;
END;
SELECT MyValue AS Result FROM MyTable;