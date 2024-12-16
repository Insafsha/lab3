import tkinter as tk
from tkinter import messagebox
import string


# сдвиг вправо
def s_right(ch, s, pers):
    index = pers.index(ch)
    s_index = (index + s) % len(pers)
    return pers[s_index]


# сдвиг влево
def s_left(ch, s, pers):
    index = pers.index(ch)
    sh_index = (index - s) % len(pers)
    return pers[sh_index]


# генерация ключа
def gen_key():
    pers = string.ascii_uppercase + string.digits
    pref = pref_entry.get().strip().upper()
    print(f"Введенная вводная часть: {pref}")

    if len(pref) != 5 or not all(ch in pers for ch in pref):
        messagebox.showerror("Ошибка", "Вводная часть должна содержать ровно 5 символов (A-Z, 0-9).")
        return
    sec_block = "".join(s_right(ch, 3, pers) for ch in pref)
    t_block = "".join(s_left(ch, 5, pers) for ch in pref)
    full_key = f"{pref}-{sec_block}-{t_block}"
    print(f"Сгенерированный ключ: {full_key}")
    key_e.delete(0, tk.END)
    key_e.insert(0, full_key)


window = tk.Tk()
window.title("Генератор ключей")
window.geometry("600x400")
bg_img = tk.PhotoImage(file="game_art.png")
lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relw=1, relh=1)
fr = tk.Frame(window)
fr.place(relx=0.5, rely=0.5, anchor='center')

# Поле ввода первой части ключа
pref_label = tk.Label(fr, text="1 блок ключа (5 символов):", font=("Arial", 12), bg="white")
pref_label.grid(row=0, column=0, padx=10, pady=10)
pref_entry = tk.Entry(fr, font=("Arial", 12), width=20)
pref_entry.grid(row=0, column=1, padx=10, pady=10)

# Поле для отображения сгенерированного ключа
key_l = tk.Label(fr, text="Сгенерированный ключ:", font=("Arial", 12), bg="white")
key_l.grid(row=1, column=0, padx=10, pady=10)
key_e = tk.Entry(fr, font=("Arial", 12), width=20)
key_e.grid(row=1, column=1, padx=10, pady=10)

# Кнопка
button = tk.Button(fr, text="Генерировать ключ", font=("Arial", 12), bg="#4CAF50", fg="white", command=gen_key)
button.grid(row=2, column=0, columnspan=2, pady=20)

# Запуск основного цикла
window.mainloop()
