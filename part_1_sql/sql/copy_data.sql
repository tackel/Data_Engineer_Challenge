-- This sql copy data in 2017.csv file to tale_2017

COPY PUBLIC.table_2017 
FROM 'D:\2017.csv' DELIMITER ',' csv HEADER

