CREATE DATABASE moviesDB;

use moviesdb;

create table directors(did int primary key,dname varchar(255),dnotes varchar(1000));

select * from directors

insert into directors values(1,'rajamouli','geujakjdqurgqjkdwjhquieqjwdqugjqwhdquiwdgjwdudjwdqudjwdqwudwdquwdjwdu')

insert into directors values(2,'trivikram','jgvrtwgsdhcuhhfsdhjqkdjghsbcalkshfdgiqowkjscalkjhjkadgyqwvsdbcbgyeiks')

insert into directors values(3,'alfred','wetgbvmksodijhfgtryeiowmsmndnhjbfjknjkfjefjefjefjfjefjefnjwefnjefejej')

insert into directors values(4,'david','ddgkejtweudbveufgwoljkfhbvncaklhfuiwefhifhweihfwolkehfiwuejkhfniewjkdhfnj')

insert into directors values(5,'johnsson','yuwdsgfcwikashdfncwuiejkashdjioweklsamdjniwekasdjiweksadjhneiwkdjiek')


create table genres(gid int primary key,gname varchar(255),gnotes varchar(1000));

select*from genres

insert into genres values(1,'action','sdtgutdtyguigtydyhgtftrtgytrthjgrfhgfdfghtryuytyttyf')

insert into genres values(2,'horror','jsfduiefjascuiqwjkdDFVYUEJDUJSHDNAJKDAklfhsldhakjhd')

insert into genres values(3,'comedy','jasfguiqweajksfncuiejkafnqiakjhsfuiewjkhdfnuweijkdhfn')

insert into genres values(4,'mystery','ajfiajfajsfuajfhnuasjkfhiwuakjsfhuiwefheuijkasfhuie')

insert into genres values(5,'thriller','ajfguicaejksfuiajkshfdnuasjkhdncejksahdncejksahdcijk')




create table categories(cid int primary key,cname varchar(255),cnotes varchar(1000));

select *from categories

insert into categories values(1,'thriller','jhfgwyjsnamdfuiasjkdbqwjkasdnjqwkasdhnqwjkdhnqwkj')

insert into categories values(2,'action','jeasfcwuiejaskhdncqwuieasjkdhniqwejkasdhniqwkjsdhiq')

insert into categories values(3,'mystery','euiasjdquiwjkashdnuiqwjkhdiqwujkdhniqwjkdhniqwhdqi')

insert into categories values(4,'horror','euijfhqweuijkshdqwuijkashdqwuijkhdiquwejkahdiqwujkasdh')

insert into categories values(5,'comedy','uieasjfhweuijkashdfnwuiqejkasdnioqwklsajdiqwklsdjiwklj')




create table movies(mid int primary key,mtitle varchar(255),mdirectorid int,mcopyrightyear int,mlength varchar(255),mgenrei1d int,mcategoryid int,mrating float,mnotes varchar(1000));
select *from movies

insert into movies values(1,'Acharya',1,2022,'2hours',1,1,3.5,'sgdwuijsdfhqwuijshfdiqwjksdiwuqjkdiwkjdhiowkhdf')

insert into movies values(2,'RRR',2,2022,'3hours',2,2,3.5,'jsfguwejfueiwjkhfuiwejkhfuiwejkfbejkfbewjkkfnwejkhd')

insert into movies values(3,'scream',3,2002,'2hours',3,3,3.5,'dfweskfjwenksdfjwieksjdiwqokjdiwqosjkdwiqoskljed')

insert into movies values(4,'bump',4,2004,'2hours',4,4,2.5,'fgreteujhfweuijkashfieowkasljdiskaldjwiqeoskldjm')

insert into movies values(5,'indra',5,2009,'3hours',5,5,3.5,'poeyfuhwjiaskhfnweuijkshfweuisjkhrfweuijdfhweuijk')


