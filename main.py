from classTurn import Tournaments
from classPlayer import Player
from classRound import Round
from classMatch import Match


dico_joueurs = {"cle":3}


Turn1 = Tournaments("Des familles", "Lille", "23/05/2021", "2 min", 2, "description")
joueur1 = Player("cama","karla", "21/12/1899", "f", 1001)
joueur2 = Player("cama","Paco", "21/12/1899", "f", 1000)
joueur3 = Player("cama","Brian", "21/12/1899", "f", 500)
joueur4 = Player("cama","Bernadette", "21/12/1899", "f", 1500)
joueur5 = Player("cama","Martine", "21/12/1899", "f", 1001)
joueur6 = Player("cama","Melina", "21/12/1899", "f", 800)
joueur7 = Player("cama","Yvette", "21/12/1899", "f", 500)
joueur8 = Player("cama","Oscar", "21/12/1899", "f", 1400)

liste_joueurs = [joueur1, joueur2, joueur3, joueur4, joueur5, joueur6, joueur7, joueur8]


def ajouter_tous_les_joueurs_au_dict(liste):
    for i in liste:
        d = {i.get_prenom() : i.get_classement()}
        dico_joueurs.update(d)

ajouter_tous_les_joueurs_au_dict(liste_joueurs)

print(dico_joueurs)

def creer_pairs():
        if joueur1.get_classement() == joueur2.get_classement():
            Round.get_choose_player_1(joueur1)
        else:
            print("c'est paaas possssiiiiblleee")
        
    