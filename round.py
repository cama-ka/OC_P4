
class Round:
    
    def __init__(self, liste, number):
        self.liste = liste
        self.number = number
    
    def get_liste(self):
        return self.liste
        
    def get_number(self):
        return self.number
                

class Round1(Round):
    def __init__(self, liste, number, groupe1, groupe2):
        super().__init__(liste, number)
        self.groupe1 = groupe1
        self.groupe2 = groupe2
        self.paire1 = None
        self.paire2 = None
        self.paire3 = None
        self.paire4 = None

        
    def trie(self, liste):
        """ Trie la liste  """
        self.liste.sort(key = lambda x: x[1])
        return self.liste


    def creer_deux_groupes(self, groupe1, groupe2, liste):
        """ 1. create 2 group  """
        self.trie(liste)
        for i in self.liste[:4]:
            self.groupe1.append(i)
        for i in self.liste[-4:]:
            self.groupe2.append(i)
            
            
    def creer_paire_1(self, groupe1, groupe2):
        """ 2. create pairs  """
        self.paire1 = (self.groupe1[0], self.groupe2[0])
        return self.paire1
        
    def creer_paire_2(self, groupe1, groupe2):
        self.paire2 = (self.groupe1[1], self.groupe2[1])
        return self.paire2
        
    def creer_paire_3(self, groupe1, groupe2):
        self.paire3 = (self.groupe1[2], self.groupe2[2])
        return self.paire3
        
    def creer_paire_4(self, groupe1, groupe2):
        self.paire4 = (self.groupe1[3], self.groupe2[3])
        return self.paire4
        
    def lancer_tour1(self):
        print(f"Paire 1 :{self.creer_paire_1(self.groupe1, self.groupe2)}\n Paire 2 : {self.paire2} \n, Paire 3 :{self.paire3}\n Paire 2 : {self.paire4} \n")
