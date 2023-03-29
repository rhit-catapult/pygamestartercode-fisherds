import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))

    is_mouth_visible = True
    # print(type(is_mouth_visible))
    is_nose_visible = True
    eye_x = 0
    eye_y = 0

    clock = pygame.time.Clock()

    while True:
        # 4: Set the clock speed to 60 fps
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 3: Make the eye pupils move with Up, Down, Left, and Right keys
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event)
                # print("Mouse down", event.pos)
                is_mouth_visible = not is_mouth_visible
            if event.type == pygame.KEYDOWN:
                # print(event)
                # print("Key down", event.key)
                # if event.key == 32:
                #     is_nose_visible = not is_nose_visible
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[pygame.K_SPACE]:
                    is_nose_visible = not is_nose_visible

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            eye_y -= 2
        if pressed_keys[pygame.K_DOWN]:
            eye_y += 2
        if pressed_keys[pygame.K_LEFT]:
            eye_x -= 2
        if pressed_keys[pygame.K_RIGHT]:
            eye_x += 2

        # screen.fill((255, 255, 255))  # white
        screen.fill(pygame.Color("white"))


        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242 + eye_x, 162 + eye_y), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398 + eye_x, 162 + eye_y), 7)  # black pupil

        # 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        # API --> pygame.draw.circle(screen, (r,g,b), (x, y), radius, thickness)
        if is_nose_visible:
            pygame.draw.circle(screen, (80, 0, 0), (screen.get_width() / 2, 245), 10)

        # 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)
        if is_mouth_visible:
            pygame.draw.rect(screen, pygame.Color("Black"), (230, 320, 180, 30))

        pygame.display.update()


main()
