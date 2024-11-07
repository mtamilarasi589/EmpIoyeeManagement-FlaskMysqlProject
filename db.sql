
create database emp;
use emp;
CREATE TABLE empdetails
(
  id VARCHAR(10) primary key,
  name VARCHAR(45) not null,
  email VARCHAR(80) not null,
  dept VARCHAR(50) not null
  );
insert into empdetails values('e001','Raj','raj@gmail.com','HR');
insert into empdetails values('e002','Sakthi','sakthi@gmail.com','Development');
insert into empdetails values('e003','Shiva','shiva@gmail.com','Testing');
select * from empdetails;

