import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Load the music and the image
    # Done 1: Create an image with the 2dogs.JPG image
    dog_image = pygame.image.load("2dogs.JPG")
    dog_image = pygame.transform.scale(dog_image, (IMAGE_SIZE, IMAGE_SIZE))

    # Done 4: Create a font object with a size 28 font.
    font1 = pygame.font.SysFont("comicsansms", 28)
    # Done 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).
    caption1 = font1.render("Two Dogs", True, BLACK)

    font2 = pygame.font.SysFont("impact", 50)
    caption2 = font2.render("This human is mine!", True, WHITE)

    print(pygame.font.get_fonts())

    # Done 8: Create a Sound object from the "bark.wav" file.
    bark_sound = pygame.mixer.Sound("bark.wav")  # Sound effects
    pygame.mixer.music.load("bark.mp3")  #  Load a song for background music



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Done 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                # bark_sound.play(5)
                pygame.mixer.music.play(-1)
            if event.type == pygame.MOUSEBUTTONUP:
                pygame.mixer.music.stop()

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # Done 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
        # Done 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(dog_image, (0, 0))

        # Draw the text onto the screen

        # Done 6: Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        screen.blit(caption1, (screen.get_width() / 2 - (caption1.get_width() / 2), 462))

        # Done 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.
        screen.blit(caption2, (screen.get_width() / 2 - (caption2.get_width() / 2), 400))
        # Update the screen
        pygame.display.update()


main()
