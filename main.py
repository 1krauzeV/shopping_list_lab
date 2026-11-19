import tkinter as tk
from tkinter import messagebox
from database import create_database, add_purchase, get_purchases, mark_purchase, delete_purchase

# Убеждаемся, что таблица в базе данных существует
create_database()

# Создаём главное окно
window = tk.Tk()
window.title("Мой список покупок")
window.geometry("520x500")

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

    # Берём покупки из базы и показываем их статус
    for purchase_id, name, quantity, is_bought in get_purchases():
        status = "КУПЛЕНО" if is_bought == 1 else "Нужно купить"
        shopping_list.insert(tk.END, f"{name} — {quantity} шт. [{status}]")


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


def mark_selected_purchase():
    # Узнаём, какую строку пользователь выбрал мышкой
    selected_indices = shopping_list.curselection()

    if not selected_indices:
        messagebox.showwarning("Не выбрана покупка", "Сначала выберите товар в списке.")
        return

    # Получаем запись с тем же порядковым номером из базы
    selected_purchase = get_purchases()[selected_indices[0]]
    purchase_id = selected_purchase[0]
    is_bought = selected_purchase[3]

    if is_bought == 1:
        messagebox.showinfo("Уже куплено", "Этот товар уже отмечен как купленный.")
        return

    # Меняем статус в базе и обновляем список на экране
    mark_purchase(purchase_id)
    refresh_list()


def delete_selected_purchase():
    # Узнаём, какую строку пользователь выбрал мышкой
    selected_indices = shopping_list.curselection()

    if not selected_indices:
        messagebox.showwarning("Не выбрана покупка", "Сначала выберите товар в списке.")
        return

    # Получаем id и название выбранной покупки
    selected_purchase = get_purchases()[selected_indices[0]]
    purchase_id = selected_purchase[0]
    product_name = selected_purchase[1]

    # Спрашиваем разрешение перед удалением
    confirmed = messagebox.askyesno(
        "Подтверждение удаления",
        f"Удалить товар «{product_name}» из списка?"
    )

    if not confirmed:
        return

    # Удаляем запись из SQLite и обновляем список
    delete_purchase(purchase_id)
    refresh_list()


add_button = tk.Button(window, text="Добавить", command=add_product)
add_button.pack(pady=10)

shopping_list = tk.Listbox(window, width=52, height=8)
shopping_list.pack(pady=10)

mark_button = tk.Button(
    window,
    text="Отметить как купленное",
    command=mark_selected_purchase
)
mark_button.pack(pady=5)

delete_button = tk.Button(
    window,
    text="Удалить выбранный товар",
    command=delete_selected_purchase
)
delete_button.pack(pady=5)

# При запуске показываем ранее сохранённые покупки
refresh_list()

window.mainloop()