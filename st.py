from sorcier import Sorcier

# Tests pour classe Sorcier


st = Sorcier("Merlin", 80, 15)
assert st.crier() == "Je vais tous vous anéantir!"
st.attaquer(30)
assert st.get_energie_courante() == 50
st.attaquer(200)
assert st.get_energie_courante() == 0
st.reset_energie()
assert st.get_energie_courante() == 80
assert st.valider_nbr_charmes(15) is True
assert st.valider_nbr_charmes(60) is False
assert st.valider_nbr_charmes(0) is True
assert st.valider_nbr_charmes(-1) is False
st.set_nbr_charmes(10)
assert st.get_nbr_charmes() == 10
assert st.to_string() == "Le sorcier, Merlin, a une énergie de 80 et 10 charmes"
