create database gradesystem;
use gradesystem;

create table student
(
 sid int(10),
 sname char(10),
 gender char(10)
);
create table course
(
 cid int(10);
 cname char(10)
);
create table mark
(
 mid int(10);
 sid int(10);
 cid int(10);
 score int(10)
);

insert into student
(1,"Tom","male");
insert into student
(2,"Jack","male");
insert into student
(3,"Rose","female");

insert into course
(1,"math");
insert into course
(2,"physics");
insert into course
(3,"chemistry");

insert into mark
(1,1,1,80);
insert into mark
(2,2,1,85);
insert into mark
(3,3,1,90);
insert into mark
(4,1,2,60);
insert into mark
(5,2,2,90);
insert into mark
(6,3,2,75);
insert into mark
(7,1,3,95);
insert into mark
(8,2,3,75);
insert into mark
(9,3,3,85);
