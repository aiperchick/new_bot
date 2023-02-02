import sqlite3
from pathlib import Path


def init():
    global db, cur
    DB_NAME = 'db.sqlite3'
    MAIN_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(MAIN_PATH / DB_NAME)
    cur = db.cursor()


def create_table():
    """
    Создаем таблицу sqlite3
    """
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS cars(
        title TEXT,
        price TEXT,
        link FLOAT,
        )
        """
    )
    db.commit()


def done_cars():
    cur.execute(
        """
        SELECT * FROM  cars
        """
    )
    return cur.fetchall()


def get_cars(cars):
    """
    Заполнениние таблицы cars
    """
    cur.executemany("""INSERT INTO cars (
    name,
    price,
    link) VALUES (?, ?, ?)""", cars)
    db.commit()