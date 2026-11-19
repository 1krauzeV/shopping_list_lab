import sqlite3
from pathlib import Path


def create_database():
    # Файл базы данных находится рядом с database.py
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
    # Получаем покупки вместе с их номером и статусом
    db_path = Path(__file__).with_name("purchases.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, quantity, is_bought FROM purchases ORDER BY id"
    )
    purchases = cursor.fetchall()

    connection.close()
    return purchases


def mark_purchase(purchase_id):
    # Отмечаем выбранную покупку как купленную
    db_path = Path(__file__).with_name("purchases.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE purchases SET is_bought = 1 WHERE id = ?",
        (purchase_id,)
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
