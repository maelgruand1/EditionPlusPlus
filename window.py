import tkinter as tk

def tkWindow(title, size):
    window = tk.Tk()
    window.title(title)
    window.geometry(size)
    return window

def tkLabel(root, text, font):
    label = tk.Label(root, text=text, font=font)
    label.pack()
    return label

def tkButton(window, text, command):
    button = tk.Button(window, text=text, command=command)
    button.pack()
    return button

