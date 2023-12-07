from faker import Faker
import random
import psycopg2
from contextlib import contextmanager

@contextmanager
def create_connection():
    try:
        conn = psycopg2.connect(host="localhost", database="m6", user="SQLite", password="123456")
        yield conn
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to create database connection {err}")
    finally:
        if conn:
            conn.close()