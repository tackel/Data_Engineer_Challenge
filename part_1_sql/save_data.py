import pandas as pd
from setting import conexion

# Por motivo de permisos puse el archivo 2017.csv en D:/


def copy_data():
    """
        Function to read and execute sql for copy data of 2017.csv file 
        to tabla_2017 in database
    """
    con = conexion()
    cursor = con.cursor()
    with open('part_1_sql/sql/copy_data.sql', 'r', encoding='utf-8') as table:
        data = table.read()
        cursor.execute(data)
        con.commit()
