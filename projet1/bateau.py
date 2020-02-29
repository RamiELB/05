class bateau():
    def __init__(self, taille, type_bat):
        self.taille = taille
        self.type_bat = type_bat

    def getTaille(self):
        return self.taille
    
    def placer(self, coord, index):
        self.hp = self.taille
        self.coord = coord # liste des cases du bateaux
        self.index = index # index du bateau dans la liste de la grille
        
    def toucher(self, position):
        self.hp -= 1
        self.coord.remove(position)
            
    def isDead(self):
        return self.hp == 0