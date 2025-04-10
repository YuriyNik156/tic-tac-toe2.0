import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("380x440")
window.configure(bg="#f0f0f0")

current_player = "X"
buttons = []
status_label = None


def check_winner():
    # Проверка строк и столбцов
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            highlight_buttons([(i, 0), (i, 1), (i, 2)])
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            highlight_buttons([(0, i), (1, i), (2, i)])
            return True

    # Проверка диагоналей
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        highlight_buttons([(0, 0), (1, 1), (2, 2)])
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        highlight_buttons([(0, 2), (1, 1), (2, 0)])
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
    buttons[row][col]["fg"] = "#2c3e50" if current_player == "X" else "#c0392b"

    if check_winner():
        status_label.config(text=f"Игрок {current_player} победил!")
        disable_all_buttons()
        return

    if is_draw():
        status_label.config(text="Ничья!")
        return

    current_player = "0" if current_player == "X" else "X"
    status_label.config(text=f"Ход игрока: {current_player}")


def highlight_buttons(coords):
    for r, c in coords:
        buttons[r][c].config(bg="#7bed9f")


def disable_all_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")


def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn.config(text="", state="normal", bg="white")
    status_label.config(text="Ход игрока: X")


# Статус игры
status_label = tk.Label(window, text="Ход игрока: X", font=("Arial", 16), bg="#f0f0f0", fg="#34495e")
status_label.pack(pady=10)

# Игровое поле
frame = tk.Frame(window, bg="#f0f0f0")
frame.pack()

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(frame, text="", font=("Arial", 24, "bold"), width=5, height=2,
                        bg="white", fg="#2c3e50",
                        activebackground="#dff9fb",
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Кнопка сброса
reset_button = tk.Button(window, text="Сбросить игру", font=("Arial", 14), bg="#74b9ff", fg="white",
                         activebackground="#0984e3", command=reset_game)
reset_button.pack(pady=15)

window.mainloop()