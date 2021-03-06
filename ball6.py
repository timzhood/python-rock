"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting x,y position of the square
# Note how this is outside the main while loop.
square_x = 50
square_y = 50

# start going right and down
change_x = 5
change_y = 5

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    pygame.draw.rect(screen, WHITE, [square_x, square_y, 50, 50])

    # Draw a red rectangle inside the white one
    pygame.draw.rect(screen, RED, [square_x + 10, square_y + 10, 30, 30])

    # Move the x,y point at which the square is drawn
    square_x = square_x + change_x
    square_y = square_y + change_y

    # Bounce the rectangle if needed

    # when hit bottom edge
    if square_y > 450:
        # change direction, go up
        change_y = -5

    # when hit top edge
    if square_y < 0:
        # change direction, go down
        change_y = 5

    # when hit right edge
    if square_x > 650:
        # change direction, go left
        change_x = -5

    # when hit left edge
    if square_x < 0:
        # change direction, go right
        change_x = 5

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
