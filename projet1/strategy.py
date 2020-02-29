import random

class Strategy(object):
    """Class strategy qui represente la strategie pr gagner en trouvant les 17cases des bateaus
    """
    def __init__(self, bataille):
        self.miss = []
        self.hits = []
        self.total = bataille.totalHp
        self.bataille = bataille

class RandomPlayer(Strategy):
    """Strat aléatoire: On commence avec 1 grille alea et chaque tour on joue un coup random
    """
    def __init__(self, bataille):
        super().__init__(bataille)
        
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
            #if(uselessCPT%5==0):
                #self.bataille.grilleAlea.affiche()
            uselessCPT+=1
        #self.bataille.grilleAlea.affiche()
        
        #Return la somme des miss et hits
        return len(self.hits) + len(self.miss)

class HeuresticPlayer(Strategy):
    """ Strat avec regles(exploiter coup precedent ) :
        1) Jouer random tant que on touche rien...
        2) Qd on touche un bateau, on explore les cases connexes 
    """
    
    
    def __init__(self, bataille):
        super().__init__(bataille)

    def joueCoup(self):
        coupsPossibles=coupsPossiblesGrille() ## LISTE DES COUPS
        NvxCoups = []
        #print("ici")
        while (len(self.hits) < self.total):
            #print("ici2")
            try : 
                coord_a_Jouer = NvxCoups.pop()
            except:
                coord_a_Jouer = random.choice(coupsPossibles)
            coupsPossibles.remove(coord_a_Jouer) # enleve ce coup de la liste
            
            if (self.bataille.joue(coord_a_Jouer)) == True :
                self.hits.append(coord_a_Jouer)
                NvxCoups = casesConnexes(self.bataille.grilleAlea, coord_a_Jouer)
                NvxCoups = [i for i in NvxCoups if i in coupsPossibles]

            else:
                self.miss.append(coord_a_Jouer)                                          
                
        return len(self.hits)+len(self.miss)

def coupsPossiblesGrille():
    """FCT auxiliaire pr generer les coups possibles sous forme de liste:
    """
    coupsPossibles=[]
    for i in range(10):
            for j in range (10):
                coupsPossibles.append( (i,j) )
    return coupsPossibles

def casesConnexes(grille, position):
    taille = len(grille.tab)
    i,j = position
    list_coord_i = [i-1,i+1]
    list_coord_j = [j-1,j+1]
    [list_coord_i.remove(i) for i in list_coord_i if i>taille-1 or i < 0]
    [list_coord_j.remove(j) for j in list_coord_j if j>taille-1 or j < 0]
    return [(i2,j) for i2 in list_coord_i] + [(i,j2) for j2 in list_coord_j]

    