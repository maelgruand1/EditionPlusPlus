import window as win
import fileSaver as fs
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import font

# Fenêtre principale
root = win.tkWindow("Edition ++", "800x600")

H1_FONT = font.Font(family="Arial", size=25, weight="bold")
welcome = win.tkLabel(root, "Welcome to Edition ++", font=H1_FONT)

editor1 = None  # Variable pour la fenêtre d'édition
text_area = None  # Zone de texte

# Fonction pour ouvrir l'éditeur
def openEditor():
    global editor1, text_area
    if editor1 is None or not editor1.winfo_exists():
        editor1 = win.tkWindow("Editor", "800x600")

        # Barre de menu
        menu_bar = tk.Menu(editor1)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Ouvrir", command=lambda: fs.ouvrir_fichier(text_area))
        file_menu.add_command(label="Enregistrer", command=lambda: fs.enregistrer_fichier(text_area))
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=closeEditor)

        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        editor1.config(menu=menu_bar)

        # Zone de texte
        text_area = tk.Text(editor1, wrap="word", font=("Arial", 12))
        text_area.pack(expand=True, fill="both")

        # Bouton de fermeture
        win.tkButton(editor1, "Fermer l'éditeur", command=closeEditor)

    else:
        msg.showinfo("Information", "L'éditeur est déjà ouvert")

# Fonction pour fermer l'éditeur
def closeEditor():
    global editor1
    if editor1 and editor1.winfo_exists():
        editor1.destroy()
        editor1 = None
        msg.showinfo("Information", "Éditeur fermé")

# Bouton pour ouvrir l'éditeur
win.tkButton(root, "Ouvrir l'éditeur", command=openEditor)

root.mainloop()
