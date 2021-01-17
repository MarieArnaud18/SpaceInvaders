from tkinter import *

DXA = 1.5  # initialisation des paramètres globaux
DYA = 20
arretdujeu = False
aliendetruit = 0

class Alien:  # création de la classe Alien
    def __init__(self, x, y, canyoushot, indice, jeu, fenetre, rayonA, alientag):
        self.x = x
        self.y = y
        self.canyoushot = canyoushot # paramêtre aléatoire qui devait servir à déterminer si l'alien était autorisé à tirer (pas développé)
        self.indice = indice
        self.jeu = jeu
        self.fenetre = fenetre
        self.rayonA = rayonA
        self.alientag = alientag
        self.vaisseau = None
        self.alientag = self.jeu.create_oval (x-rayonA, y-rayonA, x+rayonA, y+rayonA, outline = 'black', fill = 'pink') # dessin de l'alien sur le canvas et récupération de son identifiant
    
    def deplacement_horizontal ( self):  # fonction permettant le déplacement horizontal des aliens
        [x1, y1, x2, y2] = self.jeu.bbox(self.alientag) # récupération des coordonnées de l'alien 
        global DXA, arretdujeu
        if x2 > 1000 : # condition de contact sur le bord droit du canvas
            DXA = -1.5
        if x1 < 0 : # condition de contact sur le bord gauche du canvas
            DXA = 1.5
        self.jeu.move (self.alientag, DXA, 0) # déclenche le déplacement de l'alien 
        if not arretdujeu :  # condition de non arrêt du jeu 
            self.fenetre.after ( 29, lambda : self.deplacement_horizontal()) # bouclage de la fonction sur un temps 


    def deplacement_vertical (self, hauteur, largeur, defaite, Defaite): # fonction permettant le déplacement vertical des aliens
        global DYA, arretdujeu
        [x1, y1, x2, y2] = self.jeu.bbox(self.alientag)
        if x1 < 0 : 
            liste_y1 = self.jeu.find_overlapping (x1, y1, x2, y1+(2/12)*hauteur+self.rayonA) # récupère la liste des identifiants des éléments se situant dans le rectangle définit
            liste_y2 = self.jeu.find_overlapping (x1+(1/7)*largeur, y1, x2+(1/7)*largeur, y1+(2/12)*hauteur+self.rayonA) # idem
            liste_y3 = self.jeu.find_overlapping (x1+(2/7)*largeur, y1, x2+(2/7)*largeur, y1+(2/12)*hauteur+self.rayonA)
            liste_y4 = self.jeu.find_overlapping (x1+(3/7)*largeur, y1, x2+(3/7)*largeur, y1+(2/12)*hauteur+self.rayonA)
            liste_y5 = self.jeu.find_overlapping (x1+(4/7)*largeur, y1, x2+(4/7)*largeur, y1+(2/12)*hauteur+self.rayonA)
            liste_y6 = self.jeu.find_overlapping (x1+(5/7)*largeur, y1, x2+(5/7)*largeur, y1+(2/12)*hauteur+self.rayonA)
            liste_y = liste_y1 + liste_y2 + liste_y3 + liste_y4 + liste_y5 + liste_y6 # concaténation des listes
            for i in liste_y : 
                if i < 19: # vérifie que l'élément est un alien  
                    self.jeu.move (i, 0, DYA)
        if y2 > hauteur : # condition de défaite (les aliens touchent le bas du canvas)
            self.jeu.delete(19) # destruction du vaisseau
            Defaite.focus_set()
            defaite.set("Perdu...") # affichage du message de defaite 
            arretdujeu = True # variable permettant l'arrêt du jeu 

        if not arretdujeu:
            self.fenetre.after ( 30, lambda : self.deplacement_vertical(hauteur, largeur, defaite, Defaite))
    



