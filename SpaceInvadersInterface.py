from tkinter import *
import SpaceInvadersFonctions as SIF

score = 1000
largeur = 1000
hauteur = 700
X = []
Y = []
rayonA = 15
rayonV = 30
rayonM = 5
DXV = 8
DYM = -8

Mafenetre = Tk()
Mafenetre.title('Space invaders')
Mafenetre.geometry('1200x800+100+50')

Boutons = Frame(Mafenetre, width = 100, height = 700)
Boutons.pack (side = 'left', padx = 5, pady = 5)

BoutonQuitter = Button (Boutons, text = 'Quitter', command = Mafenetre.destroy, relief = 'groove')
BoutonQuitter.pack (side = 'bottom', padx = 5, pady = 10)

scoretk = IntVar ()
scoreaffiche = Label(Boutons, textvariable = scoretk, bg = 'black', fg = 'yellow')
scoreaffiche.pack (side = 'top', padx = 5, pady = 10)
scoretk.set(score)

BoutonLancer = Button (Boutons, text = 'Commencer', command = lambda:fonctioncommencer(), relief = 'groove')
BoutonLancer.pack (side = 'top', padx = 5, pady = 10)

MenuBar = Menu (Mafenetre)
Apropos = Menu (MenuBar, tearoff = 0 )
Apropos.add_command (label = 'Quitter', command = Mafenetre.destroy)
MenuBar.add_cascade (label = 'A propos', menu = Apropos)

Mafenetre.config (menu = MenuBar)

Jeu = Canvas (Mafenetre, width = largeur, height = hauteur, bg = 'white')
Jeu.pack (side = 'right', padx = 50, pady = 5)


X,Y,A_liste = SIF.PositionsInit (largeur, hauteur, X, Y, Jeu, Mafenetre, rayonA)


for a in A_liste:
    a.deplacement( rayonA)
V = SIF.Vaisseau (Jeu, Mafenetre, rayonV, rayonM, A_liste)
Jeu.bind("<Key>", lambda event: V.deplacement(DXV, DYM, event))
Jeu.focus_set()



Mafenetre.mainloop()
