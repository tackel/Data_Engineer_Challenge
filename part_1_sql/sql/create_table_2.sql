-- This sql create table_task_1 table for the task number 1 of part 1.

CREATE TABLE IF NOT EXISTS table_task_1(
    id SERIAL PRIMARY KEY,
    exchange VARCHAR(250) UNIQUE,
    transaction INTEGER
    )