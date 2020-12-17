from tkinter import *

class Alien:
    def __init__(self, x, y, canyoushot, indice, jeu, fenetre):
        self.x = x
        self.y = y
        self.canyoushot = canyoushot
        self.indice = indice
        self.jeu = jeu
        self.fenetre = fenetre
    
    def deplacement ( self, x, y, DXA, DYA, indice, jeu, fenetre):
        
        
        
        
        fenetre.after ( 50, lambda : deplacement( self, x, y, indice, jeu, fenetre))




def PositionsInit ( largeur, hauteur, X, Y, A_liste, jeu, fenetre):
    distancehorizontale = largeur/7
    distanceverticale = hauteur/(3*4)
    n = 0
    for i in range (1,7):
        for j in range (1,4):
            X.append (i*distancehorizontale)
            Y.append (j*distanceverticale)
            A_liste.append(Alien(X[n], Y[n], False, n, jeu, fenetre))
            n = n+1
    return(X,Y, A_liste)
