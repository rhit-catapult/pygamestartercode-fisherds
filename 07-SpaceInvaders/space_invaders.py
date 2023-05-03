import pygame
import sys

import fighter_missile_module as fmm
import enemy_fleet_module
import scoreboard_module


def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("SPACE INVADERS!")
    screen = pygame.display.set_mode((640, 650))

    is_game_over = False
    enemy_rows = 3
    enemy_fleet = enemy_fleet_module.EnemyFleet(screen, enemy_rows)
    fighter = fmm.Fighter(screen)
    scoreboard = scoreboard_module.Scoreboard(screen)
    win_sound = pygame.mixer.Sound("win.wav")
    lose_sound = pygame.mixer.Sound("lose.wav")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
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

        if is_game_over:
            game_over_image = pygame.image.load("gameover.png")
            screen.blit(game_over_image, (170, 200))
            pygame.display.update()
            continue

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            fighter.move(-5)
        if pressed_keys[pygame.K_RIGHT]:
            fighter.move(5)

        enemy_fleet.move()

        for missile in fighter.missiles:
            missile.move()
            missile.draw()

        for badguy in enemy_fleet.badguys:
            for missile in fighter.missiles:
                if badguy.is_hit_by(missile):
                    scoreboard.score += 100
                    badguy.is_dead = True
                    missile.has_exploded = True

        fighter.remove_exploded_missiles()
        enemy_fleet.remove_dead_badguys()

        if enemy_fleet.is_defeated:
            enemy_rows += 1
            win_sound.play()
            enemy_fleet = enemy_fleet_module.EnemyFleet(screen, enemy_rows)

        for badguy in enemy_fleet.badguys:
            if badguy.y + badguy.image.get_height() > fighter.y + 10:
                is_game_over = True
                lose_sound.play()

        pygame.display.update()


main()
