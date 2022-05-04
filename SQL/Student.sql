CREATE DATABASE StudentsDB;

Use StudentsDB;

CREATE TABLE Students(StudentsID int,
StudentsName varchar(255),
StudentsAge int,
Address varchar(255),
City varchar(255),
postalcode int,
Country varchar(255));

INSERT INTO Students VALUES('1','Ravi',21,'Skagen 21','Kista',4006,'Sweden')

INSERT INTO Students VALUES('2','Raju',22,'Skagen 26','Akalla',4236,'Norway')

INSERT INTO Students VALUES('3','kavya',21,'Skagen 24','sollentuna',4234,'Norway')

INSERT INTO Students VALUES('4','John',23,'Skagen 22','bromma',3456,'Norway')

INSERT INTO Students VALUES('5','Rita',23,'Skagen 22','solna',4346,'Norway')

select* from Students;

 DELETE FROM Students WHERE StudentsName='RAvi';

 INSERT INTO Students VALUES('6','Ravi',23,'Skagen 21','kista',4346,'Norway')

 SELECT StudentsName, City FROM Students;

 SELECT StudentsName  FROM Students WHERE city='kista'

select StudentsName,address,postalCode from Students Order by StudentsName desc;

SELECT * FROM Students WHERE City='kista' OR City='Bromma';

UPDATE Students SET StudentsAge =22,city='Malmo' WHERE StudentsID =4;

UPDATE Students SET StudentsAge =26,city='Goteborg' WHERE StudentsID =2;

DELETE FROM Students WHERE StudentsName= 'Ravi';

alter table students add phonenum int;


SELECT * FROM Students ORDER BY City, StudentsName;

update Students set phonenum =4567654 where StudentsID=5;

update Students set phonenum =123456 where StudentsID=2;

update Students set phonenum =5434567 where StudentsID=3;

update Students set phonenum =345678 where StudentsID=4;

delete from Students where StudentsAge=22

SELECT * FROM Students ORDER BY StudentsAge, StudentsName;

ALTER TABLE students ADD DOB DATE;








