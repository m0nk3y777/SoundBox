import pygame
from pygame.locals import QUIT
from ui.main_window import showMenu
from data.config_manager import LARGEUR,HAUTEUR

pygame.init()
screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption("S0undb0x")
screen.fill((255,255,255))

#Charger le Background
background = pygame.image.load("assets/bgsoundbox.jpg")
background = pygame.transform.scale(background,(LARGEUR,HAUTEUR))
screen.blit(background,(0,0))

continuer = 1 
while continuer : 
    for event in pygame.event.get():
        showMenu(screen)
        if event.type == QUIT :
            continuer = 0 
    pygame.display.flip()