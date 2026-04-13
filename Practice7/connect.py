import psycopg2
from config import params

def get_connection():
    try:
        conn = psycopg2.connect(**params)
        return conn

    except Exception as error:
        print(f"Connection error: {error}")
        return None