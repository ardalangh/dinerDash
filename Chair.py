import pygame
import Table

class Chair:
    def __init__(self, table, facing):
        self.table = table    # table instance that this chair is around
        self.facing = facing  # facing = -1  means left facing = 1 means left
        self.taken = False    # no one sitting on the table

        self.x = table.getPossiblePos()[table.id][0] + self.facing * 100
        self.y = table.getPossiblePos()[table.id][1]



        if self.facing == 1:
            self.filePath = "./assets/chairL.png"
        elif self.facing == -1:
            self.filePath = "./assets/chairR.png"
        else:
            raise RuntimeError("Chair must face left or right")


    def draw(self, screen):
        chair = pygame.image.load(self.filePath).convert()
        screen.blit(chair, [self.x, self.y])

        