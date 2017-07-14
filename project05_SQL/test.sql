create database pnudb;

use pnudb;

#test table을 만들어
CREATE table test(
	id varchar(20) not null,
    pw varchar(8) not null,
    user_name varchar(30) not null
);

#test에 대한 설명보기
desc test;

#insert 
insert into test(id,pw,user_name) values ('user1','1234','choi');

#delete id='user2'의 자료
delete from test 
where id = 'user2';

#update id = 'admin'의 pw를 '2345'로 set하라.
update test set pw='2345'
where id = 'admin';