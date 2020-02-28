import random

class Strategy():
    """Class strategy qui represente la strategie pr gagner en trouvant les 17cases des bateaus
    """
    def __init__(self, total = 17):
        self.miss = []
        self.hits = []
        self.total = total

class RandomPlayer(Strategy):
    """Strat aléatoire: On commence avec 1 grille alea et chaque tour on joue un coup random
    """
    def __init__(self, bataille , total = 17):
        super(RandomPlayer,self).__init__(total)
        self.bataille = bataille #bataille contient grille aleatoire et fcts ...
        
    def joueCoup(self):
        """Joue un coup et retourne le nombre de coups ratés + coups reussis pr obtenir la victoire
        """
        uselessCPT=0
        coupsPossibles=coupsPossiblesGrille() ## LISTE DES COUPS
        #print("ici")
        while (len(self.hits) < self.total):
            #print("ici2")
            coord_a_Jouer = random.choice(coupsPossibles) # selectionne un coup aleatoire de la liste
            coupsPossibles.remove(coord_a_Jouer) # enleve ce coup de la liste
            
            if (self.bataille.joue(coord_a_Jouer)) == True :
                self.hits.append(coord_a_Jouer)
            else:
                self.miss.append(coord_a_Jouer)
                
            #Affichage de l'état de la grille
            if(uselessCPT%5==0):
                self.bataille.grilleAlea.affiche()
            uselessCPT+=1
        print("Hits",len(self.hits))
        print("Misses",len(self.miss))
        
        #Return la somme des miss et hits
        return len(self.hits) + len(self.miss)

class HeuresticPlayer(Strategy):
    """ Strat avec regles(exploiter coup precedent ) :
        1) Jouer random tant que on touche rien...
        2) Qd on touche un bateau, on explore les cases connexes 
    """
    
    
    def __init__(self, bataille , total = 17):
        super(HeuresticPlayer,self).__init__(total)
        self.bataille = bataille

    def joueCoup(self):
        return len(self.hits)+len(self.miss)

def coupsPossiblesGrille():
    """FCT auxiliaire pr generer les coups possibles sous forme de liste:
    """
    coupsPossibles=[]
    for i in range(10):
            for j in range (10):
                coupsPossibles.append( (i,j) )
    return coupsPossibles
