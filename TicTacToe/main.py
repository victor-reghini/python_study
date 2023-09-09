import tkinter as tk
import ttkbootstrap as ttk

player_x_turn = True
game_values = ['', '', '', '', '', '', '', '', '']
winner = ''


def check_winner():
    win_cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    x_indexes = []
    o_indexes = []
    x_wins = [False, False, False]
    o_wins = [False, False, False]
    global game_values
    global winner
    for i in range(0, 9):
        if game_values[i] == 'X':
            x_indexes.append(i)
        if game_values[i] == 'O':
            o_indexes.append(i)
    for i in range(0, 8):
        for j in range(0, 3):
            x_wins[j] = bool(win_cases[i][j] in x_indexes)
            o_wins[j] = bool(win_cases[i][j] in o_indexes)
        if x_wins[0] and x_wins[1] and x_wins[2]:
            title_var.set('Player X wins')
            winner = 'X'
            break
        if o_wins[0] and o_wins[1] and o_wins[2]:
            title_var.set('Player O wins')
            winner = 'O'
            break


def handle_play(index):
    if buttons_vars[index].get() in ['X', 'O']:
        return
    global winner
    if winner in ['X', 'O']:
        return
    global player_x_turn
    if player_x_turn:
        buttons_vars[index].set(str('X'))
        game_values[index] = 'X'
        player_x_turn = False
        title_var.set('Player O Turn')
    else:
        buttons_vars[index].set(str('O'))
        game_values[index] = 'O'
        player_x_turn = True
        title_var.set('Player X Turn')
    check_winner()


# window
window = ttk.Window(themename='journal')
window.title('Tic Tac Toe')
window.geometry('400x400')

# label
title_var = tk.StringVar()
title_var.set('Player X Turn')
title_label = ttk.Label(master=window, textvariable=title_var, font='Arial 24 bold')
title_label.pack()

# buttons
buttons_vars = [tk.StringVar(), tk.StringVar(), tk.StringVar(),
                tk.StringVar(), tk.StringVar(), tk.StringVar(),
                tk.StringVar(), tk.StringVar(), tk.StringVar()]

font = "Helvetica 40 bold"

row_1 = ttk.Frame(master=window)
(tk.Button(master=row_1, textvariable=buttons_vars[0], command=lambda: handle_play(0),
           font=font, width=3).pack(side='left'))
(tk.Button(master=row_1, textvariable=buttons_vars[1], command=lambda: handle_play(1),
           font=font, width=3).pack(side='left', padx=10))
(tk.Button(master=row_1, textvariable=buttons_vars[2], command=lambda: handle_play(2),
           font=font, width=3).pack(side='left'))
row_1.pack()
row_2 = ttk.Frame(master=window)
(tk.Button(master=row_2, textvariable=buttons_vars[3], command=lambda: handle_play(3),
           font=font, width=3).pack(side='left'))
(tk.Button(master=row_2, textvariable=buttons_vars[4], command=lambda: handle_play(4),
           font=font, width=3).pack(side='left', padx=10))
(tk.Button(master=row_2, textvariable=buttons_vars[5], command=lambda: handle_play(5),
           font=font, width=3).pack(side='left'))
row_2.pack(pady=10)
row_3 = ttk.Frame(master=window)
(tk.Button(master=row_3, textvariable=buttons_vars[6], command=lambda: handle_play(6),
           font=font, width=3).pack(side='left'))
(tk.Button(master=row_3, textvariable=buttons_vars[7], command=lambda: handle_play(7),
           font=font, width=3).pack(side='left', padx=10))
(tk.Button(master=row_3, textvariable=buttons_vars[8], command=lambda: handle_play(8),
           font=font, width=3).pack(side='left'))
row_3.pack()

# run
window.mainloop()
