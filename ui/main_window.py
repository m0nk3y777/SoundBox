import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    myfont = pygame.font.SysFont("monospace", 32)
    label = myfont.render("SoundBox", 1, (0,0,0))
    
    posX = 100
    posY = 200
    nbbtn = 20
    size = (100,50, 100, 100)
    red = (200,20,30)
    j= 0
    screen.fill("gray")
    screen.blit(label, (100, 100))

    while (j < 3) :
        for i in range(nbbtn):
            size = (posX + i* 150, posY, 100, 100)
            pygame.draw.ellipse(screen, red, size, width = 0)
            if i > 4 :
                posX = 100
                posY = 350
                i = 0
                j +=1
                break

    pygame.display.flip()

    clock.tick(60) 
pygame.quit()