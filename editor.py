import tkinter as tk
from tkinter import messagebox as msg
import fileSaver as fs

class Editor:
    def __init__(self, root):
        self.root = root
        self.editor_frame = None  # Frame qui contiendra l'éditeur
        self.text_area = None  # Zone de texte

    def toggleEditor(self):
        """Afficher ou masquer l'éditeur dans la même fenêtre"""
        if self.editor_frame is None:
            self.editor_frame = tk.Frame(self.root, bg="#ffffff")
            self.editor_frame.pack(expand=True, fill="both", padx=10, pady=10)

            # Zone de texte
            self.text_area = tk.Text(self.editor_frame, wrap="word", font=("Arial", 12), bd=2, relief="solid")
            self.text_area.pack(expand=True, fill="both", padx=5, pady=5)

            # Barre de menu
            menu_bar = tk.Menu(self.root)
            file_menu = tk.Menu(menu_bar, tearoff=0)
            file_menu.add_command(label="Ouvrir", command=lambda: fs.ouvrir_fichier(self.text_area))
            file_menu.add_command(label="Enregistrer", command=lambda: fs.enregistrer_fichier(self.text_area))
            file_menu.add_separator()
            file_menu.add_command(label="Quitter", command=self.closeEditor)

            menu_bar.add_cascade(label="Fichier", menu=file_menu)
            self.root.config(menu=menu_bar)

            # Bouton de fermeture
            close_btn = tk.Button(self.editor_frame, text="Fermer l'éditeur", command=self.closeEditor, font=("Arial", 12), bg="#d9534f", fg="white", relief="raised", bd=3)
            close_btn.pack(pady=10)

        else:
            # Si l'éditeur est déjà ouvert, on le masque
            self.editor_frame.pack_forget()
            self.editor_frame = None
            self.text_area = None
            msg.showinfo("Information", "Éditeur fermé")

    def closeEditor(self):
        """Fermer l'éditeur et masquer la zone de texte"""
        if self.editor_frame:
            self.editor_frame.pack_forget()
            self.editor_frame = None
            self.text_area = None
            msg.showinfo("Information", "Éditeur fermé")
