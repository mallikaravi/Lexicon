CREATE DATABASE Student;
use Student

CREATE TABLE Student(Studentrollno int primary key,
StudentName varchar(255) ,
deptcode int not null,
DOB date,
Email varchar(255),
Address varchar(255));
select *from student

INSERT INTO STUDENT values (1,'Ravi',101, '1989-05-01','Ravi@gmail.com','old town 123')
INSERT INTO STUDENT values (2,'Rani',102, '1990-06-01','Rani@gmail.com','new town 456')
INSERT INTO STUDENT values (3,'Raju',103,'1989-09-01','Raju@gmail.com','old town 183')

CREATE TABLE course(ccode int primary key,
cname varchar(255),
departmentcode int not null);


insert into course values(21,'Java',101)
insert into course values(22,'python',102)
insert into course values(23,'oracle',103)

CREATE TABLE enroll(rollno int foreign key references student(studentrollno),
coursecode int foreign key references course(ccode),
semester varchar(50),
grade varchar(10), 
primary key (coursecode,semester))


select * from enroll
insert into enroll values(1,21,'first','A')
insert into enroll values(2,22,'second','A+')
insert into enroll values(3,23,'Third','B')

drop table enroll

CREATE TABLE textbook(coursecode int foreign key references course(ccode),
semester varchar(255),
book_isbn int,
primary key(coursecode,semester));

select * from textbook
insert into textbook values(21,'Fourth','123345')

insert into textbook values(22,'fifth','123346')

insert into textbook values(23,'sixth','123347')


--foreign key references textbook(book_isbn
CREATE TABLE bookdetails(book_isbn int primary key,
title varchar(255),
publisher varchar(255),
author varchar(255));

select *from bookdetails
insert into bookdetails values('123345','God of things','Tom','John')
insert into bookdetails values('123346','Beloved','Toni','Tanith')

insert into bookdetails values('123347','Temple','Margaret','Idowu')


---Add a column named price in bookdetails

ALTER TABLE bookdetails ADD price int;

---Add a check constarint

ALTER TABLE enroll  ADD CHECK (Grade IN ('O','A','A+','B','B+','RA'))

--drop column address

ALTER TABLE student DROP COLUMN Address;
---drop column using cascade

--ALTER TABLE student DROP COLUMN Address cascade

--we dont have to use cascade because it is not applicabele,as it is not having  any reference keys.

---create tables department,branch

--CONSTRAINT FK_Department FOREIGN KEY (dcode) REFERENCES student(deptcode)

CREATE TABLE Department(dcode int primary key ,
dName varchar(255),
dlocation varchar(255),
branchcode int );
select * from Department
insert into department values(101,'aba','kista',23)
insert into department values(102,'aba','kista',24)

--foreign key references department(branchcode)

CREATE TABLE branch(branchcode int  primary key,
bname varchar(255));

select * from branch

insert into branch values(23,'CSE')
insert into branch values(24,'EEE')

---difference between drop and truncate

drop table department;
truncate table branch;

---NOT null constraint 

alter table bookdetails alter column author varchar(255) not null

---adding columns to book details

ALTER TABLE bookdetails ADD  published_year int;

ALTER TABLE bookdetails ADD  Edition varchar(255);

select*from bookdetails
UPDATE bookdetails SET published_year= ''

WHERE published_year IS NULL

alter table bookdetails alter column published_year int not null

UPDATE bookdetails SET Edition= ''

WHERE Edition IS NULL

alter table bookdetails alter column edition varchar(255) not null

--Display the constraint type and constraint name

SELECT TABLE_NAME,

      CONSTRAINT_TYPE,CONSTRAINT_NAME

FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS

WHERE TABLE_NAME='student';

---Modifying datatype

ALTER TABLE course ALTER COLUMN cname char(50);

--rename the table


exec sp_rename 'branch', 'branch_details'

--rename column
EXEC sp_RENAME 'student.Dob' , 'Birthdate', 'COLUMN'

select *from branch_details

---Drop branch details with cascade option

alter table department
add constraint fk_department_branchcode
foreign key (branchcode)
references branch_details(branchcode)

select * from department
select * from branch_details

drop table branch_details

alter table department  drop constraint fk_department_branchcode

alter table department
add constraint fk_department_branchcode
foreign key (branchcode)
references branch_details(branchcode)
on delete cascade

drop table branch_details

SELECT * FROM DEPARTMENT
SELECT * FROM BRANCH_DETAILS

DELETE FROM BRANCH_DETAILS WHERE BRANCHCODE=23
SELECT * FROM DEPARTMENT

SELECT * FROM BRANCH_DETAILS

/*alter table department  drop constraint fk_department_branchcode

alter table department
add constraint fk_department_branchcode
foreign key (branchcode)
references branch_details(branchcode)
on delete set null


SELECT * FROM DEPARTMENT
SELECT * FROM BRANCH_DETAILS

DELETE FROM BRANCH_DETAILS WHERE BRANCHCODE=23
SELECT * FROM DEPARTMENT

SELECT * FROM BRANCH_DETAILS*/

