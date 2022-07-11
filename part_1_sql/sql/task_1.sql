-- sql to solve task 1 

select exchange, count(*)
from table_2017
group by exchange
order by count desc
limit 3;