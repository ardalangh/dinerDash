class Chair:
    def __init__(self, x, y, table, facing):
        self.x = x            # x cor
        self.y = y            # y cor
        self.table = table    # table instance that this chair is around
        self.facing = facing  # facing = 0 means left facing = 1 means left
        self.taken = False    # no one sitting on the table

        if self.facing == 0:
            self.filePath = "./assets/chairL.png"
        elif self.facing == 1:
            self.filePath = "./assets/chairR.png"
        else:
            raise RuntimeError("Chair must face left or right")

        