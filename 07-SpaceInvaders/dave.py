import pygame


class Fighter:
    def __init__(self, screen):
        # Store the given parameters to instance variables.
        # Set   self.missiles   to the empty list.
        # Load the file  "fighter.png"  as the image
        # Set the colorkey to white (it has a white background that needs removed) using the method set_colorkey
        self.screen = screen
        self.image = pygame.image.load("fighter.png")
        self.image.set_colorkey((255, 255, 255))
        self.x = screen.get_width() / 2 - self.image.get_width() / 2
        self.y = screen.get_height() - self.image.get_height()
        self.missiles = []

    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, delta_x):
        # Move the ship!
        self.x += delta_x
        left_bound = - self.image.get_width() / 2
        right_bound = self.screen.get_width() - self.image.get_width() / 2
        if self.x < left_bound:
            self.x = left_bound
        if self.x > right_bound:
            self.x = right_bound

    def fire(self):
        # Construct a new Missile self.image.get_width() / 2 pixels to the right of this Fighter's x position.
        # Append that Missile to this Fighter's list of Missile objects.
        pass

    def remove_exploded_missiles(self):
        # Already complete
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].has_exploded or self.missiles[k].y < 0:
                del self.missiles[k]
