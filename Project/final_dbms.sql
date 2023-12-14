create database miniproject;
show databases;
use miniproject;

CREATE TABLE USERSINFO(
    USER_NAME varchar(20) NOT NULL PRIMARY KEY,
    FIRST_NAME VARCHAR(25),
    LAST_NAME VARCHAR(25),
    MOBILE_NUMBER int,
    DOB DATE,
    GENDER TINYINT(1) NOT NULL,
    INITIAL_BAL int,
    PASSWORDS VARCHAR(255) NOT NULL
);


CREATE TABLE ACCOUNT_INFO(
    USER_NAME varchar(20) NOT NULL,
    BALANCE INT(10) NOT NULL,
    FOREIGN KEY (USER_NAME) REFERENCES USERSINFO(USER_NAME)
);

DELIMITER $$ 
CREATE TRIGGER insert_account
AFTER
INSERT ON USERSINFO FOR EACH ROW BEGIN
INSERT INTO ACCOUNT_INFO
VALUES(NEW.USER_NAME, NEW.INITIAL_BAL);
END $$ 
DELIMITER;

INSERT INTO USERSINFO (
        USER_NAME,
        FIRST_NAME,
        LAST_NAME,
        MOBILE_NUMBER,
        DOB,
        GENDER,
        INITIAL_BAL,
        PASSWORDS
    )
VALUES (
        'user1',
        'John',
        'Doe',
        1234567890,
        19900101,
        1,
        5000,
        'hashedpassword1'
    );

SELECT * FROM ACCOUNT_INFO;

SELECT * FROM USERSINFO;

CREATE TABLE EXPENSE_TRACKER(
    USER_NAME varchar(20) NOT NULL,
    DESCRIPTION_OF_EXPENSE varchar(50) NOT NULL,
    AMOUNT INT(25),
    TIME_STAMP DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (USER_NAME) REFERENCES USERSINFO(USER_NAME)
);

DELIMITER $$ 
CREATE TRIGGER update_balance
AFTER
INSERT ON expense_tracker FOR EACH ROW BEGIN
UPDATE account_info
SET BALANCE = BALANCE - NEW.AMOUNT
WHERE USER_NAME = NEW.USER_NAME;
END $$ 
DELIMITER;

INSERT INTO EXPENSE_TRACKER(USER_NAME, DESCRIPTION_OF_EXPENSE, AMOUNT)
VALUES("user1", "TEST", 100);

select * from EXPENSE_TRACKER;