def PositionsInit ( largeur, hauteur, X, Y, jeu, fenetre, rayonA): # fonction définissant la position initiale de chaque alien
    distancehorizontale = largeur/7  # définition des écarts verticaux entre aliens
    distanceverticale = hauteur/(3*4) # définition des écarts horizontaux entre aliens
    n = 0 
    A_liste = []
    for i in range (1,7): # boucle sur les colonnes d'aliens
        for j in range (1,4): # boucle sur les lignes d'aliens
            X.append (i*distancehorizontale) # definition des coordonnées des aliens 
            Y.append (j*distanceverticale)
            A_liste.append(Alien(X[n], Y[n], False, n, jeu, fenetre, rayonA, 0)) # création des objets alien et les ajoute dans la liste 
            n = n+1
    return(X,Y, A_liste)



class Vaisseau: # création de la classe Vaisseau
    def __init__(self, jeu, fenetre, rayonV, rayonM, A_liste):
        self.jeu = jeu
        self.fenetre = fenetre
        self.rayonV = rayonV
        self.PositionInitV(rayonV)
        self.rayonM = rayonM
        self.A_liste = A_liste

    def deplacement (self, DXV, DYM, event, defaite, Defaite): # fonction permettant les actions du Vaisseau en fonction du clavier
        [x1, y1, x2, y2] = self.jeu.bbox(self.vaisseautag)
        touche = event.keysym # récupère le nom de l'entrée clavier
        if touche == "d": # condition d'appui sur la touche "d"
            if x2 > 1000: # si le vaisseau touche déjà le bord droit du canvas
                DXV = 0 # pas de déplacement à droite autorisé
            else: # sinon 
                DXV = 8 # déplacement à droite autorisé
            self.jeu.move (self.vaisseautag, DXV, 0)
        if touche == "q": # condition d'appui sur la touche "q"
            if x1 < 0 : # si le vaisseau touche déjà le bord gauche du canvas
                DXV = 0
            else:
                DXV = -8
            self.jeu.move (self.vaisseautag, DXV, 0)
        if touche == "space": # condition d'appui sur la touche "espace"
            self.TireMissile (DYM, defaite, Defaite) # appel de la fonction qui permet de tirer un missile 
    
    def PositionInitV (self, rayonV): # création du vaisseau sur le canvas et récupération de son identifiant
        self.vaisseautag = self.jeu.create_oval (500-self.rayonV, 11*700/12-self.rayonV, 500+self.rayonV, 11*700/12+self.rayonV, outline = 'black', fill = 'blue') # dessin du vaisseau sur le canvas

    def TireMissile(self, DYM, defaite, Defaite): # fonction permattant de tirer un missile avec le vaisseau
        [x1, y1, x2, y2] = self.jeu.bbox(self.vaisseautag)
        x = (x1+x2)/2 # calcul de la position intiale du centre du missile définie grâce à la position du vaisseau (missile qui par du milieu supérieur du vaisseau)
        M = self.jeu.create_oval (x-self.rayonM, y1-self.rayonM, x+self.rayonM, y1+self.rayonM, outline = 'black', fill = 'blue') # dessin du missile sur le canvas
        self.DeplacementMissile (DYM, M, defaite, Defaite)

    def DeplacementMissile(self, DYM, M, defaite, Defaite): # fonction gérant les déplacements du missile 
        global arretdujeu, aliendetruit
        [x1, y1, x2, y2] = self.jeu.bbox(M)
        if y1 < 0: # si le missile atteint le bord supérieur du canvas
            self.jeu.delete(M) # suppression du missile
            return
        liste = self.jeu.find_overlapping (x1, y1, x2, y2) # récupération des identifiants des éléments touchant le missile (y compris le missile)
        for i in liste : 
            if i != 19 and i != self.jeu.find_withtag (M)[0] :  # si l'élément n'est pas le vaisseau ni le missile (donc si c'est un alien)
                self.jeu.delete(i) # suppression de l'alien touché
                self.jeu.delete(self.jeu.find_withtag (M)[0]) # suppression du missile qui a touché 
                aliendetruit += 1 # compte le nombre d'aliens détruits
        else:
            self.jeu.move (M, 0, DYM) # déplacement vertical du missile 
        if aliendetruit == 18 : # condition de victoire ( tous les aliens ont été détruits)
            arretdujeu = True
            Defaite.focus_set()
            defaite.set("Bien joué !") # affichage du message de victoire
        if not arretdujeu:
            self.fenetre.after (20, lambda : self.DeplacementMissile( DYM, M, defaite, Defaite))

