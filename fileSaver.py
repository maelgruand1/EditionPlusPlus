import tkinter as tk
from tkinter import filedialog

def ouvrir_fichier(text_widget):
    """Ouvre un fichier .txt et affiche son contenu dans la zone de texte."""
    nom_fichier = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    if nom_fichier:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, f.read())

def enregistrer_fichier(text_widget):
    """Enregistre le contenu de la zone de texte dans un fichier .txt."""
    nom_fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])
    if nom_fichier:
        with open(nom_fichier, "w", encoding="utf-8") as f:
            f.write(text_widget.get("1.0", tk.END))
