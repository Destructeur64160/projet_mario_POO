'''
Programme de base de Mario.
Il n'utilise pas les classes de python, ce qui compliquera l'écriture du
programme avec l'ajout de personnages.
'''
import pygame
from pygame.locals import *
from B_sprites import *
pygame.init()

index = 0
xp = 50
yp = 296
deplt = 10
sens = "droite"

continuer = True
'''
Boucle principale (évenement) du jeu. Elle s'exécute tant que Quit
n'est pas cliqué (dans ce cas la variable continuer = False)
'''
while continuer:
    #détection des événements de type clavier notamment
    for event in pygame.event.get():
        if event.type == QUIT :
            continuer = False
        if event.type == KEYDOWN :
            if event.key == K_RIGHT :
                sens = "droite"
                xp = xp + deplt
                index = (index + 1) % 6
            if event.key == K_LEFT :
                sens = "gauche"

            if event.key== K_UP :
                yp = yp
        else:       # Mario a l'arrêt
            if sens == "droite" :
                index = 12
            else:
                index = 13

    pygame.time.Clock().tick(10)
    #réaffichage de la fenêtre
    fenetre.blit(fond,(0,0))
    fenetre.blit(mario_sprite[index],(xp,yp))
    pygame.display.flip()

#Fermeture de  pygame
pygame.quit()