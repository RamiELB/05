import numpy as np
import random
import matplotlib.pyplot as plt

class grille():
    def __init__(self):
        self.tab = np.zeros([10,10])
        
    def eq(self ,grilleB):
        return (np.array_equal(self.tab, grilleB.tab))
        
    def peut_placer(self, bateau, position, direction):
        """ direction : 1 pour horizontal, 2 pour vertical """
        taille = bateau.getTaille()
        i = position[0]
        j = position[1]
        if direction == 1:
            if taille + j > 10:
                return False
            while taille > 0:
                if(self.tab[i,j] != 0):
                    return False
                taille -= 1
                j += 1
                
        else :
            if taille + i > 10:
                return False
            while taille > 0:
                if(self.tab[i,j] != 0):
                    return False
                taille -= 1
                i += 1
            
        return True
    
    def affiche(self) :
        plt.imshow(self.tab)
        plt.show()
    
    def place_alea(self, bateau):
        direction = random.randint(1,2)
        position = (random.randint(0,9), random.randint(0,9))
        while(not(self.place(bateau, position, direction))) :
            direction = random.randint(1,2)
            position = (random.randint(0,9), random.randint(0,9))
        
    
    def place(self, bateau, position, direction):
        """ Renvoie True si on a placé le bateau, false sinon """
        if not(self.peut_placer(bateau, position, direction)):
            return False
        
        taille = bateau.getTaille()
        i = position[0]
        j = position[1]
        
        if direction == 1:
            while taille > 0:
                self.tab[i][j] += bateau.type_bat
                taille -= 1
                j += 1
                
        else :
            while taille > 0:
                self.tab[i][j] += bateau.type_bat
                taille -= 1
                i += 1
            
        return True
    
    def vider(self):
        for i in range(10):
            for j in range(10):
                self.tab[i][j] = 0
                
    def equals(self,g2):
        for i in range(10):
            for j in range(10):
                if (self.tab[i][j] != g2.tab[i][j]):
                    return False
        return True
    
    def equals2(self,L1):
        for coord in L1:
            (i, j) = coord[0]
            if not(self.tab[i][j] == coord[1]):
                return False
        return True
        
        
    def trouver_coord(self):
        L=[]
        for i in range(10):
            for j in range(10):
                if self.tab[i][j]!=0:
                    L.append(((i,j),self.tab[i][j]))        
        return L
    
    def enlever_bateau(self, position, direction, taille):
        i = position[0]
        j = position[1]
        if direction == 1:
            while taille > 0:
                self.tab[i][j] = 0
                taille -= 1
                j += 1
                
        if direction == 2:
            while taille > 0:
                self.tab[i][j] = 0
                taille -= 1
                i += 1
        
    
class bateau():
    def __init__(self, taille, type_bat):
        self.taille = taille
        self.type_bat = type_bat
        
    def getTaille(self):
        return self.taille
        
def genere_grille():
    g = grille()
    list_bat = []
    list_bat.append(bateau(5,1))
    list_bat.append(bateau(4,2))
    list_bat.append(bateau(3,3))
    list_bat.append(bateau(3,4))
    list_bat.append(bateau(2,5))
    [g.place_alea(i) for i in list_bat]
    return g    
    
    
    
def denombre_places_bateau(grille, bateau):
    cpt = 0
    for i in range(10):
        for j in range(10):
            if grille.peut_placer(bateau, (i,j), 1):
               cpt += 1
        
            if grille.peut_placer(bateau, (i,j), 2):
               cpt += 1
    return cpt

"""
def denombre_placer_2_bateaux():
    bateaux_différents = []
    bateaux_différents.append(bateau(5,1))    
    bateaux_différents.append(bateau(4,2))    
    bateaux_différents.append(bateau(3,3))  
    bateaux_différents.append(bateau(2,5))  
    grille_vide = grille()
    g2 = grille()
    for i in bateaux_différents:
        g2.vider()
        prob_place = denombre_places_bateau(grille_vide, i)
        g2.place_alea(i)
        for j in bateaux_différents:
            print("Taille des bateaux : {} et {}, façon de le placer : {}".format(i.getTaille(), j.getTaille(), prob_place * denombre_places_bateau(g2, j)))
"""
def denombre_placer_2_bateaux():
    bateaux_différents = []
    bateaux_différents.append(bateau(5,1))    
    bateaux_différents.append(bateau(4,2))    
    bateaux_différents.append(bateau(3,3))  
    bateaux_différents.append(bateau(2,5))
    g = grille()
    for b in bateaux_différents:
        for b2 in bateaux_différents:
            cpt = 0
            for i in range(10):
                for j in range(10):
                    if(g.place(b, (i,j), 1)):
                        cpt = cpt + denombre_places_bateau(g, b2)
                        g.enlever_bateau((i,j),1,b.taille)
            for i in range(10):
                for j in range(10):
                    if(g.place(b, (i,j), 2)):
                        cpt = cpt + denombre_places_bateau(g, b2) 
                        g.enlever_bateau((i,j),2,b.taille)
            print("Taille des bateaux : {} et {}, façon de le placer : {}".format(b.getTaille(), b2.getTaille(), cpt))
 
