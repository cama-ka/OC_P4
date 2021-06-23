from classPlayer import Player

class Match(Player):
    ''' classe d'un match '''
    def __init__(self, nom, prenom, date, sexe, classement, numero_match):
        Player.__init__(self, nom, prenom, date, sexe, classement)
        self.numero = numero_match
        joueur_choisi = None
        
    def choose_player(self, joueur_choisi):
        self.joueur_choisi = joueur_choisi
    
    def has_choose_player(self):
        return self.joueur_choisi is not None
    

        