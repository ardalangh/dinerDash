import pygame

from Food import Food
from Player import Player
from Table import Table


pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Dinar Dash")



size = (screen.get_width(), screen.get_height())


running = True 

clock = pygame.time.Clock()

# bg = pygame.image.load("./assets/bg.jpeg").convert()

player = Player(testing=False)

tables = [Table(2, 0), Table(2, 1), Table(2, 2), Table(2, 3)]
[t.calculate_pos(size) for t in tables]




kitchen = pygame.image.load("assets/kitchen.png").convert_alpha()

food = Food("plate_NE")














obstacles = []
for t in tables:
    obstacles.append(t.table_rect)
    # for c in t.chairs:
    #     obstacles.append(c.chair_rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            player.moveTo(mouse_pos)



    player.update(obstacles)
    # screen.blit(bg, [0,0])

    screen.fill((254,235,202,255))
    [t.draw(screen) for t in tables]
    food.draw_on_table(screen, tables[0])
    # screen.blit(kitchen, (0, size[1]//4))
    player.draw(screen)











    # pygame.d
    pygame.display.flip()
    clock.tick(60)

pygame.quit()