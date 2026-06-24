import pygame
from data.config_manager import LARGEUR,HAUTEUR,BLUE,RED,WHITE,ORANGE,GREEN,COLORS,TITLE,NB_COLS

def showMenu(screen,mouse,nb_buttons) : 
    font = pygame.font.SysFont("book antiqua",48)
    text = font.render(TITLE, 1,WHITE)
    textpos = text.get_rect()
    textpos = textpos.center
    screen.blit(text, textpos)

    X1 = LARGEUR/6
    Y1 = HAUTEUR/6
    SPACEX = 0
    SPACEY = 0

    for i in range (0,nb_buttons) :
        soundBtn = pygame.draw.rect(screen, ORANGE, (X1+SPACEX , Y1 ,80 ,80),border_radius = 35)
        fontBtn = pygame.font.SysFont("book antiqua", 12, bold=True)
        textSound = fontBtn.render("Sound",1,WHITE)
        textSoundPos = textSound.get_rect()
        textSoundPos.center = soundBtn.center
        screen.blit(textSound,textSoundPos)
        
        if soundBtn.collidepoint(mouse) :
            playBtn = pygame.draw.rect(screen, GREEN, (X1+SPACEX ,Y1 ,80 ,80),border_radius = 35)
            playBtnBorder = pygame.draw.rect(screen, BLUE,  (X1+SPACEX ,Y1 ,80 ,80),border_radius = 35, width = 2)
            screen.blit(textSound,textSoundPos)
        SPACEX += LARGEUR/5

        if nb_buttons == 5 :
            SPACEX = 0
            Y1 = HAUTEUR/6 + 100
            nb_buttons = 0
            return nb_buttons

    pygame.display.flip()
    

def addSound(screen,mouse,nb_buttons) : 

    click = pygame.mouse.get_pressed()

    soundAddBtn = pygame.draw.rect(screen, GREEN, ((LARGEUR-100 ) ,(HAUTEUR-100) ,40 ,40),border_radius = 20)
    font = pygame.font.SysFont("Arial" ,32)
    text = font.render("+", 1 ,WHITE)
    textpos = text.get_rect()
    textpos.center = soundAddBtn.center
    screen.blit(text, textpos)

    if soundAddBtn.collidepoint(mouse) :
            soundAddBtnBorder = pygame.draw.rect(screen, BLUE,  ((LARGEUR-100 ) ,(HAUTEUR-100) ,40 ,40),border_radius = 20, width= 2)
            screen.blit(text, textpos)
            if click[0] == True and nb_buttons < 4 :
                nb_buttons += 1
                print (nb_buttons)
                return nb_buttons
                
    return nb_buttons

    pygame.display.flip()

def deleteSound(screen,mouse,nb_buttons) : 
    soundDelBtn = pygame.draw.rect(screen, RED, ((LARGEUR-100 ) ,(HAUTEUR-150) ,40 ,40),border_radius = 20)
    font = pygame.font.SysFont("Arial" ,32)
    text = font.render("-", 1 ,WHITE)
    textpos = text.get_rect()
    textpos.center = soundDelBtn.center
    screen.blit(text, textpos)

    if soundDelBtn.collidepoint(mouse) :
            soundAddBtnBorder = pygame.draw.rect(screen, BLUE,  ((LARGEUR-100 ) ,(HAUTEUR-150) ,40 ,40),border_radius = 20, width = 2)
            screen.blit(text, textpos)

    pygame.display.flip()