class Personnage:
    """
    Attributes:
        energie_depart_defaut (int): L'énergie de départ par défaut
        energie_depart_min (int): L'énergie de départ minimum
        energie_max (int): L'énergie maximum en tout temps
        longueur_nom_min (int) : La longueur minimale du nom
        longueur_nom_max (int) : La longueur maximale du nom
        nom (str) : Le nom
        energie_depart (int): L'énergie de départ
        energie_courante (int): L'énergie courante

    """
    def __init__(self, nom, energie_depart):
        """
        Le constructeur du Personnage. Il doit initialiser le nom, l’énergie de départ et l’énergie courante. 
        À la création d’un objet personnage, l’énergie courante égale à l’énergie de départ.
        Args:
            nom (str): Le nom du personnage  
            energie_depart (int): L'énergie de départ 
        """
        self.energie_depart_defaut = 20
        self.energie_depart_min = 1
        self.energie_max = 100
        self.longueur_nom_min = 3
        self.longueur_nom_max = 30
        self.nom = nom
        self.energie_depart = energie_depart
        self.energie_courante = energie_depart

    def crier(self):
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def attaquer(self, force_attaque):
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def est_mort(self):
        """
        Retourne vrai lorsque l’énergie du personnage est à 0.
        Returns (bool): True si le personnage est mort, False sinon.
        """
        return True if self.energie_courante == 0 else False

    def valider_nom(self, nom):
        """
        Valide le nom du personnage. Un nom de personnage est valide lorsqu’il a la bonne longueur 
        (entre min et max) bornes incluses.
        Args:
            nom (str): Le nom à valider

        Returns (bool): True si le nom est valide, False sinon.
        """
        return True if self.longueur_nom_min <= len(nom) <= self.longueur_nom_max else False

    def valider_energie_courante(self, energie_courante):
        """
        Valide l'énergie courante. Elle doit être positive (0 inclus) et ne doit pas dépasser energie_max.
        Args:
            energie_courante (int): L'énergie à valider.

        Returns (bool): True si l'énergie est valide, False sinon.

        """
        return True if 0 <= energie_courante <= self.energie_max else False

    def valider_energie_depart(self, energie_depart):
        """
        Valide l'énergie de départ. Elle est valide lorsqu’elle est entre energie_depart_min et 
        energie_max. (bornes incluses). 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'énergie de départ est valide, False sinon.
        """
        return True if self.energie_depart_min <= energie_depart <= self.energie_max else False

    def reset_energie(self):
        """
        Remet l’énergie courante du personnage à sa valeur de départ.
        """
        self.energie_courante = self.energie_depart

    def get_energie_courante(self):
        """
        Retourne l'énergie courante
        Returns (int): L'énergie courante
        """
        return self.energie_courante

    def set_energie_courante(self, energie_courante):
        """
        Assigne l'énergie courante si elle est valide. 
        Args:
            energie_courante (int): L'énergie courante 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        try:
            self.energie_courante = energie_courante
            return True
        except:
            return False

    def get_nom(self):
        """
        Retourne le nom.
        Returns (str): Le nom.
        """
        return self.nom

    def set_nom(self, nom):
        """
        Assigne le nom s'il est valide. 
        Args:
            nom (str): Le nom

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        try:
            self.nom = nom
            return True
        except TypeError:
            return False

    def get_energie_depart(self):
        """
        Retourne l'énergie de départ.
        Returns (int): L'énergie de départ
        """
        return self.energie_depart

    def set_energie_depart(self, energie_depart):
        """
        Assigne l'énergie de départ si elle est valide. 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        self.energie_depart = energie_depart


    # compléter la méthode manquante
    def to_string(self):
        return self.nom + " a une énergie de " + str(self.energie_courante)
