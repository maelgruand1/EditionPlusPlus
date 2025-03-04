import tkinter as tk
from tkinter import filedialog

def ouvrir_fichier():
    nom_fichier = filedialog.askopenfilename(filetypes=[("Fichiers MonTexte", "*.montexte")])
    if nom_fichier:
        with open(nom_fichier, "r") as f:
            texte.delete("1.0", tk.END)
            texte.insert(tk.END, f.read())

def enregistrer_fichier():
    nom_fichier = filedialog.asksaveasfilename(defaultextension=".montexte", filetypes=[("Fichiers MonTexte", "*.montexte")])
    if nom_fichier:
        with open(nom_fichier, "w") as f:
            f.write(texte.get("1.0", tk.END))

fenetre = tk.Tk()

menu_barre = tk.Menu(fenetre)
menu_fichier = tk.Menu(menu_barre, tearoff=0)
menu_fichier.add_command(label="Ouvrir", command=ouvrir_fichier)
menu_fichier.add_command(label="Enregistrer", command=enregistrer_fichier)
menu_barre.add_cascade(label="Fichier", menu=menu_fichier)
fenetre.config(menu=menu_barre)

texte = tk.Text(fenetre)
texte.pack()

fenetre.mainloop()