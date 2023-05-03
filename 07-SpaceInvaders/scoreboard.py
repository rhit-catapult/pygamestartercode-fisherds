import pygame
import sys


class Scoreboard:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.score = 0
        self.font = pygame.font.SysFont(None, 30)

    def draw(self):
        caption = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(caption, (2, 2))


def main():
    print("Testing the scoreboard")
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Scoreboard only")
    screen = pygame.display.set_mode((640, 650))

    print(pygame.font.get_fonts())

    scoreboard = Scoreboard(screen)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            # Doing something once when a key is PRESSED
            if event.type == pygame.KEYDOWN:
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_SPACE]:
                    scoreboard.score += 100
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))
        scoreboard.draw()
        pygame.display.update()




if __name__ == "__main__":
    main()
