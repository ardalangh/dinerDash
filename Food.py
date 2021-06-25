import pygame


class Food:
    path_to_assets = "assets/foodKit/Isometric/"

    def __init__(self, name):
        self.name = name
        self.img_path = Food.path_to_assets + self.name + ".png"
        self.img_loaded = pygame.image.load(self.img_path)
        assert self.img_loaded is not None
        self.img_loaded = pygame.transform.scale(self.img_loaded, (50, 50))


    def draw_on_table(self, screen, table, pos):
        if (pos == "left"):
            screen.blit(self.img_loaded, [table.table_rect.x, table.table_rect.y])
        elif (pos == "right"):
            screen.blit(self.img_loaded, [table.table_rect.x + 50, table.table_rect.y])