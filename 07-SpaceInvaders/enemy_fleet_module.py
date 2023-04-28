import pygame
import sys


class Badguy:
    def __init__(self, screen, x, y, speed):
        # Store the given arguments as instance variables with the same names.
        # Set   is_dead to False   and   original_x to x.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("badguy.png")
        self.speed = speed
        self.original_x = x
        self.is_dead = False

    def move(self):
        # Move self.speed units horizontally in the current direction.
        # If this Badguy's horizontal position is more than 100 pixels from its original x position, then...
        #     change the direction
        #     move the y down 4 * self.speed units
        self.x += self.speed
        if abs(self.x - self.original_x) >= 100:
            self.speed = - self.speed
            self.y += 4 * abs(self.speed)

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
        self.screen.blit(self.image, (self.x, self.y))

    def is_hit_by(self, missile):
        # Make a Badguy hitbox rect.
        # Return True if that hitbox collides with the xy point of the given missile.
        hitbox = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        return hitbox.collidepoint(missile.x, missile.y)


class EnemyFleet:
    def __init__(self, screen, enemy_rows):
        # Already done.  Prepares the list of Badguys.
        self.badguys = []
        for j in range(enemy_rows):
            for k in range(8):
                self.badguys.append(Badguy(screen, 80 * k, 50 * j + 20, enemy_rows))

    @property
    def is_defeated(self):
        # Return True if the number of badguys in this Enemy Fleet is 0,
        # otherwise return False.
        return len(self.badguys) == 0

    def move(self):
        # Make each Badguy in badguys move.
        for badguy in self.badguys:
            badguy.move()

    def draw(self):
        # Make each Badguy in badguys draw itself.
        for badguy in self.badguys:
            badguy.draw()

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Enemy Fleet and Badguys only")
    screen = pygame.display.set_mode((640, 650))

    enemy_rows = 4
    enemy_fleet = EnemyFleet(screen, enemy_rows)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        enemy_fleet.draw()
        enemy_fleet.move()

        # enemy_fleet.remove_dead_badguys()
        pygame.display.update()


# Testing the classes
if __name__ == "__main__":
    main()
