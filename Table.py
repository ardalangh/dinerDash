class Table:
    possible_caps = [2, 4, 6, 8]
    possible_pos = [] # to be added later
    file_path = "/assets/tableSingle.png" 


    def __init__(self, cap):
        if cap is not in Table.possible_caps:
            raise ValueError("The capacity of your table needs to in [2, 4, 6, 8]")
    
        self.cap = cap    # The cap of the table (int)
        self.empty = True # Table is empty (bool)
        self.guest_at = 0 # How many people are at this table (int)
        self.num = None   # The number of the table (int)


    def draw(self, screen):
        table = pygame.image.load(Table.file_path).convert() 
        screen.blit(table, [10,10])