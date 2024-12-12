import pygame
from pygame.locals import *

pygame.init()
largeur_ecran = 640
hauteur_ecran = 360
#Définiton de la fenêtre d'affichage
fenetre = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
# Chargement des images
fond = pygame.image.load("images/background.jpg").convert()

#configuration du delais et de l'intervalle de répétition des touches
pygame.key.set_repeat(150,100)


mario_sprite_sheet = pygame.image.load("images/mario-sprite.png").convert_alpha()
# Récupération des sprite correspondant aux déplacements à droite de mario
mario_sprite=[]
#use subsurface to cut the img
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(3,98,40,50)))    #droite0
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(50,98,40,50)))   #droite1
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(96,98,40,50)))   #droite2
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(148,98,40,50)))  #droite3
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(197,98,40,50)))  #droite4
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(244,98,35,50)))  #droite5
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(242,335,35,50))) #gauche0
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(193,335,40,50))) #gauche1
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(145,335,40,50))) #gauche2
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(97,335,40,50)))  #gauche3
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(49,335,40,50)))  #gauche4
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(1,335,35,50)))   #gauche5
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(3,18,40,50)))    #arrêt droit
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(242,255,35,50))) #arrêt gauche
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(180,18,40,50)))  #shoot droit
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(66,255,40,50)))  #shoot gauche
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(3,178,40,50)))   #jump droit
mario_sprite.append(mario_sprite_sheet.subsurface(pygame.Rect(242,414,35,50))) #jump gauche


gooma_sprite_sheet = pygame.image.load("images/gooma.png").convert_alpha()
# Récupération des sprite correspondant aux déplacements à droite de gooma
gooma_sprite=[]
#use subsurface to cut the img
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(126,140,53,60))) #droite0
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(66,140,53,60)))  #droite1
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(8,140,53,60)))   #droite2
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(126,140,53,60))) #droite3
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(185,140,53,60))) #droite4
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(244,140,53,60))) #droite5
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(126,76,53,60))) #gauche0
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(66,76,53,60)))  #gauche1
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(8,76,53,60)))   #gauche2
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(126,76,53,60))) #gauche3
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(185,76,53,60))) #gauche4
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(244,76,53,60))) #gauche5
gooma_sprite.append(gooma_sprite_sheet.subsurface(pygame.Rect(126,25,53,60))) #arret


eagle_sprite_sheet = pygame.image.load("images/eagle-sprite-sheet.png").convert_alpha()
# Récupération des sprite correspondant aux déplacements à droite de eagle
eagle_sprite=[]
#use subsurface to cut the img
eagle_sprite.append(eagle_sprite_sheet.subsurface(pygame.Rect(73,83,52,34))) #droite0
eagle_sprite.append(eagle_sprite_sheet.subsurface(pygame.Rect(73,122,52,34))) #droite1
eagle_sprite.append(eagle_sprite_sheet.subsurface(pygame.Rect(73,210,52,34))) #droite2
eagle_sprite.append(eagle_sprite_sheet.subsurface(pygame.Rect(73,254,52,34))) #droite3
eagle_sprite.append(eagle_sprite_sheet.subsurface(pygame.Rect(73,340,52,34))) #droite4
eagle_sprite.append(eagle_sprite_sheet.subsurface(pygame.Rect(73,382,52,34))) #droite5

