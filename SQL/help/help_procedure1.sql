

DROP TABLE Students
DROP PROCEDURE AddStudent

CREATE TABLE Students(
	StudentID INT IDENTITY(1,1),
	StudentName VARCHAR(25),
	StudentAge INT
);

CREATE PROCEDURE AddStudent(
	@StudentName_input varchar(50),
	@StudentAge_input int,
	@StudentID_output int output
) AS
BEGIN
SET NOCOUNT ON
INSERT INTO Students (StudentName, StudentAge) VALUES (@StudentName_input, @StudentAge_input)
SELECT @StudentID_output=SCOPE_IDENTITY()
END

declare @StudentID_var INT
EXEC AddStudent 'David', 21, @StudentID_var OUTPUT
EXEC AddStudent 'Guigo', 29, @StudentID_var OUTPUT
SELECT @StudentID_var

SELECT * FROM Students