from tkinter import *

class Alien:
    def __init__(self, x, y, canyoushot, indice, jeu, fenetre, rayonA, alientag):
        self.x = x
        self.y = y
        self.canyoushot = canyoushot
        self.indice = indice
        self.jeu = jeu
        self.fenetre = fenetre
        self.rayonA = rayonA
        self.alientag = alientag
    
    def deplacement ( self, DXA, DYA, rayonA, alientag):
        [x1, y1, x2, y2] = self.jeu.bbox(alientag)
        if x2 > 1000 :
            DXA = -DXA
        if x1 < 0 :
            DXA = -DXA
        self.jeu.move (alientag, DXA, 0) 
        self.fenetre.after ( 20, lambda : self.deplacement( DXA, DYA, rayonA, alientag))




def PositionsInit ( largeur, hauteur, X, Y, A_liste, jeu, fenetre, rayonA):
    distancehorizontale = largeur/7
    distanceverticale = hauteur/(3*4)
    n = 0
    for i in range (1,7):
        for j in range (1,4):
            X.append (i*distancehorizontale)
            Y.append (j*distanceverticale)
            A_liste.append(Alien(X[n], Y[n], False, n, jeu, fenetre, rayonA, 0))
            n = n+1
    return(X,Y, A_liste)



class Vaisseau:
    def __init__(self, jeu, fenetre, rayonV, rayonM):
        self.jeu = jeu
        self.fenetre = fenetre
        self.rayonV = rayonV
        self.PositionInitV(rayonV)
        self.rayonM = rayonM
        [self.x1A, self.y1A, self.x2A, self.y2A] = self.jeu.bbox(Alien.alientag)

    def deplacement (self, DXV, DYM, event):
        [x1, y1, x2, y2] = self.jeu.bbox(self.vaisseautag)
        touche = event.keysym
        if touche == "d":
            if x2 > 1000:
                DXV = 0
            else: 
                DXV = 8
            self.jeu.move (self.vaisseautag, DXV, 0)
        if touche == "q":
            if x1 < 0 :
                DXV = 0
            else: 
                DXV = -8
            self.jeu.move (self.vaisseautag, DXV, 0)
        if touche == "space": 
            self.TireMissile (DYM)
    def PositionInitV (self, rayonV):
        self.vaisseautag = self.jeu.create_oval (500-self.rayonV, 11*700/12-self.rayonV, 500+self.rayonV, 11*700/12+self.rayonV, outline = 'black', fill = 'blue')

    def TireMissile(self, DYM):
        [x1, y1, x2, y2] = self.jeu.bbox(self.vaisseautag)
        x = (x1+x2)/2
        M = self.jeu.create_oval (x-self.rayonM, y1-self.rayonM, x+self.rayonM, y1+self.rayonM, outline = 'black', fill = 'blue')
        self.DeplacementMissile (DYM, M)

    def DeplacementMissile(self, DYM, M):
        [x1, y1, x2, y2] = self.jeu.bbox(M)
        liste = self.jeu.find_overlapping (self.x1A, self.y1A, self.x2A, self.y2A)
        if y1 < 0:
            self.jeu.delete(self.fenetre, M)
        else:
            self.jeu.move (M, 0, DYM) 
        self.fenetre.after ( 20, lambda : self.DeplacementMissile( DYM, M))
        
    