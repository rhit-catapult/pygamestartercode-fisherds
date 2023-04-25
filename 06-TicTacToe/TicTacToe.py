import pygame
import sys


# --------------------------- Conversion helper functions ---------------------------

def get_row_col(mouse_pos):
    """ Converts an (x, y) screen position into a row, col value. """
    mouse_x = mouse_pos[0]  # Note: a point tuple is now passed into this function.
    mouse_y = mouse_pos[1]
    # Note: the top row is row=0 (bottom row=2), left col is col=0 (right col=2)
    spacing_x = 86 + 8
    spacing_y = 98 + 5
    top_y = 50
    left_x = 50
    return (mouse_y - top_y) // spacing_y, (mouse_x - left_x) // spacing_x


def get_xy_position(row, col):
    """ Converts a row, col value into an x, y screen position (upper left corner of that location). """
    spacing_x = 86 + 11
    spacing_y = 98 + 8
    top_y = 50
    left_x = 50
    return left_x + col * spacing_x, top_y + row * spacing_y


# --------------------------- Model Object ---------------------------


class Game:
    def __init__(self):
        #  5: Create an empty board, called board
        #         A list that contains 3 lists, each of those lists has 3 "." values.
        #     - Create a game_state_string set to X's turn
        #     - Create a turn_counter variable set to 0
        #     - Create a game_is_over variable set to False
        self.board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        self.game_state_string = "X's turn"
        self.turn_counter = 0
        self.game_is_over = False

    def __repr__(self):
        """ Returns a string that represents the game. """
        #  7: Use a "".format() command to create a string to shows the board, turn_counter, and game_state_string
        return f"State: {self.game_state_string}  \nBoard: {self.board}  \nTurn: {self.turn_counter}"

    def take_turn(self, row, col):
        """Handle the current turn of the player and update board array"""
        #  8: Check if game_is_over and return from this method (doing nothing) if True
        if self.game_is_over:
            return  # This game is over, don't allow clicks.  Don't be silly.
        #  9: Check if the value for row and col are valid.  Return (doing nothing) if invalid.
        if row < 0 or row > 2 or col < 0 or col > 2:
            return  # Defensive programming.  The ViewController can pass me anything!
        #  10: Check if the mark at the requested row col is ".".  Return (doing nothing) if it is not "."
        if self.board[row][col] != ".":
            return  # this square is full!

        #  11: Determine if it is X's turn or O's turn (even turn_counter means X's turn, odd for O's turn)
        #     - Modify the board by setting the current row col to an "X" or an "O" as appropriate
        #     - Update the game_state_string as appropriate "O's Turn" or "X's Turn"
        if self.turn_counter % 2 == 0:
            self.board[row][col] = "X"
            self.game_state_string = "O's Turn"
        else:
            self.board[row][col] = "O"
            self.game_state_string = "X's Turn"

        #  12: Increment the turn_counter
        self.turn_counter += 1

        self.check_for_game_over()

    def check_for_game_over(self):
        #  18: If the turn_counter is 9 then the game is over
        #      If >=9 update the game_is_over value and set the game_state_string to "Tie Game"
        if self.turn_counter >= 9:
            self.game_state_string = "Tie Game"

        lines = []
        lines.append(self.board[0][0] + self.board[0][1] + self.board[0][2])
        lines.append(self.board[1][0] + self.board[1][1] + self.board[1][2])
        lines.append(self.board[2][0] + self.board[2][1] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][0] + self.board[2][0])
        lines.append(self.board[0][1] + self.board[1][1] + self.board[2][1])
        lines.append(self.board[0][2] + self.board[1][2] + self.board[2][2])
        lines.append(self.board[0][0] + self.board[1][1] + self.board[2][2])
        lines.append(self.board[0][2] + self.board[1][1] + self.board[2][0])

        #  19: Use the lines list to determine if there is a winner.
        #    If there is a winner, update the game_state_string, play a sound, and set game_is_over to True.
        for line in lines:
            if line == "XXX":
                self.game_is_over = True
                self.game_state_string = "X Wins!"
                pygame.mixer.music.play()
            if line == "OOO":
                self.game_is_over = True
                self.game_state_string = "O Wins!"
                pygame.mixer.music.play()


# --------------------------- View Controller ---------------------------

class ViewController:

    def __init__(self, screen: pygame.Surface):
        """ Creates the view controller (the Tic-Tac-Toe game you see) """
        #  4: Initialize the ViewController, as follows:
        #     - Store the screen.
        #     - Create the game model object.
        #     - Create images for the board, X, and O images filenames.
        #  Use instance variables:   screen game board_image x_image o_image
        self.screen = screen
        self.game = Game()
        self.board_image = pygame.image.load("board.png")
        self.x_image = pygame.image.load("x_mark.png")
        self.o_image = pygame.image.load("o_mark.png")

    def check_event(self, event):
        """ Takes actions as necessary based on the current event. """
        #  16: If the event is pygame.MOUSEBUTTONUP
        #     Get the mouse click position (event.pos or pygame.mouse.get_pos())
        #     Get the row and col values of that position using get_row_col
        #     Inform the model object about this event
        #  17: If the event is pygame.KEYDOWN
        #     Get the pressed_keys
        #     If the key is pygame.K_SPACE, then reset the game.
        if event.type == pygame.MOUSEBUTTONUP:
            # get_row_col(event.pos)
            row, col = get_row_col(pygame.mouse.get_pos())
            self.game.take_turn(row, col)
        if event.type == pygame.KEYDOWN:
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_SPACE]:
                self.game = Game()


    def draw(self):
        """ Draw the board based on the marked store in the board configuration array """
        #  13: Blit the board_image onto the screen at the x y position of row=0 col=0
        #  14: Use a nested loop (via range) to go over all marks of the game.board
        #    If the mark is "X", blit an X image at the x y position of row col
        #    If the mark is "O", blit an O image at the x y position of row col
        #  15: Update the display caption to be the game.game_state_string
        self.screen.blit(self.board_image, get_xy_position(0, 0))
        for row in range(3):
            for col in range(3):
                current_mark = self.game.board[row][col]
                if current_mark == "X":
                    self.screen.blit(self.x_image, get_xy_position(row, col))
                if current_mark == "O":
                    self.screen.blit(self.o_image, get_xy_position(row, col))
        pygame.display.set_caption(self.game.game_state_string)


# --------------------------- Controller ---------------------------


def main():
    pygame.init()
    pygame.mixer.music.load("win.mp3")
    screen = pygame.display.set_mode((380, 400))
    #  1: Create an instance of the ViewController class called view_controller
    view_controller = ViewController(screen)

    # TODO: Later comment this all out!
    # ---------------------------------------
    # 6: Write test code as needed to develop your model object.
    # print(view_controller.game)   # New unstarted game
    # view_controller.game.take_turn(1, 1)
    # print(view_controller.game)  # Now the game is O's turn, counter = 1, with an "X" in the middle
    # view_controller.game.take_turn(0, 0)
    # print(view_controller.game)  # "X's Turn" board O.. .X. ...
    #
    # view_controller.game.take_turn(0, 1)  # X top middle
    # view_controller.game.take_turn(2, 0)  # O in the lower left
    # view_controller.game.take_turn(2, 1)  # X bottom middle
    # print(view_controller.game)  # X Wins!
    # ---------------------------------------

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #  2: Pass the event to the view_controller
            view_controller.check_event(event)

        screen.fill(pygame.Color("white"))
        #  3: Draw the view_controller
        view_controller.draw()
        pygame.display.update()


main()
