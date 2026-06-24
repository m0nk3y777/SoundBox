import pygame
from data.config_manager import LARGEUR,HAUTEUR,BLUE,RED,WHITE,ORANGE,GREEN,COLORS



def showMenu(screen) : 
    font = pygame.font.SysFont("book antiqua",48)
    text = font.render("S0undB0x Project V0.1", 1,WHITE)
    textpos = text.get_rect()
    textpos = textpos.center
    screen.blit(text, textpos)

    soundBtn = pygame.draw.rect(screen, ORANGE, (LARGEUR/6 ,HAUTEUR/6 ,80,80),border_radius = 35)
    fontBtn = pygame.font.SysFont("book antiqua", 12, bold=True)
    textSound = fontBtn.render("Sound",1,WHITE)
    textSoundPos = textSound.get_rect()
    textSoundPos.center = soundBtn.center
    screen.blit(textSound,textSoundPos)

    pygame.display.flip()