import tkinter as tk

window = tk.Tk()
window.title("Мой список покупок")
window.geometry("520x420")

title_label = tk.Label(
    window,
    text="Мой список покупок",
    font=("Arial", 18)
)
title_label.pack(pady=20)

window.mainloop()
