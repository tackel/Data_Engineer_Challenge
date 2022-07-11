from setting import conexion
import psycopg2


def create_table(table):
    """
    Function for create the necessary tables by reading sql files.
    Input: Number to complete path and read sql file
    """
    con = conexion()
    cursor = con.cursor()
    with open(f'part_1_sql/sql/create_table_{table}.sql', 'r', encoding='utf-8') as table:
        data = table.read()
        cursor.execute(data)
        con.commit()
        con.close()
