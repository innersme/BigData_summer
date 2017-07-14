#기사 예제풀이
#database를 생성한다.
create database pnudb;

#pnudb database을 사용한다. 
use pnudb;

/*
CRUD
INSERT SELECT UPDATE DELETE 
생성 일기 갱신 삭제
*/

#pnudb에 'gisa'라는 table을 생성한다. #CREATE
create table gisa(
	# std_no 정수형, primary key형
	std_no integer primary key,		
	# email varchar형, no null
    email varchar(30) not null,
    # score 정수형, no null
    kor_score integer not null,		
    eng_score integer not null,	
	math_score integer not null,
	sci_score integer not null, 
	hist_score integer not null,
    total integer not null,			
	# code varchar(1)
    manager_code char(1) not null,	
    acc_code char(1) not null,
    loc_code char(1) not null
);

# select * 전체 다 출력
select * from gisa;

#출력:std_no와 eng_score+kor_score, eng_score+kor_score는 temp로 저장
select std_no,eng_score+kor_score as temp
#gisa table에서
from gisa
#조건: acc_code='A' or acc_code='B'
where acc_code = 'A' or acc_code = 'B'
#출력순서는 temp기준으로 내림차순, std_no기준 오름차순
order by temp desc,std_no asc
#출려제한 4등만, +사람
limit 4,1;

/*
acc_code가 A, B, C일 때, 
*/ 
select case acc_code
when 'A' then eng_core + 5
when 'B' then eng_core + 15
when 'C' then eng_core + 20
# 출력 ( case - end 까지를) and plus_score로 대입
end as plus_score 
from gisa
where total >=150;

/*
서브쿼리 사용법
*/
#갯수를 새자
select count(*)
from(
#kor_score를 acc_code에 따라 변환
select case acc_code
	when 'A' then kor_score + 10
    when 'B' then kor_score + 15
    when 'C' then kor_score + 20
end as temp
from gisa
#조건: manage_code = 'B' 
where manager_code='B') tbl #얘를 tbl로
#tbl.temp 가 50보다 큰 사람들
where tbl.temp > 50;

