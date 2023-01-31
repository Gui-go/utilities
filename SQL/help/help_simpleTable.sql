DROP TABLE IF EXISTS dbo.account

CREATE TABLE dbo.account ( 
    account_id INT NOT NULL IDENTITY(1,1) CONSTRAINT PK_account PRIMARY KEY CLUSTERED,
    account_name VARCHAR(100) NOT NULL,
    account_start_date DATE NOT NULL,
    account_address VARCHAR(1000) NOT NULL,
    account_type VARCHAR(10) NOT NULL,
    account_create_timestamp DATETIME NOT NULL,
    account_notes VARCHAR(500) NULL,
    is_active BIT NOT NULL
    );

INSERT INTO dbo.account (
    account_name, 
    account_start_date, 
    account_address, 
    account_type, 
    account_create_timestamp, 
    account_notes, 
    is_active
    )
VALUES (
    'Ed''s Account',
    '5/1/2019',
    'Ed''s Address',
    'TEST',
    GETUTCDATE(),
    'This is a test account to model this data.',
    0
    );

INSERT INTO dbo.account (
    account_name, 
    account_start_date, 
    account_address, 
    account_type, 
    account_create_timestamp, 
    is_active
    )
VALUES (
    'Guigo',
    YEAR(GETDATE())-5,
    'worderland',
    'first_one',
    GETDATE(),
    1
    );