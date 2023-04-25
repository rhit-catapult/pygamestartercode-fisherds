import pygame
import sys

import fighter_missile_module as fmm
import enemy_fleet_module as efm


class Scoreboard:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        # TODO: Convert the score into a string using the format "Score: " + number
        # TODO: Using the font object convert the string into an image
        # TODO: Blit the image onto the screen at 5, 5
        as_text = "Score: " + str(self.score)
        as_image = self.font.render(as_text, True, (255, 255, 255))
        self.screen.blit(as_image, (5, 5))


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))
    scoreboard = Scoreboard(screen)

    #  9: Set    enemy_rows    to an initial value of 3.
    #  10: Create an EnemyFleet object (called enemy_fleet) with the screen and enemy_rows

    enemy_rows = 3
    game_over = False
    enemy_fleet = efm.EnemyFleet(screen, enemy_rows)

    #  1: Create a Fighter (called fighter)
    fighter = fmm.Fighter(screen)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            #  5: If the event type is KEYDOWN and pressed_keys[pygame.K_SPACE] is True, then fire a missile
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_SPACE]:
                    fighter.fire()

            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))

        fighter.draw()
        enemy_fleet.draw()
        scoreboard.draw()

        if game_over:
            game_over_image = pygame.image.load("gameover.png")
            screen.blit(game_over_image, (170, 200))
            pygame.display.update()
            continue
        #  3: If pygame.K_LEFT is pressed and move the fighter left 5 (i.e. -5)
        #  4: If pygame.K_RIGHT is pressed and move the fighter right 5

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            fighter.move(-5)
        if pressed_keys[pygame.K_RIGHT]:
            fighter.move(5)

        #  2: Draw the fighter

        #  11: Move the enemy_fleet
        #  12: Draw the enemy_fleet
        enemy_fleet.move()

        #  6: For each missile in the fighter missiles
        #    7: Move the missile
        #    8: Draw the missile

        for missile in fighter.missiles:
            missile.move()
            missile.draw()

        # Done 12: For each badguy in the enemy_fleet badguys
        #     Done 13: For each missile in the fighter missiles
        #         Done 14: If the badguy is hit by the missile
        #             Done 15: Mark the badguy as is_dead = True
        #             Done 16: Mark the missile as exploded = True
        for badguy in enemy_fleet.badguys:
            for missile in fighter.missiles:
                if badguy.is_hit_by(missile):
                    # Increment the score (play a sound?)
                    scoreboard.score += 100
                    badguy.is_dead = True
                    missile.has_exploded = True

        for missile in fighter.missiles:
            if missile.is_off_screen():
                missile.has_exploded = True

        # Done 17: Use the fighter to remove exploded missiles
        fighter.remove_exploded_missiles()

        # Done 18: Use the enemy_fleet to remove dead badguys
        enemy_fleet.remove_dead_badguys()

        # TODO 19: If the enemy is_defeated
        #     TODO 20: Increment the enemy_rows
        #     TODO 21: Create a new enemy_fleet with the screen and enemy_rows
        if enemy_fleet.is_defeated:
           enemy_rows = enemy_rows + 1
           enemy_fleet = efm.EnemyFleet(screen, enemy_rows)

        #  22: Check for your death.  Figure out what needs to happen.
        # Hints: Check if a Badguy gets a y value greater than 545
        #    Note: 545 is screen.get_height() -
        #    If that happens set a variable (game_over) as appropriate
        #    If the game is over, show the gameover.png image at (170, 200)
        for badguy in enemy_fleet.badguys:
            if badguy.y + badguy.image.get_height() >= fighter.y:
                game_over = True

        # TODO 23: Create a Scoreboard class (from scratch)
        # Hints: Instance variables: screen, score, and font (size 30)
        #    Methods: draw (and __init__)
        # Create a scoreboard and draw it at location 5, 5
        # When a Badguy is killed add 100 points to the scoreboard.score

        # TODO 24: Optional extra - Add sound effects!

        pygame.display.update()


main()
