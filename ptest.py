from personnage import Personnage
import unittest

# Tests pour classe Personnage

pt = Personnage("Waldo", 50)

pt.set_energie_courante(30)
assert pt.get_energie_courante() == 30
pt.reset_energie()
assert pt.get_energie_courante() == 50
assert pt.est_mort() is False
assert pt.get_nom() == "Waldo"
assert pt.get_energie_courante() == 50
assert pt.get_energie_depart() == 50
pt.set_nom("Frank")
assert pt.get_nom() == "Frank"
pt.set_energie_depart(40)
assert pt.get_energie_depart() == 40
pt.set_energie_courante(25)
assert pt.get_energie_courante() == 25
assert pt.to_string() == "Frank a une énergie de 25"
assert pt.valider_nom("Toby") is True
assert pt.valider_nom("bd") is False
assert pt.valider_energie_depart(50) is True
assert pt.valider_energie_depart(500) is False
assert pt.valider_energie_depart(0) is False
assert pt.valider_energie_depart(-1) is False
assert pt.valider_energie_courante(50) is True
assert pt.valider_energie_courante(500) is False
assert pt.valider_energie_courante(-1) is False
assert pt.valider_energie_courante(0) is True
assert pt.valider_energie_courante(100) is True
