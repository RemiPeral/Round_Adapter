'''
Created on 10 mars 2015

@author: rperal
'''
import csv
from tkinter import *
import tkinter.ttk as ttk
from array import array
from tkinter.ttk import Combobox
from tkinter.filedialog import FileDialog, askopenfilename
from tkinter.tix import FileTypeList
import os
import pandas as pd
import xlrd
from xlrd.timemachine import xrange

class Information(Frame):
    '''
    classdocs
    '''
    def __init__(self, fenetre, leDossier, **kwargs):
        
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)

        self.leDossier = leDossier
        
        self.fname = askopenfilename(filetypes=(
                                           ("Feuille de calcul", "*.xls;*.xlsx"),
                                           ("All files", "*.*") ))
        #Récupère la feuille Excel de la tournée et la convertit en CSV
        xls = pd.ExcelFile(self.fname)
        df = xls.parse('Feuil1', index_col= None, na_values=['NA'])
        df.to_csv('csvTemporaire.csv', index = False, index_label= False, header= False)
   
        self.champInformations = Label(self, text = "Veuillez selectionner le cabinet concerne : ")
        self.champInformations.pack()
            
        self.champEtablishment = Label(self, text="Etablissement : ")
        self.champEtablishment.pack()
        
        self.lEtablishment = Listbox(self, width = 30)
    
        with open('csvTemporaire.csv', newline='', encoding="utf8", errors='ignore') as csvfile:
            
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            self.leDepartement = 0;
            
            #Récupère le numéro de département de l'établissement concerné par l'établissement
            for row in reader:
                self.zipCode = row[1]
                
                if len(self.zipCode) < 5:
                    self.leDepartement = self.zipCode[:1]
                    self.leDepartement = '0'.join(self.leDepartement)
                else:
                    self.leDepartement = self.zipCode[:2]

                self.leDepartement = int(self.leDepartement)
                if self.leDepartement > 20:
                    self.leDepartement = self.leDepartement + 1
                self.leDepartement = str(self.leDepartement)
      
        csvfile.close()
    
        with open('establishment1.csv', newline= '') as csvEtablissement:
         
            idEtablissement = 0
            idOffice = 0
            self.listeEtablissements = []
        
            readerEtab = csv.reader(csvEtablissement, delimiter = ',', quotechar = '/')
            
            #Remplis la listbox du nom de tous les cabinets qui correspondent au numéro du département précédemment récupéré
            #Permets également de récupérer l'id du cabinet et de l'établissement concerné 
            
            for rowEtab in readerEtab:
                
                idEtablissement = rowEtab[0]
                idOffice = rowEtab[1]
                nomEtablissement = ''.join(rowEtab[3])
                
                if self.leDepartement == "":
                    
                    self.lEtablishment.insert(idEtablissement, nomEtablissement)
                    self.listeEtablissements.append([idEtablissement, idOffice, nomEtablissement])
                else:
                    if rowEtab[2] == self.leDepartement:
                        
                        self.lEtablishment.insert(idEtablissement, nomEtablissement)
                        self.listeEtablissements.append([idEtablissement, idOffice, nomEtablissement])
                        
            if self.listeEtablissements == []:  
                for rowEtab in readerEtab:
                    idEtablissement = rowEtab[0]
                    idOffice = rowEtab[1]
                    nomEtablissement = ''.join(rowEtab[3])
                    self.lEtablishment.insert(idEtablissement, nomEtablissement)
                    self.listeEtablissements.append([idEtablissement, idOffice, nomEtablissement])
                            
        self.lEtablishment.pack()   
        self.bouton_envoyer = Button(self, text="Valider", command = self.envoyer)
        self.bouton_envoyer.pack()
        
    def envoyer(self):
       
        with open('csvTemporaire.csv', newline='', encoding="utf8", errors='ignore') as csvfile:
            
            #Ce bout de code permet de déterminer le nombre de lignes du Csv généré à partir de la liste des tournées       
            limite = 0
            buf_size = 1024 * 1024
            read_f = csvfile.read
            buf = read_f(buf_size)
            while buf:
                limite += buf.count('\n')
                buf = read_f(buf_size)
            csvfile.close()
            
            with open('csvTemporaire.csv', newline='', encoding="utf8", errors='ignore') as csvfile:
                
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
                keyElement = 0
                data =[]
                valeurJournees = ""
                nbElements = 0
  
                #Récupère les informations concernant les jours de la tournée et traite les résultats de manière à ce qu'ils soient conforme au format de données de la BDD
                for row in reader:
                    keyElement = keyElement + 1;
                    nbElements = nbElements + 1
                    ville = row[0]
                    
                    if row[3] != "":
                        row[3] = row[3].replace("X", '1')
                        row[3] = row[3].replace("M", '1')
                        row[3] = row[3].replace("A", '1')
                        row[3] = row[3].replace("J", '1')
                        row[3] = row[3].replace("x", '1')
                        
                    else :
                        row[3] = row[3].replace(" ", '0')
                        row[3] = row[3].replace("", '0')
                        
                    monday = row[3]
        
                    if row[4] != "":
                        row[4] = row[4].replace("X", '1')
                        row[4] = row[4].replace("M", '1')
                        row[4] = row[4].replace("A", '1')
                        row[4] = row[4].replace("J", '1')
                        row[4] = row[4].replace("x", '1')
                        
                    else :
                        row[4] = row[4].replace(" ", '0')
                        row[4] = row[4].replace("", '0')
                        
                    tuesday = row[4]
            
                    if row[5] != "":
                        row[5] = row[5].replace("X", '1')
                        row[5] = row[5].replace("M", '1')
                        row[5] = row[5].replace("A", '1')
                        row[5] = row[5].replace("J", '1')
                        row[5] = row[5].replace("x", '1')
                        
                    else: 
                        row[5] = row[5].replace(" ", '0')
                        row[5] = row[5].replace("", '0')
                        
                    wednesday = row[5]
            
                    if row[6] != "":
                        row[6] = row[6].replace("X", '1')
                        row[6] = row[6].replace("M", '1')
                        row[6] = row[6].replace("A", '1')
                        row[6] = row[6].replace("J", '1')
                        row[6] = row[6].replace("x", '1')
                        
                    else: 
                        row[6] = row[6].replace(" ", '0')
                        row[6] = row[6].replace("", '0')
                        
                    thursday = row[6]
        
                    if row[7] != "":
                        row[7] = row[7].replace("X", '1')
                        row[7] = row[7].replace("M", '1')
                        row[7] = row[7].replace("A", '1')
                        row[7] = row[7].replace("J", '1')
                        row[7] = row[7].replace("x", '1')
                        
                    else: 
                        row[7] = row[7].replace(" ", '0')
                        row[7] = row[7].replace("", '0')
                        
                    friday = row[7]
        
                    keyElement = str(keyElement)
                    reqOffice = '0'
                    reqEtablissement = '0'
         
                    for rowList in self.listeEtablissements:
                        if rowList[2] == self.lEtablishment.get(self.lEtablishment.curselection()):
                            reqOffice = str(rowList[1])
                            reqEtablissement = str(rowList[0])
                    
                    data = ["NULL", reqOffice, reqEtablissement, self.leDepartement, self.zipCode, '"'+ville+'"', monday, monday, tuesday, tuesday, wednesday, wednesday, thursday, thursday, friday, friday, '1',  '0', ' "0000-00-00 00:00:00" ', ' "0000-00-00 00:00:00" ']
        
                    keyElement = int(keyElement)
            
                    if(nbElements == limite):
                        valeurJournees += '('+(' , ' .join(data)) + ')'
                        
                    else:
                        valeurJournees += '('+(' , ' .join(data)) + '),\n'
                
          
                #Génération de la requête SQL en fonction des paramètres récupérés dans le programme
                requeteSQL = "INSERT INTO `test`.`round` (`id_round`, `id_office`, `id_establishment`, `id_departement`, `zip_code`, `city`, `monday_am`, `monday_pm`, `tuesday_am`, `tuesday_pm`, `wednesday_am`, `wednesday_pm`, `thursday_am`, `thursday_pm`, `friday_am`, `friday_pm`, `is_enable`, `is_delete`, `date_create`, `date_update`) VALUES" + valeurJournees
                
                #Création du fichier script SQL
                nomFichier = "insertSQL.sql"
                
                fichierRequete = open(self.leDossier+ "//"+ nomFichier, "w")
                fichierRequete.write(requeteSQL)
                
                self.lEtablishment.destroy()
                
                self.champEtablishment.destroy()
                self.bouton_envoyer.destroy()
                self.champInformations["fg"] = "red"
                self.champInformations["text"] = "Votre fichier script " + nomFichier + " est disponible a l'adresse " + self.leDossier
                
                fichierRequete.close()
                csvfile.close()
                os.remove("csvTemporaire.csv")
        