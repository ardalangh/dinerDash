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

tables = [Table(2, 0), Table(2, 1), Table(2, 2), Table(2, 3)]


obstacles = []
for t in tables:
    obstacles.append(t.table_rect)
    for c in t.chairs:
        obstacles.append(c.chair_rect)

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



    [t.draw(screen) for t in tables]







    # pygame.d
    pygame.display.flip()
    clock.tick(60)
    