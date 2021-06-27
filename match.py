from player import Player
from round import Round

class Match(Player):
    ''' classe d'un match '''
    def __init__(self, nom, prenom, date, sexe, classement, numero_match, resultats):
        Player.__init__(self, nom, prenom, date, sexe, classement)
        self.numero = numero_match
        joueur_choisi = None
        resultats = None
        
    def choose_player(self, joueur_choisi):
        self.joueur_choisi = joueur_choisi
    
    def has_choose_player(self):
        return self.joueur_choisi is not None
    
    def resultats(self, resultats):
        self.resultats = resultats
        
    def has_result(self):
        return self.resultats
    

        