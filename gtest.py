from guerrier import Guerrier

# Test pour classe Guerrier

gt = Guerrier("Tony", 70, 50)
assert gt.crier() == "Vous allez goûter à la puissance de mon épée!"
gt.attaquer(20)
assert gt.get_energie_courante() == 50
assert gt.get_force() == 48
gt.attaquer(200)
assert gt.get_energie_courante() == 0
assert gt.get_force() == 0
gt.reset_energie()
assert gt.get_energie_courante() == 70
assert gt.valider_force(50) is True
assert gt.valider_force(100) is False
assert gt.valider_force(-1) is False
gt.set_force(30)
assert gt.get_force() == 30
assert gt.to_string() == "Le guerrier, Tony, a une énergie de 70 et une force de 30"
