USE CustomersDB;
GO

DROP TABLE IF EXISTS States;
DROP TABLE  IF EXISTS Countries;

CREATE TABLE Countries
 
(CountryID INT PRIMARY KEY,
CountryName VARCHAR(50),
CountryCode VARCHAR(3))
 

CREATE TABLE States
 
(StateID INT PRIMARY KEY,
StateName VARCHAR(50),
StateCode VARCHAR(3),
CountryID INT)

ALTER TABLE States  WITH CHECK ADD  CONSTRAINT FK_States_Countries FOREIGN KEY(CountryID)
REFERENCES Countries (CountryID)
ON DELETE CASCADE
ON UPDATE CASCADE
GO

ALTER TABLE States CHECK CONSTRAINT FK_States_Countries
GO

INSERT INTO Countries VALUES (1,'United States','USA')
 
INSERT INTO Countries VALUES (2,'United Kingdom','UK')
 
INSERT INTO States VALUES (1,'Texas','TX',1)
INSERT INTO States VALUES (2,'Arizona','AZ',1)

SELECT TOP (1000) [CountryID]
      ,[CountryName]
      ,[CountryCode]
  FROM [CustomersDB].[dbo].[Countries]

  /****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [StateID]
      ,[StateName]
      ,[StateCode]
      ,[CountryID]
  FROM [CustomersDB].[dbo].[States]


--DELETE FROM States WHERE CountryID=1

UPDATE Countries SET CountryID =3 where CountryID=1

DELETE FROM Countries WHERE CountryID=1
