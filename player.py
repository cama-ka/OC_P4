class Player:
    ''' classe d'un joueur '''
    def __init__(self, nom, prenom, date, sexe, classement):
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.sexe = sexe
        self.classement = classement
    
    def get_nom(self):
        return self.nom
        
    def get_prenom(self):
        return self.prenom
        
    def get_date(self):
        return self.date
       
    def get_sexe(self):
        return self.sexe
    
    def get_classement(self):
        return self.classement


    def info_liste(self):
        return ((self.prenom, self.classement))
        
    def info_rapport(self):
        return (f"Information du joueur :\n{self.nom}\n{self.prenom}\n{self.date}\n{self.sexe}\n{self.classement}")
            
            
            