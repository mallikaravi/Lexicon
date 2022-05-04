CREATE DATABASE CustomersDB;

Use CustomersDB;

CREATE TABLE Customers(CustomerID int,
CustomerName varchar(255),
ContactName varchar(255),
Address varchar(255),
City varchar(255),
postalcode int,
Country varchar(255));

Create table products(PID int,ProductName varchar(50),ProductPrice int);

INSERT INTO Customers VALUES('1','cardinal','Tom B.Erichesen','Skagen 21','Stavangen',4006,'Norway')

INSERT INTO Customers VALUES('2','abc','Tom B.Erichesen','Skagen 21','Stavangen',4006,'Sweden')

INSERT INTO Customers VALUES('3','johnas','Tom B.Erichesen','Skagen 21','stenvagen',4546,'Norway')

INSERT INTO Customers VALUES('4','Ericsson','Wilson','Skagen 21','stenvagen',4536,'India')

select * from Customers

select CustomerName,Address from Customers;

select customerName from Customers where CustomerName='abc';

select customerName,address,postalCode from Customers Order by customerName desc;


UPDATE Customers SET contactName ='Richard',city='Malmo' WHERE CustomerID =1;


DELETE FROM customers WHERE ContactName='Tom B.Erichesen';

alter table customers add phonenum int;

INSERT INTO Customers VALUES('5','Ericsson','Wilson','Skagen 21','stenvagen',4536,'India',23456)

update Customers set phonenum =4567654 where CustomerID=1;

alter table Customers alter column postalcode varchar(255);

delete from Customers where CustomerID=3

select * from products

INSERT INTO products values(1,'iphone',30000)
delete from products;
drop table products
