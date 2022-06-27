from tkinter.filedialog import *
from tkinter import messagebox
from util import Util
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
    def mettre_a_jour_liste(self):
        """
        Mets à jour et trie la liste des personnages par rapport à l'énergie courante. 
        Returns (list str): La liste triée des chaînes de caractères des personnages

        """

    def gestion_creer_sorcier(self):
        """
        Crée un personnage sorcier si les informations du sorcier (méthode saisir_et_creer_sorcier) 
        sont valides, on ajoute le sorcier à la liste (méthode ajouter_personnage) et on affiche le message approprié.  
        Sinon, on affiche seulement que le sorcier n’a pas été ajouté.
        """

    def saisir_et_creer_sorcier(self):
        """
        Retourne un objet Sorcier valide. Chaque information du sorcier demandée doit être validée. 
        L’annulation d’une info entraine automatiquement l’annulation des informations suivantes.  
        Si toutes les informations sont valides, un sorcier est alors instancié.
        
        Return (Sorcier): Le sorcier instancié si la création a réussie, None sinon.
        """

    def gestion_creer_guerrier(self):
        """
        Crée un personnage sorcier si les informations du sorcier (méthode saisir_et_creer_sorcier) 
        sont valides, on ajoute le sorcier à la liste (méthode ajouter_personnage) et on affiche le message approprié.  
        Sinon, on affiche seulement que le sorcier n’a pas été ajouté.
        """

    def saisir_et_creer_guerrier(self):
        """
        Retourne un objet Guerrier valide.  Chaque information du guerrier demandée doit être validée. 
        L’annulation d’une information entraine automatiquement l’annulation des informations suivantes.  
        Si toutes les infos sont valides, un guerrier est alors instancié.
        
        Returns (Guerrier): Le guerrier instancié si la création a réussie, None sinon.
        """

    def ajouter_personnage(self, personnage):
        """
        Ajoute le Personnage à la liste.
        Args:
            personnage (Personnage): Le personnage à ajouter. 
        """


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


    def gestion_augmenter_energie(self, index):
        """
        Reçoit l’indice du personnage sélectionné ou -1 si aucun personnage n’est sélectionné.  
        Si le personnage sélectionné n’est pas mort, réinitialiser son énergie. S’il n’y a aucun personnage 
        sélectionné ou s’il est mort, un message personnalisé est affiché.
        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné. 
        """


    def gestion_crier(self, index):
        """
        Reçoit l’indice du personnage sélectionné ou -1 si aucun personnage n’est sélectionné.  
        Si le personnage sélectionné n’est pas mort, émettre son cri.  S’il n’y a aucun personnage sélectionné ou 
        s’il est mort, un message personnalisé est affiché.
        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné. 
        """


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

    def gestion_enregistrer(self):
        """
        Permet de gérer l'enregistrement d'une liste de personnages dans le fichier courant.  
        Si on a un fichier courant, on écrit les personnages de la liste dedans 
        (voir méthode ecrire_fichier_personnages dans la classe Util) et on affiche un message approprié. 
        Si l’enregistrement n’a pas fonctionné, un message d’erreur est affiché. Si on n’a pas de fichier courant, 
        on enregistre dans un nouveau fichier en appelant la méthode (gestion_enregistrer_sous). 
        """



    def gestion_enregistrer_sous(self):
        """
        Permet de gérer l'enregistrement d'une liste de personnages dans un nouveau fichier.  
        On demande un nom de fichier à l’utilisateur, on l’assigne au fichier courant et on écrit 
        dedans les personnages (voir méthode ecrire_fichier_personnages dans la classe Util).  
        Afficher un message personnalisé s’il y a erreur lors de la sauvegarde ou si la sauvegarde est ok.
        """



    def gestion_vider_liste(self):
        """
        Permet de fermer le fichier courant. Si la liste n'est pas vide et que l'utilisateur veut sauvegarder ses 
        données, enregistrer les données de la liste dans le fichier courant (gestion_enregistrer) ou dans un 
        nouveau fichier (gestion_enregistrer_sous) s’il n’y a pas de fichier courant.  
        La liste est vidée et le fichier courant devient none.
        """


    def gestion_quitter(self):
        """
        Permet de quitter l'application après confirmation de l'utilisateur.
        """
