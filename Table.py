import pygame

from Chair import Chair


class Table:
    possible_caps = [2, 4, 6, 8]
    ratio_map = [(0.4, 0.4),
                    (0.8, 0.4),
                    (0.8, 0.7),
                    (0.4, 0.7)]
    file_path = "./assets/table.png"

    def __init__(self, cap, idNum):


        self.pos =  [0, 0]
        self.id = idNum
        if cap not in Table.possible_caps:
            raise ValueError("The capacity of your table needs to in [2, 4, 6, 8]")

        self.cap = cap        # The cap of the table (int)
        self.empty = True     # Table is empty (bool)
        self.guest_at = 0     # How many people are at this table (int)
        self.num = None       # The number of the table (int)
        # self.chairs = [Chair(self, -1), Chair(self, 1)]  # list of all the chairs around the instance of the table class
        self.table_loaded = pygame.image.load(Table.file_path).convert_alpha()
        self.table_rect = self.table_loaded.get_rect()

        self.debug = True


    def calculate_pos(self, size):
        self.pos = [Table.ratio_map[self.id][0] * size[0], Table.ratio_map[self.id][1] * size[1]]
        self.table_rect.x, self.table_rect.y = self.pos


    # def getPossiblePos(self):
    #     return Table.possible_pos

    def draw(self, screen):
        # for chair in self.chairs:
        #     chair.draw(screen)


        if self.debug:
            pygame.draw.rect(screen, (0, 0, 0), self.table_rect, 3)
        screen.blit(self.table_loaded, self.pos)
        # pygame.draw.circle(screen, (0,0,0), Table.possible_pos[self.id], 10 )

    def initChairs(self):
        self.chairs.append(Chair(self.determineLeftChairPos()[0],
                                  self.determineLeftChairPos()[1],
                                  self,
                                  0))

    def determineLeftChairPos(self):
        return self.x - 10, self.y
