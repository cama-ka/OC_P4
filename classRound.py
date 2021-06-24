class Round:
    ''' classe d'un round '''
    def __init__(self):
        
        self.joueur_choisi_1 = None
        self.joueur_choisi_2 = None
        self.result_1 = None
        self.result_2 = None
        
    def choose_player_1(self, joueur_choisi_1):
        self.joueur_choisi_1 = joueur_choisi_1
        
    def has_choose_player_1(self):
        return self.joueur_choisi_1 is not None
            
    def get_player_1(self):
        return self.joueur_choisi_1
        
    def choose_player_2(self, joueur_choisi_2):
        self.joueur_choisi_2 = joueur_choisi_2
    
    def has_choose_player_2(self):
        return self.joueur_choisi_2 is not None
        
    def get_player_2(self):
        return self.joueur_choisi_2
        
    def start_round(self):
        if self.joueur_choisi_1 and self.joueur_choisi_2:
            print(f"{self.joueur_choisi_1} joue contre {self.joueur_choisi_2}.")
        elif self.joueur_choisi_1:
            print(f"Ou est le {joueur_choisi_2} ?")
        else:
            print("Veuillez choisir des joueurs.")
            
    def get_result_1(self, result_1):
        self.result_1 = result_1
        
    def has_result(self):
        return self.result is not None
        
        
    def get_result_2(self, result_2):
        self.result_2 = result_2
        
    def has_result_2(self):
        return self.result_2 is not None
           
    def enter_result(self):
        self.result_1 = input(f"Entrez le résultat de {self.get_player_1()} > ")
        print(self.result_1)
        self.result_2 = input(f"Entrez le résultat de {self.get_player_2()} > ")
        print(self.result_2)
       