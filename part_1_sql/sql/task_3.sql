-- sql to solve task 3

select to_char(inputdate::text::date, 'mm/yy') as monthyear, 
round(count(*) * 100.0 / (select count(*) from table_2017 where tradesignificance = 3),2) as percent
from table_2017
where tradesignificance = 3
group by monthyear
order by monthyear asc