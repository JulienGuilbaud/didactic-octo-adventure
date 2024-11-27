#import des modules
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image  

#import des fonctions
import FeedBase

def function1():
    # Code pour la fonction 1
    FeedBase.FeedBase()
    goodbye()


def function2():
    # Code pour la fonction 2
    print("Function 2 executed")
    goodbye()


def function3():
    # Code pour la fonction 3
    print("Function 3 executed")
    goodbye()

def goodbye():
    # Affiche un message d'au revoir et ferme la fenêtre
    messagebox.showinfo("Au Revoir", "Merci et au revoir!")
    root.destroy()

# Crée la fenêtre principale
root = tk.Tk()
root.title("Exécuteur de Fonctions")

# Style pour un look moderne (optionnel)
style = ttk.Style()
style.theme_use("clam")  # Ou explorer d'autres thèmes comme 'aqua', 'alt', etc.

# Cadre pour les boutons
button_frame = ttk.Frame(root, padding="20")
button_frame.pack()

# Ajoute le logo de l'entreprise
try:
    # Il est important d'utiliser ImageTk.PhotoImage pour que l'image s'affiche correctement
    logo_image = Image.open("asset/2.png")  # Ouvrir l'image avec PIL.Image
    logo = ImageTk.PhotoImage(logo_image) # Convertir en objet PhotoImage
    logo_label = tk.Label(root, image=logo)
    logo_label.image = logo # Conserver une référence à l'image pour éviter qu'elle ne soit détruite par le garbage collector
    logo_label.pack(pady=(0, 20)) # Ajoute un espacement sous le logo
except FileNotFoundError:
    print("Fichier du logo non trouvé.  Vérifiez le chemin : asset/2.png")  # Message d'erreur plus précis

# Boutons
button1 = ttk.Button(button_frame, text="Flux TEST (NEW PARTS)", command=function1) # Appeler la fonction FeedBase du module FeedBase
button1.pack(pady=10)

button2 = ttk.Button(button_frame, text="Function 2", command=function2)
button2.pack(pady=10)

button3 = ttk.Button(button_frame, text="Function 3", command=function3)
button3.pack(pady=10)

button4 = ttk.Button(button_frame, text="Quiter", command=goodbye) # Correction orthographique: "Quitter"
button4.pack(pady=10)

root.mainloop()

