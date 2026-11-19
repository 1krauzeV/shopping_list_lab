
import tkinter as tk

# Создаём главное окно программы
window = tk.Tk()
window.title("Мой список покупок")
window.geometry("520x420")

# Создаём заголовок
title_label = tk.Label(
    window,
    text="Мой список покупок",
    font=("Arial", 18)
)
title_label.pack(pady=20)

# Надпись для названия товара
product_label = tk.Label(window, text="Название товара:")
product_label.pack()

# Поле, в которое вводим название товара
product_entry = tk.Entry(window, width=35)
product_entry.pack(pady=(0, 12))

# Надпись для количества
quantity_label = tk.Label(window, text="Количество:")
quantity_label.pack()

# Поле для ввода количества
quantity_entry = tk.Entry(window, width=35)
quantity_entry.pack(pady=(0, 12))

# Создаём кнопку
add_button = tk.Button(window, text="Добавить")
add_button.pack(pady=10)

# Запускаем окно
window.mainloop()
