import pygame 
from Table import Table


pygame.init()







size = (1520, 980)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dinar Dash")






running = True 

clock = pygame.time.Clock()

bg = pygame.image.load("./assets/bg.jpeg").convert()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(bg, [0,0])
    
    tb1 = Table(2)
    tb1.draw(screen)





    pygame.display.flip()
    clock.tick(60)
    