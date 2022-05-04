use StudentDB

drop table if exists softdrink
CREATE TABLE softdrink(Drinkcode int,
DName varchar(255),
price decimal(12,2),
calories int);
select* from softdrink

insert into softdrink values(101,'Lime and Lemon',20.00,120)
insert into softdrink values(102,'Apple Drink',18.00,120)
insert into softdrink values(103,'Nature Nectar',15.00,115)
insert into softdrink values(104,'Green Mango',15.00,140)

insert into softdrink values(105,'Aaam Panna',20.00,135)
insert into softdrink values(106,'Mango Juice Bahaar',12.00,150)



select * from softdrink

--Display names and drink codes of those drinks that have more than 120 calories

select dname,drinkcode from softdrink WHERE calories>120;

--Display drink codes, names and calories of all drinks in descending order of calories.

select drinkcode,dname ,calories from softdrink order by calories desc;

--Display names and price of drinks that have price in the range 12 to 18 (both 12 and 18 included).

select dNAME,PRICE from softdrink where price between 12 and 18

--Increase the price of all drinks in the given table by 10%

update softdrink
set price=price+0.10*price;

--Insert the following values in the table (108,”orange juice”,14.00,120)

insert into softdrink values(108,'orange juice',14.00,120)

-- Delete the record whose drinkcode is 102.

DELETE FROM softdrink WHERE Drinkcode = 102;

--- Display the count of distinct price values from softdrink table.

SELECT COUNT( DISTINCT price) as Distinct_Price FROM softdrink;

select * from softdrink

update softdrink set price=16.50 where Drinkcode=103

--Select the max calories from softdrink table.

select dname,drinkcode, price, calories from softdrink where calories >120;

---Select dname from softdrink where dname contains the word mango.

select dname from softdrink where dname like '%mango%'