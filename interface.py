from tkinter import *
from tkinter.filedialog import *

from gestion_personnages import GestionPersonnages


class Interface(Frame):
    gp = GestionPersonnages()
    pIndex = -1

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.listbox = Listbox(self)
        self.index = None
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Personnages : Un exemple d'héritage et de polymorphisme")
        self.pack(fill=BOTH, expand=True)

        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Fichier", menu=menu)
        menu.add_command(label="Ouvrir", command=self.menu_ouvrir_click)

        # ajouter les autres options
        menu.add_command(label="Enregistrer", command=self.menu_enregistrer_click)
        menu.add_command(label="Enregistrer sous", command=self.menu_enregistrer_sous_click)
        menu.add_command(label="Vider liste", command=self.menu_vider_liste_click)
        menu.add_command(label="Quitter", command=self.menu_quitter_click)


        self.master.config(menu=self.menubar)

        # frame 1 (droite)
        self.frame1 = Frame(self)
        # frame 2 (gauche)
        self.frame2 = Frame(self, width=100, height=700, borderwidth=5)

        # Ajout de labels dans les frames

        # Ajout du listbox
        self.listbox = Listbox(self.frame2, self.gp.liste_personnages, width=100, height=800)
        self.listbox.bind('<<ListboxSelect>>', self.listbox_click)

        # Ajout de bouttons
        btn_creer_sorcier = Button(self.frame1, text="Créer un sorcier", command=self.btn_sorcier_click, height=5, width=200)
        btn_creer_sorcier.pack()

        btn_creer_guerrier = Button(self.frame1, text="Créer un guerrier", command=self.btn_guerrier_click, height=5, width=200)
        btn_creer_guerrier.pack()

        btn_attaquer = Button(self.frame1, text="Attaquer", command=self.btn_attaquer_click, height=5, width=200)
        btn_attaquer.pack()

        btn_redonner_energie = Button(self.frame1, text="Réinitialiser l'énergie", command=self.btn_redonner_energie_click, height=5, width=200)
        btn_redonner_energie.pack()

        btn_crier = Button(self.frame1, text="Crier", command=self.btn_crier_click, height=5, width=200)
        btn_crier.pack()

        # TESTING
        self.frame2.pack(side="left")
        self.listbox.pack()
        self.frame1.pack(side="right")

    def list_is_empty(self):
        try:
            self.index = int(self.listbox.curselection()[0])
        except IndexError:
            return True

        return False

    # Ajoute un personnage dans la listbox
    def append_list(self, personnage):
        self.listbox.insert(END, personnage)

    # Remplace tous les personnages de la listbox par une nouvelle liste
    def update_list(self, personnages):
        self.listbox.delete(0, END)

        for personnage in personnages:
            self.listbox.insert(END, personnage.to_string())

        self.pIndex = -1

    # Permet d'identifier le personnage selectionné (set pIndex)
    def listbox_click(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        index = widget.curselection()[0]

        # print ("selection:", selection, ": '%s'" % value)
        self.pIndex = index
        # print(self.gp.getPersonnage(index))

    def menu_ouvrir_click(self):
        self.gp.gestion_ouvrir()
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        if personnages:
            self.update_list(personnages)

    def menu_enregistrer_click(self):
        self.gp.gestion_enregistrer()

    def menu_enregistrer_sous_click(self):
        self.gp.gestion_enregistrer_sous()

    def menu_vider_liste_click(self):
        self.gp.gestion_vider_liste()
        self.listbox.delete(0, END)
        # quit()

    def menu_quitter_click(self):
        if self.gp.gestion_quitter():
            quit()

    def btn_sorcier_click(self):
        self.gp.gestion_creer_sorcier()
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        if personnages:
            self.update_list(personnages)

    def btn_guerrier_click(self):
        self.gp.gestion_creer_guerrier()
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        if personnages:
            self.update_list(personnages)

    def btn_attaquer_click(self):
        self.gp.gestion_attaquer(self.pIndex)
        row = self.pIndex
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        if personnages:
            self.update_list(personnages)

        # Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")

    def btn_redonner_energie_click(self):
        self.gp.gestion_augmenter_energie(self.pIndex)
        row = self.pIndex
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        self.update_list(personnages)

        # Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")

    def btn_crier_click(self):
        self.gp.gestion_crier(self.pIndex)
        row = self.pIndex

        # Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")


def main():
    root = Tk()
    root.geometry("700x400+300+100")
    app = Interface(root)
    root.mainloop()


if __name__ == '__main__':
    main()
