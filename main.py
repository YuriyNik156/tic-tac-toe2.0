# Импортирование модуля tkinter
import tkinter as tk
from tkinter import messagebox

# Создание главного окна для игры крестики-нолики
window = tk.Tk()
window.title("Крестики-нолики. Игра до 3-х побед.")
window.geometry("460x540")
window.configure(bg="#f0f0f0")

# Инициализация переменных
current_player = "X"
player_choice = None
buttons = []
status_label = None
score_x = 0
score_o = 0
score_label = None

# Создание подсчета очков каждого игрока и условие победы до 3-х очков
def update_score(winner):
    global score_x, score_o
    if winner == "X":
        score_x += 1
    elif winner == "0":
        score_o += 1

    score_label.config(text=f"Счёт — X: {score_x} | 0: {score_o}")

    if score_x == 3 or score_o == 3:
        end_game(winner)

# Создание окончания игры после 3-х побед и возможность начать новую игру
def end_game(winner):
    status_label.config(text=f"Игрок {winner} одержал 3 победы и выиграл игру!")
    disable_all_buttons()
    reset_button.pack_forget()
    new_game_button.pack(pady=10)

# Условия, при которых игроки получают очки
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            highlight_buttons([(i, 0), (i, 1), (i, 2)])
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            highlight_buttons([(0, i), (1, i), (2, i)])
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        highlight_buttons([(0, 0), (1, 1), (2, 2)])
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        highlight_buttons([(0, 2), (1, 1), (2, 0)])
        return True

    return False

# Условия ничьи
def is_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

# Основная логика игры. Заполнение полей Х и 0
def on_click(row, col):
    global current_player

    if buttons[row][col]["text"] != "":
        return

    buttons[row][col]["text"] = current_player
    buttons[row][col]["fg"] = "#2c3e50" if current_player == "X" else "#c0392b"

    if check_winner():
        status_label.config(text=f"Игрок {current_player} победил!")
        update_score(current_player)
        disable_all_buttons()
        return

    if is_draw():
        status_label.config(text="Ничья!")
        return

    current_player = "0" if current_player == "X" else "X"
    status_label.config(text=f"Ход игрока: {current_player}")

# Подсвечиваем зеленым цветом кнопки, по которым прошла выигрышная линия
def highlight_buttons(coords):
    for r, c in coords:
        buttons[r][c].config(bg="#7bed9f")

# Отключаем кнопки после окончания раунда
def disable_all_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")

# Добавление возможности сброса текущей игры
def reset_game():
    global current_player
    current_player = player_choice
    for row in buttons:
        for btn in row:
            btn.config(text="", state="normal", bg="white")
    status_label.config(text=f"Ход игрока: {current_player}")

# Сброс текущего счета у обоих игроков
def new_game():
    global score_x, score_o
    score_x = 0
    score_o = 0
    score_label.config(text=f"Счёт — X: {score_x} | 0: {score_o}")
    new_game_button.pack_forget()
    reset_button.pack(pady=15)
    reset_game()

# Запуск игры после выбора символа Х или 0 игроком
def start_game(choice):
    global current_player, player_choice
    player_choice = choice
    current_player = choice
    start_frame.pack_forget()
    game_frame.pack()
    status_label.config(text=f"Ход игрока: {current_player}")
    score_label.config(text=f"Счёт — X: {score_x} | 0: {score_o}")


# Выбор символа перед игрой
start_frame = tk.Frame(window, bg="#f0f0f0")
tk.Label(start_frame, text="Выберите, чем играть:", font=("Arial", 16), bg="#f0f0f0").pack(pady=10)

choose_x_btn = tk.Button(start_frame, text="Играть за X", font=("Arial", 14), width=15,
                         bg="#55efc4", fg="black", command=lambda: start_game("X"))
choose_x_btn.pack(pady=5)

choose_o_btn = tk.Button(start_frame, text="Играть за 0", font=("Arial", 14), width=15,
                         bg="#81ecec", fg="black", command=lambda: start_game("0"))
choose_o_btn.pack(pady=5)

start_frame.pack(pady=100)

# Основной фрейм игры
game_frame = tk.Frame(window, bg="#f0f0f0")

score_label = tk.Label(game_frame, text="", font=("Arial", 14), bg="#f0f0f0", fg="#2d3436")
score_label.pack(pady=5)

status_label = tk.Label(game_frame, text="", font=("Arial", 16), bg="#f0f0f0", fg="#34495e")
status_label.pack(pady=10)

board_frame = tk.Frame(game_frame, bg="#f0f0f0")
board_frame.pack()

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(board_frame, text="", font=("Arial", 24, "bold"), width=5, height=2,
                        bg="white", fg="#2c3e50",
                        activebackground="#dff9fb",
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

reset_button = tk.Button(game_frame, text="Сбросить раунд", font=("Arial", 14), bg="#74b9ff", fg="white",
                         activebackground="#0984e3", command=reset_game)
reset_button.pack(pady=15)

new_game_button = tk.Button(game_frame, text="Новая игра", font=("Arial", 14), bg="#00b894", fg="white",
                            activebackground="#00cec9", command=new_game)

new_game_button.pack_forget()

window.mainloop()