import pygame


class Player:
    def __init__(self, testing):
        self.testing = testing
        self.x = 0
        self.y = 0
        self.moving = False
        self.movingTo = (None, None)
        self.dir = "RIGHT"
        self.img_counter = 0
        self.player_loaded = pygame.image.load(self.get_file_path()).convert_alpha()
        self.player_rect = self.player_loaded.get_rect()
        self.debug = True
        self.color_debug = (0, 0, 0)
        self.touching_obj = False

    def get_file_path(self):
        if self.testing:
            return f"../assets/girlWalk{self.dir}{self.img_counter}.png"
        return f"./assets/girlWalk{self.dir}{self.img_counter}.png"

    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

    def moveTo(self, mousePos):
        self.movingTo = mousePos
        self.moving = True

    def draw(self, screen):
        if self.debug:
            pygame.draw.rect(screen, self.color_debug, self.player_rect, 3)
        screen.blit(self.player_loaded, [self.x, self.y])

    def update(self, obstacles):
        if self.moving:
            move_to = self.move_helper(self.movingTo, 5)
            self.player_rect = self.player_rect.move(move_to[0], move_to[1])
            self.x, self.y = self.player_rect.x, self.player_rect.y
            if abs(self.movingTo[1] - self.y) <= 0 and abs(self.movingTo[0] - self.x) <= 0:
                self.moving = False;
            self.touching_obj = False
            for obs in obstacles:
                if obs.colliderect(self.player_rect):
                    self.touching_obj = True
            if self.touching_obj:
                self.color_debug = (255, 0, 0)
            else:
                self.color_debug = (0, 0, 0)
















    def move_helper(self, dest, vel):
        """
            TESTED
            :param dest: destination coordinate where the player should move to
            :param vel: velocity of the movement
            :returns a list indicating the change in coordinate in the next cycle

            checking X first then Y
        """
        res = [0,0]
        # check if x is not at dest
        if self.x != dest[0]:
            if self.x < dest[0]:
                res[0] = vel * 1
            else:
                res[0] = vel * -1
        # check if y is not at dest
        if self.y != dest[1]:
            if self.y < dest[1]:
                res[1] = vel * 1
            else:
                res[1] = vel * -1
        return res
