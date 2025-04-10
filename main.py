import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x400")

current_player = "X"
buttons = []


def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


def is_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True


def on_click(row, col):
    global current_player

    if buttons[row][col]["text"] != "":
        return

    buttons[row][col]["text"] = current_player

    if check_winner():
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        return

    if is_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        return

    current_player = "0" if current_player == "X" else "X"


def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = ""


# Создание игрового поля
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

# Кнопка сброса игры
reset_button = tk.Button(window, text="Сбросить игру", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

window.mainloop()