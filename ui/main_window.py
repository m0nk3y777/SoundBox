import pygame
from data.config_manager import LARGEUR,HAUTEUR,BLUE,RED,WHITE,ORANGE,GREEN,PURPLE,COLORS,TITLE,NB_COLS
from data.file_loader import soundImporter
from ui.sound_button import playSound


def showMenu(screen,mouse,soundWbutton) : 
    click = pygame.mouse.get_pressed()
    font = pygame.font.SysFont("book antiqua",48)
    text = font.render(TITLE, 1,WHITE)
    textpos = text.get_rect()
    textpos = textpos.center
    screen.blit(text, textpos)

    X1 = LARGEUR/6
    Y1 = HAUTEUR/6
    SPACEX = 0
    SPACEY = 0

    for i in range (0,len(soundWbutton)) :
        soundBtn = pygame.draw.rect(screen, ORANGE, (X1+SPACEX , Y1+SPACEY ,80 ,80),border_radius = 35)
        fontBtn = pygame.font.SysFont("book antiqua", 12, bold=True)
        textSound = fontBtn.render("Sound",1,WHITE)
        textSoundPos = textSound.get_rect()
        textSoundPos.center = soundBtn.center
        screen.blit(textSound,textSoundPos)
        
        if soundBtn.collidepoint(mouse) :
            playBtn = pygame.draw.rect(screen, GREEN, (X1+SPACEX ,Y1+SPACEY ,80 ,80),border_radius = 35)
            playBtnBorder = pygame.draw.rect(screen, BLUE,  (X1+SPACEX ,Y1+SPACEY ,80 ,80),border_radius = 35, width = 2)

            if click[0] == True :
                playSound(soundWbutton,i)
            screen.blit(textSound,textSoundPos)
        SPACEX += LARGEUR/5

        if (i+1) % (NB_COLS) == 0 :
            SPACEX = 0
            SPACEY += 100            
    

    pygame.display.flip()
    

def addSound(screen,mouse,soundWbutton) : 

    click = pygame.mouse.get_pressed()
    n_id = len(soundWbutton)

    soundAddBtn = pygame.draw.rect(screen, GREEN, ((LARGEUR-100 ) ,(HAUTEUR-100) ,40 ,40),border_radius = 20)
    font = pygame.font.SysFont("Arial" ,32)
    text = font.render("+", 1 ,WHITE)
    textpos = text.get_rect()
    textpos.center = soundAddBtn.center
    screen.blit(text, textpos)

    

    if soundAddBtn.collidepoint(mouse) :
            soundAddBtnBorder = pygame.draw.rect(screen, BLUE,  ((LARGEUR-100 ) ,(HAUTEUR-100) ,40 ,40),border_radius = 20, width= 2)
            screen.blit(text, textpos)
            if click[0] == True and len(soundWbutton) < 20 :
                filename = soundImporter()
                if filename != "" :
                    soundWbutton [n_id] = filename
                    print (soundWbutton)
                    return soundWbutton
    return soundWbutton

    pygame.display.flip()

def deleteSound(screen,mouse,soundWbutton) : 
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

def stopBtn(screen,mouse,soundWbutton) : 
    click = pygame.mouse.get_pressed()
    stopBtn = pygame.draw.rect(screen, PURPLE,  ((LARGEUR-100 ) ,(HAUTEUR-50) ,40 ,40))
    if stopBtn.collidepoint(mouse) :
            stopBtnBorder = pygame.draw.rect(screen, BLUE,  ((LARGEUR-100 ) ,(HAUTEUR-50) ,40 ,40),width = 2)
    if stopBtn.collidepoint(mouse) and click[0] == True :
        pygame.mixer.stop()
    pygame.display.flip()
