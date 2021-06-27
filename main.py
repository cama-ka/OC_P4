from turn import Tournaments
from player import Player
from round import Round, Round1
from match import Match



def infos_tournoi():
    turn = Tournaments(input("Nom du tournois : "),input("Lieu du tournois : "),\
            input("Date du tournois : "),input("Nombre de tour du tournois : "),\
            input("Timing du tournois : "),input("Description du tournois : "))
     
    return turn.info_turn()
    
def infos_joueur():
    joueur = Player(input("Nom du joueur : "), input("Prénom : "),\
                input("Date : "), input("Sexe : "), input("Classement : "))
     
    return joueur.info_liste()
    
def ajout_joueur(liste, func):
        """ Permet à l'utilisateur d'entrer de nouveaux joueurs """ 
        while True:
            try :
                reponse = input(f"Souhaitez-vous ajouter un nouveau joueur ? ").capitalize()
                if reponse == "Yes" or reponse == "Oui":
                    joueur = func()
                    liste.append(joueur)
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

def main():           
    liste_joueur = []
    liste_test = [("karla",1001),("Paco",1001),("fav", 500), ("soraya",800),("karlota",1001),("Paquito",1001),("favio", 510), ("Thoraya",830)]
    groupe1 = []
    groupe2 = []
    # ajout_joueur(liste_joueur, infos_joueur)
    
    round1 = Round1(liste_test,1, groupe1,groupe2)
    
    round1.creer_deux_groupes(groupe1, groupe2, liste_test)
    round1.creer_paire_1(groupe1, groupe2)
    round1.creer_paire_2(groupe1, groupe2)
    round1.creer_paire_3(groupe1, groupe2)
    round1.creer_paire_4(groupe1, groupe2)
    
    round1.lancer_tour1()
            
if __name__ == "__main__":
    main()