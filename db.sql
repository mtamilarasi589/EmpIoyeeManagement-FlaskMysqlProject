create database emp;
use emp;
CREATE TABLE empdetails
(
	id VARCHAR(10) primary key,
   name VARCHAR(45) not null,
  email VARCHAR(30) not null,
  phone int(10) not null
  );
insert into empdetails values('e001','Raj','raj@gmail.com',9750037022);
insert into empdetails values('e002','Sakthi','sakthi@gmail.com',9712345678);
insert into empdetails values('e003','Shiva','shiva@gmail.com',9678945611);
select * from empdetails;
