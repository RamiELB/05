

class Bataille ():
    def __init__(self , grilleAlea):
        self.grilleAlea=grilleAlea
    
    
    def joue(self,position): 
        """Joue un coup dans les coordonnées du tuple position, si ça touche on rend true 
            sinon false
        """
        i,j = position
        if self.grilleAlea.tab[i][j] > 0 :
            self.grilleAlea.tab[i][j] = 0 # On a coulé la case
            return True
        # rien touché
        return False
        

    def victoire(self):
        """
        Rend true si tt les bateaux sont coulés, false s'il en reste des bateaux a detruire
        """
        ListeCoordBateau= self.grilleAlea.trouver_coord()
        for (i,j) in ListeCoordBateau :
            if self.grilleAlea(i,j) == 0:
                continue
            else:
                return False
        return True
    #def reset (self):
