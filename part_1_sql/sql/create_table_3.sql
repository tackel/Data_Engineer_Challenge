-- This sql create table_task_2 table for the task number 2 of part 1.

CREATE TABLE IF NOT EXISTS table_task_2(
    id SERIAL PRIMARY KEY,
    companyname VARCHAR(250) UNIQUE,
    valueeur DECIMAL
)