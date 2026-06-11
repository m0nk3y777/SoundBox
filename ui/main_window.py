import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
screen.fill("gray")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    myfont = pygame.font.SysFont("monospace", 32)
    label = myfont.render("SoundBox", 1, (0,0,0))
    
    posX = 100
    posY = 200
    space_row = 150
    nb_btn = 20
    nb_lignes = 3
    j= 0

    red = (200,20,30)
    
    screen.blit(label, (100, 100))

    for j in range(nb_lignes) :
        for i in range(nb_btn):
            size = (posX + i* 150, posY, 100, 100)
            pygame.draw.ellipse(screen, red, size, width = 0)
            if i > 4 :
                posX = 100
                posY += space_row
                i -= 4
                j +=1
                break
    pygame.display.flip()
    clock.tick(60) 
pygame.quit()