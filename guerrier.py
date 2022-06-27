from personnage import Personnage


class Guerrier(Personnage):
    """
    Classe représentant un Guerrier. Hérite de Personnage.
    Attributes:
        force_defaut (int): La valeur par défaut de la force
        force_max (int): La valeur maximum de la force
        perte_force_defaut (int): La perte de force lors d'une attaque
        gain_force_defaut (int): Le gain de force lors d'une resitution d'énergie
        force (int): La force courante du guerrier
    """
    def __init__(self, nom, energie_depart, force):
        """
        Le constructeur du Guerrier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et la force.
        NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom (str): Le nom du guerrier
            energie_depart (int): L'énergie de départ du guerrier
            energie (int): L'énergie courante du guerrier
            force (int): La force du guerrier
        """
        super().__init__(nom, energie_depart) # il y a un problème avec energie_depart vs energie
        self.force_defaut = 20
        self.force_max = 80
        self.perte_force_defaut = 2
        self.gain_force_defaut = 10
        self.force = force

    def to_string(self):
        """
        Retourne une chaîne du genre : "Le guerrier, nom de Personnage, a une énergie de valeur de
        l’énergie et une force de valeur de la force."

        Returns (str): La chaîne représentant le guerrier.
        """
        return f"Le guerrier, {self.nom}, a une énergie de {self.energie_courante} et une force de {self.force}"

    def valider_force(self, force):
        """
        Valide si la force en paramètre est valide (entre 0 et force_max inclusivement).
        Args:
            force (int): La force à valider

        Returns (bool): True si la force est valide, False sinon
        """
        return True if 0 <= force <= self.force_max else False

    def crier(self):
        """
        Retourne le cri du guerrier : "Vous allez goûter à la puissance de mon épée!"
        Returns (str): Le cri du guerrier
        """
        return "Vous allez goûter à la puissance de mon épée!"

    def attaquer(self, force_attaque):
        """
        Lorsqu’un guerrier se fait attaquer, son énergie est diminuée de la force de l’attaque.
        Si la force de l’attaque est plus grande que son énergie, l’énergie du guerrier devient 0 (il meurt).
        Lors d’une attaque, la force du guerrier est aussi modifiée.  Elle est diminuée, à chaque attaque,
        de la valeur de perte_force_defaut jusqu’à concurrence de 0.  Si le guerrier meurt pendant l’attaque,
        sa force est aussi mise à 0.
        Args:
            force_attaque (int): La force de l'attaque
        """
        if force_attaque > self.energie_courante:
            self.energie_courante = 0
            self.force = 0
        else:
            self.energie_courante -= force_attaque
            if self.force - self.perte_force_defaut >= 0:
                self.force -= self.perte_force_defaut
            else:
                self.force = 0

    def reset_energie(self):
        """
        Permet de remettre l’énergie courante du guerrier à sa valeur de départ (héritage) et
        augmente sa force (la valeur de force) par la valeur de gain_force_defaut jusqu’à concurrence de
        la force maximale sans jamais la dépasser.
        """
        self.energie_courante = self.energie_depart
        if self.force + self.gain_force_defaut <= self.force_max:
            self.force = self.force + self.gain_force_defaut
        else:
            self.force = self.force_max

    # setter et getter, a vous de compléter
    def set_force(self, force):
        self.force = force

    def get_force(self):
        return self.force
