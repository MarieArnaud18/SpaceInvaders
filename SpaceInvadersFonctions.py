from tkinter import *
DXA = 1.5
DYA = 0
j = 0
i = -1
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
        self.vaisseau = None
        self.alientag = self.jeu.create_oval (x-rayonA, y-rayonA, x+rayonA, y+rayonA, outline = 'black', fill = 'pink')
        self.vivant = True
    
    def deplacement ( self, rayonA):
        [x1, y1, x2, y2] = self.jeu.bbox(self.alientag)
        global DXA,DYA,j,i
        if x2 > 1000 :
            DXA = -1.5
        if x1 < 0 :
            j += 1
            print (i,j,'premier')
            DXA = 1.5
            if i != j :
                i +=1
                DYA = 175/6
                print(i,j,'second')
            if i == j :
                DYA = 0

        self.jeu.move (self.alientag, DXA, DYA) 
        self.fenetre.after ( 20, lambda : self.deplacement( rayonA))



def PositionsInit ( largeur, hauteur, X, Y, jeu, fenetre, rayonA):
    distancehorizontale = largeur/7
    distanceverticale = hauteur/(3*4)
    n = 0
    A_liste = []
    for i in range (1,7):
        for j in range (1,4):
            X.append (i*distancehorizontale)
            Y.append (j*distanceverticale)
            A_liste.append(Alien(X[n], Y[n], False, n, jeu, fenetre, rayonA, 0))
            
            n = n+1
    return(X,Y, A_liste)



class Vaisseau:
    def __init__(self, jeu, fenetre, rayonV, rayonM, A_liste):
        self.jeu = jeu
        self.fenetre = fenetre
        self.rayonV = rayonV
        self.PositionInitV(rayonV)
        self.rayonM = rayonM
        self.A_liste = A_liste

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
        if y1 < 0:
            self.jeu.delete(M)
            print(M)
            return
        liste = self.jeu.find_overlapping (x1, y1, x2, y2)
        print(liste)
        for i in liste : 
            print(i)
            print(self.jeu.find_withtag (M))
            if i != 19 and i != self.jeu.find_withtag (M)[0] :
                print ("Hello")  
                self.jeu.delete(i)
                self.jeu.delete(self.jeu.find_withtag (M)[0])
        else:
            self.jeu.move (M, 0, DYM) 
        self.fenetre.after (20, lambda : self.DeplacementMissile( DYM, M))