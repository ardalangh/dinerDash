import pygame

from Chair import Chair


class Table:
    possible_caps = [2, 4, 6, 8]
    possible_pos = [(400, 400),
                    (900, 400),
                    (900, 700),
                    (400, 700)]
    file_path = "./assets/table.PNG"






    def __init__(self, cap, idNum):
        self.id = idNum
        if cap not in Table.possible_caps:
            raise ValueError("The capacity of your table needs to in [2, 4, 6, 8]")

        self.cap = cap      # The cap of the table (int)
        self.empty = True   # Table is empty (bool)
        self.guest_at = 0   # How many people are at this table (int)
        self.num = None     # The number of the table (int)
        self.chairs = [Chair(self, -1), Chair(self, 1)]    # list of all the chairs around the instance of the table class


    def getPossiblePos(self):
        return Table.possible_pos



    def draw(self, screen):
        for chair in self.chairs:
            chair.draw(screen)
        table = pygame.image.load(Table.file_path).convert()
        screen.blit(table, Table.possible_pos[self.id])

    def initChairs(self):
        self.chairs.appemnd(Chair(self.determineLeftChairPos()[0],
                                  self.determineLeftChairPos()[1],
                                  self,
                                  0))

    def determineLeftChairPos(self):
        return self.x - 10, self.y
