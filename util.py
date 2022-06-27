import csv
import sys
from tkinter.filedialog import *
from tkinter import simpledialog

import sorcier
from sorcier import Sorcier
from guerrier import Guerrier
import pandas
import numpy


class Util:
    """
    Classe utilitaire comportant uniquement des méthodes statiques.
    """
    TYPE_SORCIER = "Sorcier"
    TYPE_GUERRIER = "Guerrier"

    @staticmethod
    def lire_fichier_personnages(fichier, liste_personnages):
        """
        Permet de lire un fichier de personnages reçu en entrée et de remplir la liste de personnages. Pour plus
        de détails, voir l'énoncé du travail. 
        Args:
            fichier (str): Le nom du fichier à lire 
            liste_personnages (list): La liste de personnages que la méthode doit remplir.  

        Returns:

        """
        with open(fichier, newline='') as f:
            reader = csv.reader(f)
            liste_personnages = list(reader)
        f.close()

        try:
            with open(fichier, 'r', encoding='utf-8', newline='') as f:
                reader = csv.reader(f)
                liste_personnages = list(reader)
            f.close()
        except Exception:
            print(sys.stderr, "erreur d'execution dans gestionOuvrir")
            sys.exit(1)


    @staticmethod
    def ecrire_fichier_personnages(fichier, liste_personnages):
        """
        Permet d’écrire la liste de personnages reçue en paramètre dans le fichier de personnages aussi reçu en entrée.
        Pour plus de détails, voir l'énoncé du travail.
        Args:
            fichier: 
            liste_personnages: 
        """
        try:
            with open(fichier, 'w', encoding='utf-8', newline='') as t:
                for i in liste_personnages:
                    if isinstance(i, Sorcier):
                        tmp_str = f"Sorcier;{i.nom};{i.energie_depart};{i.energie_courante};{i.nb_charmes}"
                    else:
                        tmp_str = f"Guerrier;{i.nom};{i.energie_depart};{i.energie_courante};{i.force}"
                    t.write(f"{tmp_str}\n")
                print(liste_personnages)
            t.close()
            return True
        except Exception:
            return False

    @staticmethod
    def saisir_objet_entier(question):
        """
        Permet de demander la saisie d'un entier et de le valider
        Args:
            question (str): La question à poser 

        Returns (int): L'entier saisi

        """
        objet_entier = -1

        valide = False

        while not valide:
            objet_entier = simpledialog.askstring("Saisie d'un entier", question)

            try:
                objet_entier = int(objet_entier)
                valide = True
            except ValueError:
                print("aucune sasie")

        return objet_entier


    @staticmethod
    def saisir_string(question):
        """
        Permet de demander la saisie d'une chaîne de caractères
        Args:
            question (str): La question à poser 

        Returns (str): La chaîne saisie

        """
        string_temp = ""

        valide = False

        while string_temp == "" and not valide:
            string_temp = simpledialog.askstring("Saisie d'une chaine de caractères", question)

            if string_temp == "":
                print("aucune saisie")
            else:
                valide = True

        return string_temp
