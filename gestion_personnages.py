from tkinter.filedialog import *
from tkinter import messagebox
from util import Util
from tkinter import filedialog as fd
from personnage import Personnage
from sorcier import Sorcier
from guerrier import Guerrier


class GestionPersonnages:
    """
    Classe s'occupant de la gestion des personnages. 
    Attributes:
        liste_personnages (list): La liste des personnages
        fichier_courant (str): Le nom du fichier courant
    """

    def __init__(self):
        self.fichier_courant = ""
        self.liste_personnages = []

    def mettre_a_jour_liste(self):
        """
        Mets à jour et trie la liste des personnages par rapport à l'énergie courante. 
        Returns (list str): La liste triée des chaînes de caractères des personnages
        """
        self.liste_personnages.sort(key=lambda x: x.energie_courante)
        return self.liste_personnages

    def gestion_creer_sorcier(self):
        """
        Crée un personnage sorcier si les informations du sorcier (méthode saisir_et_creer_sorcier) 
        sont valides, on ajoute le sorcier à la liste (méthode ajouter_personnage) et on affiche le message approprié.  
        Sinon, on affiche seulement que le sorcier n’a pas été ajouté.
        """
        s = self.saisir_et_creer_sorcier()
        if self.ajouter_personnage(s):
            messagebox.showinfo("Ajout d'un sorcier", "Le nouveau sorcier a été ajouté à la liste")
        else:
            messagebox.showinfo("Ajout d'un sorcier", "Erreur lors de la sauvegarde")

    def saisir_et_creer_sorcier(self):
        """
        Retourne un objet Sorcier valide. Chaque information du sorcier demandée doit être validée.
        L’annulation d’une info entraine automatiquement l’annulation des informations suivantes.
        Si toutes les informations sont valides, un sorcier est alors instancié.
        Return (Sorcier): Le sorcier instancié si la création a réussie, None sinon.
        """
        n = Util.saisir_string("Donnez le nom du Sorcier (entre 3 à 30)")
        ed = int(Util.saisir_objet_entier("Donnez l'énergie de départ du Sorcier"))
        c = int(Util.saisir_objet_entier("Donnez le nombre de charmes du Sorcier"))
        s = Sorcier(n, ed, c)
        if Personnage.valider_nom(s, n) and Personnage.valider_energie_depart(s, ed) and Sorcier.valider_nbr_charmes(s, c):
            return s
        else:
            return None

    def gestion_creer_guerrier(self):
        """
        Crée un personnage sorcier si les informations du sorcier (méthode saisir_et_creer_sorcier) 
        sont valides, on ajoute le sorcier à la liste (méthode ajouter_personnage) et on affiche le message approprié.  
        Sinon, on affiche seulement que le sorcier n’a pas été ajouté.
        """
        g = self.saisir_et_creer_guerrier()
        if self.ajouter_personnage(g):
            messagebox.showinfo("Ajout d'un guerrier", "Le nouveau guerrier a été ajouté à la liste")
        else:
            messagebox.showinfo("Ajout d'un guerrier", "Erreur lors de la sauvegarde")

    def saisir_et_creer_guerrier(self):
        """
        Retourne un objet Guerrier valide.  Chaque information du guerrier demandée doit être validée. 
        L’annulation d’une information entraine automatiquement l’annulation des informations suivantes.  
        Si toutes les infos sont valides, un guerrier est alors instancié.
        
        Returns (Guerrier): Le guerrier instancié si la création a réussie, None sinon.
        """
        n = Util.saisir_string("Donnez le nom du Guerrier (entre 3 à 30)")
        ed = Util.saisir_objet_entier("Donnez l'énergie de départ du Guerrier")
        f = Util.saisir_objet_entier("Donnez la force du Guerrier")
        g = Guerrier(n, ed, f)
        if Personnage.valider_nom(g, n) and Personnage.valider_energie_depart(g, ed) and Guerrier.valider_force(g, f):
            return g
        else:
            return None

    def ajouter_personnage(self, personnage):
        """
        Ajoute le Personnage à la liste.
        Args:
            personnage (Personnage): Le personnage à ajouter.
        """
        try:
            self.liste_personnages.append(personnage)
            return True
        except Exception:
            return False

    def gestion_attaquer(self, index):
        """
        Reçoit l’indice du personnage sélectionné ou -1 si aucun personnage n’est sélectionné.  
        Si le personnage sélectionné n’est pas mort, on saisit avec validation la force de l’attaque 
        (> 0 et <= energie_max).  Lorsque la force saisie est valide, on attaque le personnage sélectionné sinon on 
        affiche un message adéquat.  S’il n’y a aucun personnage sélectionné ou s’il est mort, 
        un message est affiché.
        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné.
        """
        if index == -1:
            messagebox.showinfo("Action sur un personnage", "Aucun personnage n'est selectionné")
        else:
            personnage = self.getPersonnage(index)
            if personnage.energie_courante > 0:
                a = Util.saisir_objet_entier(f"Entrez la force de l'attaque (valeur positive plus petite que {personnage.energie_courante + 1} )")
                if 0 < a <= 100:
                    personnage.attaquer(a)
                else:
                    messagebox.showinfo("Action sur un personnage",
                                        f"force de l'attaque invalide, elle doit être positive plus petite que {personnage.energie_courante + 1}")
            else:
                messagebox.showinfo("Action sur un personnage", "Le personnage est mort")

    def gestion_augmenter_energie(self, index):
        """
        Reçoit l’indice du personnage sélectionné ou -1 si aucun personnage n’est sélectionné.  
        Si le personnage sélectionné n’est pas mort, réinitialiser son énergie. S’il n’y a aucun personnage 
        sélectionné ou s’il est mort, un message personnalisé est affiché.
        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné. 
        """
        if index == -1:
            messagebox.showinfo("Action sur un personnage", "Aucun personnage n'est sélectionné")
        else:
            personnage = self.getPersonnage(index)
            if personnage.energie_courante == 0:
                messagebox.showinfo("Action sur un personnage", "Le personnage est mort")
            else:
                personnage.energie_courante = personnage.energie_depart

    def gestion_crier(self, index):
        """
        Reçoit l’indice du personnage sélectionné ou -1 si aucun personnage n’est sélectionné.  
        Si le personnage sélectionné n’est pas mort, émettre son cri.  S’il n’y a aucun personnage sélectionné ou 
        s’il est mort, un message personnalisé est affiché.
        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné. 
        """
        if index == -1:
            messagebox.showinfo("Cri du personnage", "Aucun personnage n'est sélectionné")
        else:
            personnage = self.getPersonnage(index)
            if personnage.energie_courante == 0:
                messagebox.showinfo("Action sur un personnage", "Le personnage est mort")
            else:
                messagebox.showinfo("Gestion personnages", personnage.crier())

    def gestion_ouvrir(self):
        """
        Permet de gérer l'ouverture et la lecture d'un fichier de personnages 
        (un fichier .txt qui contient des informations sur des personnages, un personnage par ligne).  
        Si la liste n’est pas vide, on demande à l’utilisateur s’il veut sauvegarder les données courantes et 
        s’il répond oui, on fait appel à gestion_enregistrer_sous.  Ensuite, on demande à l’utilisateur le nom du 
        fichier à ouvrir.  Si le fichier choisi n’est pas null, le fichier à ouvrir devient le fichier courant 
        et si la lecture du fichier n’a pas bien fonctionné (voir méthode lireFichierPersonnages dans classe Util), 
        un message d’erreur est affiché.
        """

        # n = Util.saisir_string("Donnez le nom du Sorcier (entre 3 à 30)")
        # ed = int(Util.saisir_objet_entier("Donnez l'énergie de départ du Sorcier"))
        # c = int(Util.saisir_objet_entier("Donnez le nombre de charmes du Sorcier"))
        # s = Sorcier(n, ed, c)
        # if Personnage.valider_nom(s, n) and Personnage.valider_energie_depart(s, ed) and Sorcier.valider_nbr_charmes(s, c):
        #     return s
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Ouvrir un fichier',
            initialdir='',
            filetypes=filetypes)

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                temp_line = line.rstrip()
                list_perso = temp_line.split(";")
                if list_perso[0] == "Sorcier":
                    s = Sorcier(list_perso[1], int(list_perso[2]), int(list_perso[4]))
                    if Personnage.valider_nom(s, s.nom) and Personnage.valider_energie_depart(s, s.energie_depart) and Sorcier.valider_nbr_charmes(s, s.nb_charmes):
                        self.ajouter_personnage(s)
                elif list_perso[0] == "Guerrier":
                    g = Guerrier(list_perso[1], int(list_perso[2]), int(list_perso[4]))
                    if Personnage.valider_nom(g, g.nom) and Personnage.valider_energie_depart(g, g.energie_depart) and Guerrier.valider_force(g, g.force):
                        self.ajouter_personnage(g)
        file.close()
        self.fichier_courant = filename

    def gestion_enregistrer(self):
        """
        Permet de gérer l'enregistrement d'une liste de personnages dans le fichier courant.  
        Si on a un fichier courant, on écrit les personnages de la liste dedans 
        (voir méthode ecrire_fichier_personnages dans la classe Util) et on affiche un message approprié. 
        Si l’enregistrement n’a pas fonctionné, un message d’erreur est affiché. Si on n’a pas de fichier courant, 
        on enregistre dans un nouveau fichier en appelant la méthode (gestion_enregistrer_sous). 
        """
        if self.fichier_courant == "":
            self.gestion_enregistrer_sous()
        else:
            if Util.ecrire_fichier_personnages(self.fichier_courant, self.liste_personnages):
                messagebox.showinfo("Gestion personnages", "Sauvegarde des données effectuée correctement")
                return True
            else:
                messagebox.showinfo("Gestion personnages", "Erreur enregistrement")
                return None

    def gestion_enregistrer_sous(self):
        """
        Permet de gérer l'enregistrement d'une liste de personnages dans un nouveau fichier.  
        On demande un nom de fichier à l’utilisateur, on l’assigne au fichier courant et on écrit 
        dedans les personnages (voir méthode ecrire_fichier_personnages dans la classe Util).  
        Afficher un message personnalisé s’il y a erreur lors de la sauvegarde ou si la sauvegarde est ok.
        """
        filename = fd.asksaveasfilename(
            title='Enregistrer un fichier sous',
            initialdir=''
        )
        self.fichier_courant = filename
        if Util.ecrire_fichier_personnages(filename, self.liste_personnages):
            messagebox.showinfo("Gestion personnages", "Sauvegarde des données effectuée correctement")
            return True
        else:
            messagebox.showinfo("Gestion personnages", "Erreur enregistrement")
            return None

    def gestion_vider_liste(self):
        """
        Permet de fermer le fichier courant. Si la liste n'est pas vide et que l'utilisateur veut sauvegarder ses 
        données, enregistrer les données de la liste dans le fichier courant (gestion_enregistrer) ou dans un 
        nouveau fichier (gestion_enregistrer_sous) s’il n’y a pas de fichier courant.  
        La liste est vidée et le fichier courant devient none.
        """
        response = messagebox.askyesno("Gestion personnages", "Voulez-vous sauvegarder les donn/es courantes avant de vider la liste de personnages?")
        if response:
            if self.fichier_courant == "":
                self.gestion_enregistrer_sous()
            else:
                self.gestion_enregistrer()

    def getPersonnage(self, index):
        return self.liste_personnages[index]

    def gestion_quitter(self):
        """
        Permet de quitter l'application après confirmation de l'utilisateur.
        """
        return True if messagebox.askyesno('Quitter', 'Voulez-vous vraiment quitter ce programme?') else False
