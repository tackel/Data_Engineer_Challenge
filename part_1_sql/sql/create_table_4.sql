-- This sql create table_task_3 table for the task number 3 of part 1.

CREATE TABLE IF NOT EXISTS table_task_3(
    id SERIAL PRIMARY KEY,
    monthyear VARCHAR(40) UNIQUE,
    percent DECIMAL
)