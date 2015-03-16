import csv
from tkinter import *
import tkinter.ttk as ttk
from Information import Information
from tkinter.filedialog import askdirectory

#Methode qui permet de demander et récuperer l'adresse du dossier de destination
def selectionDossier():  
        
    leDossier = askdirectory()
    var_dossier.set(leDossier)

def setValue():
    #Si l'utilisateur à selectionné un dossier, la fenêtre actuelle est détruite et fait place à la suivante en ayant pour paramètre l'adresse de destination du fichier
    if zoneDossier.get() != "":        
        fenetre.destroy()
        fenetreInformation = Tk()
        informations = Information(fenetreInformation, var_dossier.get())          
        informations.mainloop()

    else:
        champ_label['text'] = "Veuillez choisir un dossier de destination pour votre script SQL" 
        champ_label["fg"] = "red"  

# Création de l'interface de l'utilisateur
fenetre = Tk()
champ_label = Label(fenetre, text="Saisissez le dossier où stocker votre script SQL : ")
champ_label.pack()

var_dossier = StringVar()

zoneDossier = Entry(fenetre, textvariable=var_dossier, width=30)
zoneDossier.pack()

#Permet a l'utilisateur de sélectionner un dossier de destination pour son script SQL
bouton_chercher = Button(fenetre, text="Sélection", command = selectionDossier)
bouton_chercher.pack()

bouton_valider = Button(fenetre, text = "Valider", command = setValue)
bouton_valider.pack()


bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()


fenetre.mainloop()

