import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


def convert():
    value = entry_int.get()
    converted_value = 60 / value
    output_string.set(str(converted_value))


# window
window = ttk.Window(themename='journal')
window.title('Conveter Pace')
window.geometry('650x150')

# title
title_label = ttk.Label(master=window, text='Converter Km/h para min/Km(pace)', font='Arial 24 bold')
title_label.pack(pady=10)

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Converter', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack()

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='6', font='Arial 24 bold', textvariable=output_string)
output_label.pack(pady=10)

# run
window.mainloop()