import tkinter as tk
import window as win
from tkinter import font
from editor import Editor  # Importation de la classe Editor

# Fenêtre principale
root = win.tkWindow("Edition ++", "800x600")
root.config(bg="#f0f0f0")  # Fond de la fenêtre principale

H1_FONT = font.Font(family="Arial", size=25, weight="bold")

# Texte d'accueil
welcome = win.tkLabel(root, "Welcome to Edition ++", font=H1_FONT, bg="#f0f0f0")
welcome.pack(pady=20)

# Création de l'éditeur
editor = Editor(root)

# Bouton pour ouvrir l'éditeur
openEditor_btn = win.tkButton(root, "Ouvrir l'éditeur", command=editor.toggleEditor)
openEditor_btn.pack(pady=20)

root.mainloop()
