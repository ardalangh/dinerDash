import pygame 
class Table:
    possible_caps = [2, 4, 6, 8]
    possible_pos = [(400, 400),
                    (900, 400),
                    (900, 700),
                    (400, 700)]
    file_path = "./assets/table.PNG"


    def __init__(self, cap, id):
        self.id = id
        if cap not in Table.possible_caps:
            raise ValueError("The capacity of your table needs to in [2, 4, 6, 8]")
    
        self.cap = cap    # The cap of the table (int)
        self.empty = True # Table is empty (bool)
        self.guest_at = 0 # How many people are at this table (int)
        self.num = None   # The number of the table (int)
        self.chairs = []  # list of all the chairs around the instance of the table class














    def draw(self, screen):
        table = pygame.image.load(Table.file_path).convert()
        screen.blit(table, Table.possible_pos[self.id])