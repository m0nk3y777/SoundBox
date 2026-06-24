import pygame
from data.config_manager import LARGEUR,HAUTEUR,BLUE,RED,WHITE,ORANGE,GREEN,COLORS,TITLE



def showMenu(screen) : 
    font = pygame.font.SysFont("book antiqua",48)
    text = font.render(TITLE, 1,WHITE)
    textpos = text.get_rect()
    textpos = textpos.center
    screen.blit(text, textpos)

    soundBtn = pygame.draw.rect(screen, ORANGE, (LARGEUR/6 ,HAUTEUR/6 ,80,80),border_radius = 35)
    fontBtn = pygame.font.SysFont("book antiqua", 12, bold=True)
    textSound = fontBtn.render("Sound",1,WHITE)
    textSoundPos = textSound.get_rect()
    textSoundPos.center = soundBtn.center
    screen.blit(textSound,textSoundPos)

    mouse = pygame.mouse.get_pos()

    if soundBtn.collidepoint(mouse) :
        playBtn = pygame.draw.rect(screen, GREEN, (LARGEUR/6 ,HAUTEUR/6 ,80,80),border_radius = 35)
        playBtnBorder = pygame.draw.rect(screen, BLUE,  (LARGEUR/6 ,HAUTEUR/6 ,80,80),border_radius = 35,width = 2)
        screen.blit(textSound,textSoundPos)

    pygame.display.flip()