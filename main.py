import pygame

from Player import Player
from Table import Table


pygame.init()







size = (1520, 980)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dinar Dash")






running = True 

clock = pygame.time.Clock()

# bg = pygame.image.load("./assets/bg.jpeg").convert()

player = Player(testing=False)


tb1 = Table(2, 0)
tb2 = Table(2, 1)
tb3 = Table(2, 2)
tb4 = Table(2, 3)

obstacles = [tb1.table_rect, tb2.table_rect, tb3.table_rect, tb4.table_rect]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            player.moveTo(mouse_pos)



    player.update(obstacles)
    # screen.blit(bg, [0,0])

    screen.fill((254,235,202,255))
    player.draw(screen)



    tb1.draw(screen)
    tb2.draw(screen)
    tb3.draw(screen)
    tb4.draw(screen)







    # pygame.d
    pygame.display.flip()
    clock.tick(60)
    