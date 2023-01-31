CREATE PROC GeneralQuery @TableName NVARCHAR(100)
AS
DECLARE @SQL NVARCHAR(1000)
SET @SQL = 'SELECT * FROM ' + @TableName
EXEC (@SQL)
GO 

EXEC GeneralQuery 'mydataset.mytable'
EXEC GeneralQuery 'stagedataset.factSales'
