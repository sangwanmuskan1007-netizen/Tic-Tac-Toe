from tkinter import *
from tkinter import messagebox
import math

root = Tk()
root.title("Tic Tac Toe - AI")

board = [""] * 9
buttons = []

# Check winner
def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check draw
def is_draw():
    return "" not in board

# Minimax Algorithm
def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(False)
                board[i] = ""
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(True)
                board[i] = ""
                best_score = min(score, best_score)

        return best_score

# AI Move
def ai_move():

    best_score = -math.inf
    best_move = -1

    for i in range(9):

        if board[i] == "":
            board[i] = "O"

            score = minimax(False)

            board[i] = ""

            if score > best_score:
                best_score = score
                best_move = i

    if best_move != -1:
        board[best_move] = "O"
        buttons[best_move].config(text="O")

    if check_winner("O"):
        messagebox.showinfo("Result", "AI Wins!")
        reset_game()
        return

    if is_draw():
        messagebox.showinfo("Result", "Match Draw!")
        reset_game()

# Human Move
def player_move(index):

    if board[index] != "":
        return

    board[index] = "X"
    buttons[index].config(text="X")

    if check_winner("X"):
        messagebox.showinfo("Result", "You Win!")
        reset_game()
        return

    if is_draw():
        messagebox.showinfo("Result", "Match Draw!")
        reset_game()
        return

    root.after(300, ai_move)

# Reset Board
def reset_game():

    global board

    board = [""] * 9

    for btn in buttons:
        btn.config(text="")

# Create Buttons
for i in range(9):

    btn = Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: player_move(i)
    )

    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()