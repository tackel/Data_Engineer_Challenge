from decouple import config
import psycopg2


DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST', default='localhost')
DB_PORT = config('DB_PORT', default=5433, cast=int)
DB_DATABASE = config('DB_DATABASE')


def conexion():
    """
    Function for connect database postgrest. This need .env file
    Return: connection to database
    """
    connection = psycopg2.connect(
        host=DB_HOST, database=f'{DB_DATABASE}', user=f'{DB_USER}', password=f'{DB_PASSWORD}', port=f'{DB_PORT}')
    return connection
