from classTurn import Tournaments
from classPlayer import Player
from classRound import Round
from classMatch import Match



def infos_tournoi():
    turn = Tournaments(input("Nom du tournois : "),input("Lieu du tournois : "),\
            input("Date du tournois : "),input("Nombre de tour du tournois : "),\
            input("Timing du tournois : "),input("Description du tournois : "))
     
    return turn.info_turn()
    
def infos_joueur():
    joueur = Player(input("Nom du joueur : "), input("Prénom : "),\
                input("Date : "), input("Sexe : "), input("Classement : "))
     
    return joueur.info_liste()
    
    
def ajout_joueur(liste,func):
    """ Permet à l'utilisateur d'entrer de nouveaux joueurs """ 
    
    while True:
        try :
            reponse = input(f"Souhaitez-vous ajouter un nouveau joueur ? ").capitalize()
            if reponse == "Yes" or reponse == "Oui":
                ajout_joueur = func()
                liste.append(ajout_joueur)
                continue
            else:
                print(f"Vous ne souhaitez pas ajouter de nouveau joueur.")
                break
                
        except ValueError:
            print(f"Le format de votre réponse n'est pas bon. Veuillez recommencer.")
            break
            
           



def joueur_numerotation(liste, func):
    """ Sauvegarder des joueurs dans la liste """
    liste.append(func)
    
    
def trie(liste):
    """ Trie la liste  """
    liste.sort(key = lambda x: x[1])
    return liste


def creer_deux_groupes(groupe1, groupe2, liste):
    """ 1. create 2 group  """
    
    for i in liste[:4]:
        groupe1.append(i)
    for i in liste[-4:]:
        groupe2.append(i)
        
        
def creer_4_pairs(groupe1, groupe2):
    """ 2. create pairs  """
    pair1 = (groupe1[0], groupe2[0])
    pair2 = (groupe1[1], groupe2[1])
    pair3 = (groupe1[2], groupe2[2])
    pair4 = (groupe1[3], groupe2[3])
    
    pairs_tour1 = [pair1, pair2, pair3, pair4]
    
    return pairs_tour1



def main():           
    liste_ajout_joueur = []
    groupe1 = []
    groupe2 = []
    ajout_joueur(liste_ajout_joueur, infos_joueur)
    creer_deux_groupes(groupe1, groupe2, liste_ajout_joueur)
    tour1 = creer_4_pairs(groupe1, groupe2)
    print(tour1)
            
if __name__ == "__main__":
    main()