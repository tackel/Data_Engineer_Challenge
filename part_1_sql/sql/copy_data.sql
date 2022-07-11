-- This sql copy data in 2017.csv file to tale_2017

-- I need to read the 2017.csv file from drive d:\ because I don't have permission

copy PUBLIC.table_2017 
FROM 'D:\2017.csv' with DELIMITER ',' csv HEADER
