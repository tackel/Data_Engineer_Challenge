from extrac_data import extrac_data
from part_1_sql.create_table import create_table
from part_1_sql.save_data import copy_data
from part_1_sql.task import task
from psycopg2 import errors
from part_2_python.part_2_tasks import task_part_2


def part_1():
    """ 
        Run all functions for part 1 of the challege
        Create all tables for the database.
        Copy data table_2017.
        Then run the 3 tasks of part 1.
    """
    try:

        create_table(1)
        create_table(2)
        create_table(3)
        create_table(4)
        try:
            copy_data()
            print('Data copied in table_2017')
        except errors.UniqueViolation:
            print('The data already exists in the table_2017')
        print('Part 1:')
        print('')
        print('Which are the top 3 exchange with the most transactions in the file?')
        task(1)
        print('')
        print('In August 2017, which 2 companyNames had the highest combined valueEUR?')
        task(2)
        print('')
        print('For 2017, only considering transactions with tradeSignificance 3, what is the percentage of transactions per month?')
        task(3)
        print('')
        print('End of application part 1')
        print('')
    except EOFError as e:
        print(f'Error in the process {e}')


def part_2():
    """
        Run functions for part 2 of the challege 
    """
    try:
        print('Part 2')
        print('')
        task_part_2()
        print('End of application part 2')
    except EOFError as e:
        print('Error', e)


if __name__ == '__main__':
    print('Start of application')
    extrac_data()
    part_1()
    part_2()
