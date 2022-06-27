
from tkinter import *
from tkinter.filedialog import *

from gestion_personnages import GestionPersonnages


class Interface(Frame):
    gp = GestionPersonnages()
    pIndex = -1

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Personnages : Un exemple d'héritage et de polymorphisme")
        self.pack(fill=BOTH, expand=True)

        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Fichier", menu=menu)
        menu.add_command(label="Ouvrir...", command=self.menuOuvrir_Click)
       #ajouter les autres options


        self.master.config(menu=self.menubar)

        # frame 1 (droite)


        # frame 2 (gauche)


        # Ajout de labels dans les frames


        # Ajout du listbox


        # Ajout de bouttons


    def listIsEmpty(self):
        try:
            self.index = int(self.listbox.curselection()[0])
        except IndexError:
            return True

        return False

    #Ajoute un personnage dans la listbox
    def appendList(self, personnage):
        self.listbox.insert(END, personnage)


    #Remplace tous les personnages de la listbox par une nouvelle liste
    def updateList(self, personnages):
        self.listbox.delete(0, END)

        for personnage in personnages:
            self.listbox.insert(END, personnage)

        self.pIndex = -1

    #Permet d'identifier le personnage selectionné (set pIndex)
    def listbox_Click(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        index = widget.curselection()[0]

        #print ("selection:", selection, ": '%s'" % value)

        self.pIndex = index
        #print(gp.getPersonnage(index))


    def menuOuvrir_Click(self):
        self.gp.gestionOuvrir()
        personnages = self.gp.mettreAJourListe()

        # Update listview
        if personnages:
            self.updateList(personnages)


    def menuEnregistrer_Click(self):
        self.gp.gestionEnregistrer()

    def menuEnregistrerSous_Click(self):
        self.gp.gestionEnregistrerSous()


    def menuViderListe_Click(self):
        self.gp.gestionViderListe()
        self.listbox.delete(0, END)
            #quit()

    def menuQuitter_Click(self):
        if self.gp.gestionQuitter():
            quit()



    def btnSorcier_Click(self):
        self.gp.gestionCreerSorcier()
        personnages = self.gp.mettreAJourListe()

        # Update listview
        if personnages:
            self.updateList(personnages)

    def btnGuerrier_Click(self):
        self.gp.gestionCreerGuerrier()
        personnages = self.gp.mettreAJourListe()

        # Update listview
        if personnages:
            self.updateList(personnages)


    def btnAttaquer_Click(self):
        self.gp.gestionAttaquer(self.pIndex)
        row = self.pIndex
        personnages = self.gp.mettreAJourListe()

        # Update listview
        if personnages:
            self.updateList(personnages)

        #Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")


    def btnRedonnerEnergie_Click(self):
        self.gp.gestionAugmenterEnergie(self.pIndex)
        row = self.pIndex
        personnages = self.gp.mettreAJourListe()

        # Update listview
        self.updateList(personnages)

        #Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")

    def btnCrier_Click(self):
        self.gp.gestionCrier(self.pIndex)
        row = self.pIndex

        #Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")



def main():
    root = Tk()
    root.geometry("700x400+300+100")
    app = Interface(root)
    root.mainloop()



if __name__ == '__main__':
    main()

