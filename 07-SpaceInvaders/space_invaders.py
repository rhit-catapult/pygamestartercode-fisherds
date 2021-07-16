import pygame, sys


class Missile:
    def __init__(self, screen, x):
        # Store the data.  Initialize:   y to 591   and   has_exploded to False.
        # Note: the 591 comes from the screen height (650) minus the ship image height (59).  Best practice would be to
        #   pass in that value in case the ship image or screen height changes, but simplified here to always be 591.
        pass

    def move(self):
        # Make self.y 5 smaller than it was (which will cause the Missile to move UP).
        # Note: you could've instead passed in a speed when you made a Missle, but all missles in the game are the same
        #   speed, so just using a hardcoded 5 is fine.
        pass

    def draw(self):
        # Draw a vertical red (or green) line on the screen for the missile, 8 pixels long,  4 pixels thick
        #   where the line starts at the current position of this Missile.
        pass


class Fighter:
    def __init__(self, screen, x, y):
        # Store the given parameters to instance variables.
        # Set   self.missiles   to the empty list.
        # Load the file  "fighter.png"  as the image
        # Set the colorkey to white (it has a white background that needs removed) using the method set_colorkey
        pass

    def draw(self):
        # Draw this Fighter, using its image at its current (x, y) position.
        pass

    def fire(self):
        # Construct a new Missile self.image.get_width() / 2 pixels to the right of this Fighter's x position.
        # Append that Missile to this Fighter's list of Missile objects.
        pass

    def remove_exploded_missiles(self):
        # Already complete
        for k in range(len(self.missiles) - 1, -1, -1):
            if self.missiles[k].has_exploded or self.missiles[k].y < 0:
                del self.missiles[k]


class Badguy:
    def __init__(self, screen, x, y, speed):
        # Store the given arguments as instance variables with the same names.
        # Set   is_dead to False   and   original_x to x.
        # Load the file  "badguy.png"  as the image. and set its colorkey to black.
        # Additionally make a   move_right   instance variable set to to True (we might us it in the move method).
        pass

    def move(self):
        # Move self.speed units horizontally in the current direction.
        # If this Badguy's horizontal position is more than 100 pixels from its original x position, then...
        #     change the direction
        #     move the y down 4 * self.speed units
        pass

    def draw(self):
        # Draw this Badguy, using its image at its current (x, y) position.
        pass

    def hit_by(self, missile):
        # Make a Badguy hitbox rect.
        # Return True if that hitbox collides with the xy point of the given missile.
        pass


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
        pass

    def move(self):
        # Make each Badguy in badguys move.
        pass

    def draw(self):
        # Make each Badguy in badguys draw itself.
        pass

    def remove_dead_badguys(self):
        for k in range(len(self.badguys) - 1, -1, -1):
            if self.badguys[k].is_dead:
                del self.badguys[k]


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))

    # TODO 9: Set    enemy_rows    to an initial value of 3.
    # TODO 10: Create an EnemyFleet object (called enemy_fleet) with the screen and enemy_rows
    # TODO 1: Create a Fighter (called fighter) at location  320, 590
    #             Note: 320 is screen.get_width() / 2 and 590 is screen.get_height() - the ship's image height.

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            # TODO 5: If the event type is KEYDOWN and pressed_keys[pygame.K_SPACE] is True, then fire a missile
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        # TODO 3: If pygame.K_LEFT is pressed and fighter.x is greater than -50 move the fighter left 5
        # TODO 4: If pygame.K_RIGHT is pressed and fighter.x is less than 590 move the fighter right 5
        # TODO 2: Draw the fighter

        # TODO 11: Move the enemy_fleet
        # TODO 12: Draw the enemy_fleet

        # TODO 6: For each missile in the fighter missiles
        #   TODO 7: Move the missile
        #   TODO 8: Draw the missile

        # TODO 12: For each badguy in the enemy_fleet.badguys list
        #     TODO 13: For each missile in the fighter missiles
        #         TODO 14: If the badguy is hit by the missile
        #             TODO 15: Mark the badguy is_dead = True
        #             TODO 16: Mark the missile has_exploded = True

        #     TODO 13 (optional extra): For each missile in the fighter missiles
        #         TODO 14 (optional extra): If the missle.y is less than 0 (or -8)
        #             TODO 16 (optional extra): Mark the missile has_exploded = True (cleaning up off screen stuff)

        # TODO 17: Use the fighter to remove exploded missiles
        # TODO 18: Use the enemy_fleet to remove dead badguys

        # TODO 19: If the enemy is_defeated
        #     TODO 20: Increment the enemy_rows
        #     TODO 21: Create a new enemy_fleet with the screen and enemy_rows

        # TODO 22: Check for your death.  Figure out what needs to happen.
        # Hints: Check if a Badguy gets a y value greater than 545
        #    Note: 545 is screen.get_height() -
        #    If that happens set a variable (game_over) as appropriate
        #    If the game is over, show the gameover.png image at (170, 200)

        # TODO 23: Create a Scoreboard class (from scratch)
        # Hints: Instance variables: screen, score, and font (size 30)
        #    Methods: draw (and __init__)
        # Create a scoreboard and draw it at location 5, 5
        # When a Badguy is killed add 100 points to the scoreboard.score

        # TODO 24: Optional extra - Add sound effects!

        pygame.display.update()


main()
