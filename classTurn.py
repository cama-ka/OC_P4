from classPlayer import Player

class Tournaments:
    ''' class d'un tournois '''
    def __init__(self, nom, lieu, date, nombre_de_tour, time, description):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nombre_de_tour = nombre_de_tour
        self.joueur = None
        self.time = time
        self.description =  description
        
        
    def get_nom(self):
        return self.nom
        
    def get_lieu(self):
        return self.lieu
        
    def get_date(self):
        return self.date
       
    def get_nombre_de_tour(self):
        return self.nombre_de_tour
    
    def get_joueur(self, joueur):
        self.joueur = joueur
    
    def has_joueur(self):
        return self.joueur is not None
        
    def get_time_control(self):
        return self.time_control
        
    def get_description(self):
        return self.description
        
    def info_turn(self):
        return (f" Informations du tournois : \n{self.nom}\n {self.lieu}\n{self.date}\n{self.nombre_de_tour}\n{self.time}\n{self.description}\n\n")
            
     
