# https://github.com/MarieArnaud18/SpaceInvaders


from tkinter import *
import SpaceInvadersFonctions as SIF

score = 0000    #initialisation des paramètres 
largeur = 1000
hauteur = 700
X = []
Y = []
rayonA = 15
rayonV = 30
rayonM = 5
DXV = 8
DYM = -8



Mafenetre = Tk()   # création de la fenêtre Tkinter
Mafenetre.title('Space invaders')
Mafenetre.geometry('1200x800+100+50') # taille et emplacement de la fenêtre

Boutons = Frame(Mafenetre, width = 100, height = 700) # menu avec boutons et labels à gauche de la fenêtre
Boutons.pack (side = 'left', padx = 5, pady = 5)

BoutonQuitter = Button (Boutons, text = 'Quitter', command = Mafenetre.destroy, relief = 'groove') # création du bouton quitter
BoutonQuitter.pack (side = 'bottom', padx = 5, pady = 10)
defaite = StringVar()   # création du label affichant l'issue de la partie (défaite ou victoire)
defaite.set("")
Defaite = Label(Boutons, textvariable = defaite, bg = 'white', fg = 'black', font = ('Arial', 30))
Defaite.pack (side = 'top', padx = 2, pady = 0)

scoretk = IntVar ()  # création du label affichant le score
scoreaffiche = Label(Boutons, textvariable = scoretk, bg = 'black', fg = 'yellow')
scoreaffiche.pack (side = 'top', padx = 5, pady = 10)
scoretk.set(score)

BoutonLancer = Button (Boutons, text = 'Commencer', command = lambda:fonctioncommencer(), relief = 'groove') # création du bouton de lancement du jeu (non développé)
BoutonLancer.pack (side = 'top', padx = 5, pady = 10)

MenuBar = Menu (Mafenetre)  # création du menu en haut de la fenêtre (ne contient que le bouton quitter)
Apropos = Menu (MenuBar, tearoff = 0 )
Apropos.add_command (label = 'Quitter', command = Mafenetre.destroy)
MenuBar.add_cascade (label = 'A propos', menu = Apropos)

Mafenetre.config (menu = MenuBar)

Jeu = Canvas (Mafenetre, width = largeur, height = hauteur, bg = 'white') # création du canvas (zone de jeu)
Jeu.pack (side = 'right', padx = 50, pady = 5)


X,Y,A_liste = SIF.PositionsInit (largeur, hauteur, X, Y, Jeu, Mafenetre, rayonA) # initialisation de la position des aliens


for a in A_liste:  # appel des fonctions de déplacement des aliens (vertical et horizontal)
    a.deplacement_horizontal()
    a.deplacement_vertical(hauteur, largeur, defaite, Defaite)

V = SIF.Vaisseau (Jeu, Mafenetre, rayonV, rayonM, A_liste) # création d'un objet de la classe Vaisseau 

Jeu.bind("<Key>", lambda event: V.deplacement(DXV, DYM, event, defaite, Defaite)) # interaction clavier qui déclenche les actions liées au vaisseau
Jeu.focus_set()



Mafenetre.mainloop() 
