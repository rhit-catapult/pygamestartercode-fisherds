import pygame
import sys

pygame.init()

pygame.display.set_caption("Hello Dave Fisher")
screen = pygame.display.set_mode((1280, 640))

while True:
    for event in pygame.event.get():
        print(event)  # Weird usually you DO something

        if event.type == pygame.QUIT:
            sys.exit()

        # Additional interactions with events

    screen.fill(pygame.Color("gray"))

    # Done 01: Try to draw a circle (any size, any color, anywhere)
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, (0, 0, 255), (1270, 10), 10, 2)

    # TODO 02: Try to draw a red circle in the middle of the screen with a radius 100
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, (255, 0, 0), (screen.get_width() / 2, screen.get_height() / 2), 100)

    # TODO 03: Try to draw a yellow circle with the center exactly in the lower left corner of the screen, radius 10
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    radius = 100
    pygame.draw.circle(screen, (255, 255, 0), (radius, screen.get_height() - radius), radius)

    pygame.display.update()
