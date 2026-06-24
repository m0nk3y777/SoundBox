import pygame
from data.config_manager import LARGEUR,HAUTEUR,BLUE,RED,WHITE,ORANGE,GREEN,COLORS,TITLE,NB_COLS

def showMenu(screen,mouse) : 
    font = pygame.font.SysFont("book antiqua",48)
    text = font.render(TITLE, 1,WHITE)
    textpos = text.get_rect()
    textpos = textpos.center
    screen.blit(text, textpos)

    SPACEX = 0
    SPACEY = 0

    for i in range (0,NB_COLS) :
        soundBtn = pygame.draw.rect(screen, ORANGE, ((LARGEUR/6)+SPACEX ,HAUTEUR/6 ,80 ,80),border_radius = 35)
        fontBtn = pygame.font.SysFont("book antiqua", 12, bold=True)
        textSound = fontBtn.render("Sound",1,WHITE)
        textSoundPos = textSound.get_rect()
        textSoundPos.center = soundBtn.center
        screen.blit(textSound,textSoundPos)
        
        if soundBtn.collidepoint(mouse) :
            playBtn = pygame.draw.rect(screen, GREEN, ((LARGEUR/6)+SPACEX ,HAUTEUR/6 ,80 ,80),border_radius = 35)
            playBtnBorder = pygame.draw.rect(screen, BLUE,  ((LARGEUR/6)+SPACEX ,HAUTEUR/6 ,80 ,80),border_radius = 35, width = 2)
            screen.blit(textSound,textSoundPos)
        SPACEX += LARGEUR/5

    pygame.display.flip()
    

def addSound(screen,mouse) : 
    soundAddBtn = pygame.draw.rect(screen, GREEN, ((LARGEUR-100 ) ,(HAUTEUR-100) ,40 ,40),border_radius = 20)
    font = pygame.font.SysFont("Arial" ,32)
    text = font.render("+", 1 ,WHITE)
    textpos = text.get_rect()
    textpos.center = soundAddBtn.center
    screen.blit(text, textpos)

    pygame.display.flip()

def deleteSound(screen,mouse) : 
    soundDelBtn = pygame.draw.rect(screen, RED, ((LARGEUR-100 ) ,(HAUTEUR-150) ,40 ,40),border_radius = 20)
    font = pygame.font.SysFont("Arial" ,32)
    text = font.render("-", 1 ,WHITE)
    textpos = text.get_rect()
    textpos.center = soundDelBtn.center
    screen.blit(text, textpos)

    pygame.display.flip()