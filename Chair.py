import pygame


class Chair:
    def __init__(self, table, facing):
        self.table = table  # table instance that this chair is around
        self.facing = facing  # facing = -1  means Right facing = 1 means left
        self.taken = False  # no one sitting on the table

        self.y = table.getPossiblePos()[table.id][1]

        if self.facing == 1:
            self.x = table.getPossiblePos()[table.id][0] + 122
        else:
            self.x = table.getPossiblePos()[table.id][0] + (self.facing * 100)

        if self.facing == 1:
            self.filePath = "./assets/chairL.png"
        elif self.facing == -1:
            self.filePath = "./assets/chairR.png"
        else:
            raise RuntimeError("Chair must face left or right")

        self.chair_loaded = pygame.image.load(self.filePath).convert_alpha()
        self.chair_rect = self.chair_loaded.get_rect()
        self.chair_rect.x, self.chair_rect.y = self.x, self.y
        self.debug = True

    def draw(self, screen):
        if self.debug:
            pygame.draw.rect(screen, (0, 0, 0), self.chair_rect, 3)
        screen.blit(self.chair_loaded, [self.x, self.y])
