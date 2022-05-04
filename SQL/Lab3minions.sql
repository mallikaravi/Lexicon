CREATE DATABASE minionsDB;

use minionsdb;

--create tables
create table minions(minid int primary key,minname varchar(255),minage int)

create table towns(tid int primary key,tname varchar(255))

ALTER TABLE minions ADD tid int; 

ALTER TABLE minions ADD FOREIGN KEY (tid) REFERENCES towns(tid);