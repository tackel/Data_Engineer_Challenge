from setting import conexion


def task(task):
    """
    Function to read and execute sql to resolve task of part 1.
    Inserts the answers of the tasks in the databese 
    Input: Number to complete path and read sql file
    """
    con = conexion()
    cursor = con.cursor()
    try:
        with open(f'part_1_sql/sql/task_{task}.sql', 'r', encoding='utf-8') as table:
            data = table.read()
            cursor.execute(data)
            res = cursor.fetchall()
            for i in res:
                if task == 1:
                    print(f'-- Exchange: {i[0]} with {i[1]} transactions')
                    cursor.execute(
                        f"INSERT INTO table_task_1(exchange,transaction) VALUES('{i[0]}',{i[1]})"
                        "ON CONFLICT (exchange) DO UPDATE SET transaction = EXCLUDED.transaction;"
                    )
                    con.commit()

                elif task == 2:
                    print(f'-- Company: {i[0]} with {i[1]} valueEUR')
                    cursor.execute(
                        f"INSERT INTO table_task_2(companyname,valueeur) VALUES('{i[0]}',{i[1]})"
                        "ON CONFLICT (companyname) DO UPDATE SET valueeur = EXCLUDED.valueeur"
                    )
                    con.commit()
                elif task == 3:
                    print(f'-- Month: {i[0]} = {i[1]} % ')
                    cursor.execute(
                        f"INSERT INTO table_task_3(monthyear, percent) VALUES('{i[0]}',{i[1]})"
                        "ON CONFLICT (monthyear) DO UPDATE SET percent = EXCLUDED.percent"
                    )
                    con.commit()
        con.close()
    except EOFError as e:
        print('error', e)
