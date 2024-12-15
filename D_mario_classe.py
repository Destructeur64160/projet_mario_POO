'''
Programme de base de Mario.
Il n'utilise pas les classes de python, ce qui compliquera l'écriture du
programme avec l'ajout de personnages.
'''
import pygame
from pygame.locals import *
from B_sprites import *
from D_classes import *
pygame.init()

index = 0
xp = 50
yp = 296
deplt = 10
sens = "droite"
sens_eagle="droite"

continuer = True
'''
Boucle principale (évenement) du jeu. Elle s'exécute tant que Quit
n'est pas cliqué (dans ce cas la variable continuer = False)
'''
mario=Mario(mario_sprite,xp,yp,deplt)
gomma=Personnage(gooma_sprite,600,296,deplt-5)
eagle1=Personnage(eagle_sprite,0,30,deplt+5)
eagle2=Personnage(eagle_sprite,-200,30,deplt+2)
while continuer:
    #détection des événements de type clavier notamment
    for event in pygame.event.get():
        if event.type == QUIT :
            continuer = False
        if event.type == KEYDOWN :
            if event.key == K_RIGHT :
                sens = "droite"
                image_mario=mario.deplacer_droite()
            elif event.key == K_LEFT :
                sens = "gauche"
                image_mario=mario.deplacer_gauche()
            elif event.key == K_SPACE:  # Détection de la touche '2'
                image_mario = mario.saute()
        else:       # Mario a l'arrêt
            if sens == "droite" :
                image_mario=mario.stop()
            else:
                image_mario=mario.stop()
    if mario.xp-gomma.xp>0:
        image_gomma=gomma.deplacer_droite()
    elif mario.xp-gomma.xp<0:
        image_gomma=gomma.deplacer_gauche()
    if eagle1.xp<=650:
        image_eagle1=eagle1.deplacer_droite()
    else:
        eagle1.xp=0
    if eagle2.xp<=650:
        image_eagle2=eagle2.deplacer_droite()
    else:
        eagle2.xp=0
    # Gestion du saut de Mario
    if mario.is_jumping:
        # Déplacement vertical
        mario.yp += mario.jump_velocity  # Déplace Mario verticalement
        mario.jump_velocity += 2  # Simule la gravité

        # Pendant le saut, maintenir l'image de saut
        if mario.sens == "droite":
            image_mario = mario.sprites[16]  # Sprite de saut à droite
        else:
            image_mario = mario.sprites[17]  # Sprite de saut à gauche

        # Fin du saut (Mario touche le sol)
        if mario.yp >= 296:
            mario.yp = 296  # Mario revient au sol
            mario.is_jumping = False  # Le saut est terminé
            mario.jump_velocity = 0
            image_mario = mario.stop()  # Retour à l'image de repos




    pygame.time.Clock().tick(10)
    #réaffichage de la fenêtre
    fenetre.blit(fond,(0,0))
    fenetre.blit(image_mario,(mario.xp,mario.yp))
    fenetre.blit(image_gomma,(gomma.xp,gomma.yp))
    fenetre.blit(image_eagle1,(eagle1.xp,eagle1.yp))
    fenetre.blit(image_eagle2,(eagle2.xp,eagle2.yp))

    pygame.display.flip()

#Fermeture de  pygame
pygame.quit()