"""    
def denombre_placer_3_bateaux():
    bateaux_différents = []
    bateaux_différents.append(bateau(5,1))    
    bateaux_différents.append(bateau(4,2))    
    bateaux_différents.append(bateau(3,3))  
    g1 = genere_grille()
    bateaux_différents.append(bateau(2,5)) 
    grille_vide = grille()
    g2 = grille()
    for i in bateaux_différents:
        g2.vider()
        prob_place = denombre_places_bateau(grille_vide, i)
        g2.place_alea(i)
        for j in bateaux_différents:
            prob_2_place = prob_place * denombre_places_bateau(g2, j)
            g2.place_alea(j)
            for k in bateaux_différents:
                print("Taille des bateaux : {} et {} et {}, façon de le placer : {}".format(i.getTaille(), j.getTaille(), k.getTaille(), prob_2_place * denombre_places_bateau(g2, k)))
"""
       
def denombre_placer_3_bateaux():
    bateaux_différents = []
    bateaux_différents.append(bateau(5,1))    
    bateaux_différents.append(bateau(4,2))    
    bateaux_différents.append(bateau(3,3))  
    bateaux_différents.append(bateau(2,5))
    g = grille()
    for b in bateaux_différents:
        for b2 in bateaux_différents:
            for b3 in bateaux_différents:
                cpt = 0
                for i in range(10):
                    for j in range(10):
                        if(g.place(b, (i,j), 1)):                     
                            for i2 in range(10):
                                for j2 in range(10):
                                    if(g.place(b2, (i2,j2), 1)):
                                        cpt = cpt + denombre_places_bateau(g, b3) 
                                        g.enlever_bateau((i2,j2),1,b2.taille)
                            for i2 in range(10):
                                for j2 in range(10):
                                    if(g.place(b2, (i2,j2), 2)):
                                        cpt = cpt + denombre_places_bateau(g, b3) 
                                        g.enlever_bateau((i2,j2),2,b2.taille)
                            g.enlever_bateau((i,j),1,b.taille)
                            
                for i in range(10):
                    for j in range(10):
                        if(g.place(b, (i,j), 2)):                     
                            for i2 in range(10):
                                for j2 in range(10):
                                    if(g.place(b2, (i2,j2), 1)):
                                        cpt = cpt + denombre_places_bateau(g, b3) 
                                        g.enlever_bateau((i2,j2),1,b2.taille)
                            for i2 in range(10):
                                for j2 in range(10):
                                    if(g.place(b2, (i2,j2), 2)):
                                        cpt = cpt + denombre_places_bateau(g, b3) 
                                        g.enlever_bateau((i2,j2),2,b2.taille)
                            g.enlever_bateau((i,j),2,b.taille)
                            
                print("Taille des bateaux : {} et {} et {}, façon de le placer : {}".format(b.getTaille(), b2.getTaille(), b3.getTaille(), cpt))

def test():
    list_bat = []
    list_bat.append(bateau(5,1))
    list_bat.append(bateau(4,2))
    list_bat.append(bateau(3,3))
    list_bat.append(bateau(3,4))
    list_bat.append(bateau(2,5)) 
    grille_vide = grille()
    for i in list_bat:
        g2.vider()
        prob_place = denombre_places_bateau(grille_vide, i)
        g2.place_alea(i)
        for j in list_bat:
            prob_2_place = prob_place * denombre_places_bateau(g2, j)
            g2.place_alea(j)
            for k in list_bat:
                prob_3_place = prob_2_place * denombre_places_bateau(g2, k)
                g2.place_alea(k)
                for l in list_bat:
                    prob_4_place = prob_3_place * denombre_places_bateau(g2, l)
                    g2.place_alea(l)
                    for m in list_bat:
                        print("Taille des bateaux : {} et {} et {} et {} et {}, façon de le placer : {}".format(i.getTaille(), j.getTaille(), k.getTaille(), l.getTaille(), m.getTaille(), prob_4_place * denombre_places_bateau(g2, m)))
                        
                        
def trouve_bonne_grille():
    g1 = genere_grille()
    cpt = 1
    g2 = genere_grille()
    while not(g1.equals(g2)):
        g2 = genere_grille()
        cpt = cpt +1
        print(cpt)
    return cpt

def trouve_bonne_grille2():
    g1 = genere_grille()
    cpt = 1
    L = g1.trouver_coord()
    g2 = genere_grille()
    while not(g2.equals2(L)):
        g2 = genere_grille()
        cpt = cpt +1
        print(cpt)
    return cpt

denombre_placer_3_bateaux()