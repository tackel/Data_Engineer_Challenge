-- sql to solve task 2

select companyname, valueeur from table_2017
where inputdate between '20170801' and '20170831'
order by valueeur desc
limit 2