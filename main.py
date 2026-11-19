import tkinter as tk
from tkinter import messagebox
from database import create_database, add_purchase, get_purchases

# Убеждаемся, что таблица в базе данных существует
create_database()

# Создаём главное окно
window = tk.Tk()
window.title("Мой список покупок")
window.geometry("520x420")

# Заголовок
title_label = tk.Label(
    window,
    text="Мой список покупок",
    font=("Arial", 18)
)
title_label.pack(pady=20)

# Поле для названия товара
product_label = tk.Label(window, text="Название товара:")
product_label.pack()
product_entry = tk.Entry(window, width=35)
product_entry.pack(pady=(0, 12))

# Поле для количества
quantity_label = tk.Label(window, text="Количество:")
quantity_label.pack()
quantity_entry = tk.Entry(window, width=35)
quantity_entry.pack(pady=(0, 12))


def refresh_list():
    # Убираем старые строки из списка на экране
    shopping_list.delete(0, tk.END)

    # Берём сохранённые покупки и показываем их в окне
    for name, quantity in get_purchases():
        shopping_list.insert(tk.END, f"{name} — {quantity} шт.")


def add_product():
    name = product_entry.get().strip()
    quantity = quantity_entry.get().strip()

    if not name or not quantity.isdigit() or int(quantity) <= 0:
        messagebox.showwarning(
            "Ошибка ввода",
            "Введите название и положительное целое количество."
        )
        return

    # Записываем товар в базу и обновляем видимый список
    add_purchase(name, int(quantity))
    refresh_list()

    # Очищаем поля после успешного добавления
    product_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)


add_button = tk.Button(window, text="Добавить", command=add_product)
add_button.pack(pady=10)

shopping_list = tk.Listbox(window, width=42, height=8)
shopping_list.pack(pady=10)

# При запуске показываем ранее сохранённые покупки
refresh_list()

window.mainloop()