import pygame


screen_width = 1280
screen_height = 720

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")

    myfont = pygame.font.SysFont("monospace", 24)
    label = myfont.render("SoundBox", 1, (0,0,0))
    label2 = myfont.render("- By Tar0saku & M0nkey", 1, (0,0,0))
    
    posX = 100
    posY = 200
    space_row = 150
    nb_btn = 20
    nb_lignes = 3
    j= 0

    red = (200,20,30)
    black = (0,0,0)
    
    label_rect = label.get_rect(center=(screen_width/2, 50))
    label2_rect = label.get_rect(center=((screen_width/2) - 150 , 100))
    screen.blit(label, label_rect)
    screen.blit(label2, label2_rect)

    for j in range(nb_lignes) :
        for i in range(nb_btn):
            size = ((screen_width - 850) / 2 + i* 150, posY, 100, 100)
            pygame.draw.ellipse(screen, red, size, width = 0)
            pygame.draw.ellipse(screen, black, size, width = 3)

            if i > 4 :
                posX = 100
                posY += space_row
                i -= 4
                j +=1
                break
                
    pygame.display.flip()
    clock.tick(60) 
pygame.quit()