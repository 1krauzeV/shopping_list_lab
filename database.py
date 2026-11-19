import sqlite3
from pathlib import Path


def create_database():
    # Файл базы данных будет рядом с database.py
    db_path = Path(__file__).with_name("purchases.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Создаём таблицу, если её ещё нет
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            is_bought INTEGER NOT NULL DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()
    print("База данных готова!")


def add_purchase(name, quantity):
    # Сохраняем новую покупку в таблицу
    db_path = Path(__file__).with_name("purchases.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO purchases (name, quantity) VALUES (?, ?)",
        (name, quantity)
    )

    connection.commit()
    connection.close()


def get_purchases():
    # Получаем все покупки из базы данных
    db_path = Path(__file__).with_name("purchases.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT name, quantity FROM purchases ORDER BY id")
    purchases = cursor.fetchall()

    connection.close()
    return purchases


if __name__ == "__main__":
    create_database()