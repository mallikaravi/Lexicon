Use customersDB;
select *from Customers

select min(CustomerID) as min_val from Customers;

select count(customername)as count_of_customers from customers where Customername='Ericsson';

select avg(CustomerID) as avg from Customers

--like operator,'a_%'

select CustomerName from Customers where CustomerName like 'E%';

--wildcards 

/*     ?-represents single character
        * Zero or more characters
		-represent single character within specified range(A-Z)
		# represents single numeric character
		! represents any character that is![A-Z]*/

--In operator 
select * from Customers;

select city from Customers where city in ('malmo','stenvagen');

--between operator
SELECT * FROM Customers WHERE CustomerID BETWEEN 4 AND 5;

--NOTNULL constarint

create  table persons(pId int not null,pname varchar(255),page int not null);

insert into persons (pid,pname) values (1,'abc')

alter table persons alter column pname varchar(25) not null;

select * from persons

create table orders(OID int not null,
                  order_Item varchar(255),
				  price int,
				  constraint or_unique unique(OID,order_item));
                 

create table items(Item_id int primary key Identity(100,1),Item_name char(45),Item_count int);

insert into items(Item_name,Item_count) values('phone',10)

insert into items(Item_name,Item_count) values('iphone',10)

insert into items(Item_id,Item_name,Item_count) values(100,'iphone',10);


select * from items

alter table orders add primary key(oid);

create table student1(sid int primary key,sname varchar(255),sage int);

create table courses (cid int primary key,cname varchar(255),sid int foreign key references student1(sid));

select sname,cname from courses,student1 where student1.sid=courses.sid;

ALTER TABLE student1
ADD CONSTRAINT df_age
DEFAULT 0 FOR sage;

insert into student1 (sid,sname)values(106,'biology');

select* from student1;

use CustomersDB;

create table supplier(sid int primary key,
sname varchar(255),)

create table orders1(oid int primary key,
sid int foreign key references supplier(sid),
o_date date);

select supplier.sid,sname,orders1.o_date
From supplier inner join orders1
on supplier.sid=orders1.sid;

select * from orders1;

select supplier.sid,sname,orders1.o_date
From supplier left outer join orders1
on supplier.sid=orders1.sid;


select supplier.sid,sname,orders1.o_date
From supplier right outer join orders1
on supplier.sid=orders1.sid;


select supplier.sid,sname,orders1.o_date
From supplier full outer join orders1
on supplier.sid=orders1.sid;

--stored procedures

create procedure basic_procedure
As
select * from supplier;
select * from orders1;

Exec basic_procedure;

---view

create table country(cid int,cname varchar(255),ccode int);

select*from country;

create view[country_sweden] As
select cname,ccode
from country
where cname='sweden';

select *from [country_sweden];