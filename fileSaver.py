import tkinter as tk
from tkinter import filedialog

def ouvrir_fichier(text_area):
    """Ouvre un fichier en UTF-8 et l'affiche dans la zone de texte"""
    nom_fichier = filedialog.askopenfilename(filetypes=[("Fichiers Texte", "*.txt")])
    if nom_fichier:
        with open(nom_fichier, "r", encoding="utf-8") as f:  # Spécification de l'encodage UTF-8
            text_area.delete("1.0", tk.END)  # Efface le texte existant
            text_area.insert(tk.END, f.read())  # Insère le contenu du fichier

def enregistrer_fichier(text_area):
    """Enregistre le contenu de la zone de texte dans un fichier en UTF-8"""
    nom_fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers Texte", "*.txt")])
    if nom_fichier:
        with open(nom_fichier, "w", encoding="utf-8") as f:  # Spécification de l'encodage UTF-8
            f.write(text_area.get("1.0", tk.END))  # Sauvegarde le contenu du text_area
