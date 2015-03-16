import csv
from tkinter import *
import tkinter.ttk as ttk
from Information import Information
from tkinter.filedialog import askdirectory
with open('Tournees_Alscace.csv', newline='') as csvfile:
    def selectionDossier(): 
        
        leDossier = askdirectory()
        var_dossier.set(leDossier)
    
    def setValue():
        print(zoneDossier.get())
        
        if zoneDossier.get() != "":
            
            fenetre.destroy()
            fenetreInformation = Tk()
            informations = Information(fenetreInformation, var_dossier.get())
            
            informations.mainloop()
    
        else:
            champ_label['text'] = "Veuillez choisir un dossier de destination pour votre script SQL" 
            champ_label["fg"] = "red"  
    
    fenetre = Tk()
    champ_label = Label(fenetre, text="Saisissez le dossier ou stocker votre script SQL : ")
    champ_label.pack()
    
    var_dossier = StringVar()
    
    zoneDossier = Entry(fenetre, textvariable=var_dossier, width=30)
    zoneDossier.pack()
    
    bouton_chercher = Button(fenetre, text="Selection", command = selectionDossier)
    bouton_chercher.pack()
    
    bouton_valider = Button(fenetre, text = "Valider", command = setValue)
    bouton_valider.pack()
    
    
    bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
    bouton_quitter.pack()
    
    
    fenetre.mainloop()
   
        