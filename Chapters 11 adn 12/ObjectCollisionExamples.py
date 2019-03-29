# import our modules
import pygame
from pygame.locals import *
import sys

# Initialize our pygame modules
pygame.init()

# Create tuples for our colors
colorWHITE = (255,255,255)
colorBLACK = (0,0,0)
colorRED = (255,0,0)

# Create our main game window - last time we named it screen
# Let's give it a different name this time
gameWindow = pygame.display.set_mode((800,600))

# Set the caption/title for our animation
pygame.display.set_caption('Colliding Objects')

gameQuit = False

# Create two variables that will store sprite rectangle objects
rect1 = pygame.sprite.Sprite()
rect1.rect = pygame.Rect(300,300,50,50)

rect2 = pygame.sprite.Sprite()
rect2.rect = pygame.Rect(100,100, 100,150)

# Game Loop
while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            pygame.quit()
            sys.exit()
        # If the player presses 'q', it is considered a quit event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        # If the player presses 'ESC', it is considered a quit event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        # If arrow key left is pressed, move the object left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect1.rect.x = rect1.rect.x - 10
        # If arrow key right is pressed, move the object right
            if event.key == pygame.K_RIGHT:
                rect1.rect.x = rect1.rect.x +10
        # If arrow key up is pressed, move the object up                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rect1.rect.y = rect1.rect.y -10
        # If arrow key down is pressed, move the object down         
            if event.key == pygame.K_DOWN:
                rect1.rect.y = rect1.rect.y +10

        # Check for collision between our two rect objects
        # using collide_rect
        # If a collision is detected, we relocate rect1
        # by changing its y and x coordinates
        if pygame.sprite.collide_rect(rect1, rect2):
            rect1.rect.y = 400
            rect1.rect.x = 400
        
        # Check to see if we collide with the right screen end
        # If it does, we move rect1 back to X coordinate 740
        if rect1.rect.x > 750:
            rect1.rect.x = 740
            pygame.display.set_caption('Right Collision')
        if rect1.rect.x < 1:
            rect1.rect.x = 51
        # Check to see if we collide with the left screen end
            pygame.display.set_caption('Left Collision')
        # Check to see if we collide with the bottom of the screen
        if rect1.rect.y > 550:
            rect1.rect.y = 540
            pygame.display.set_caption('Bottom Collision')
        # Check to see if we collide with the top of the screen
        if rect1.rect.y < 1:
            rect1.rect.y = 50
            pygame.display.set_caption('Top Collision')
            
            
    # Fill the gameWindow with the color white
    gameWindow.fill(colorWHITE)

    # Blit our rectangle objects
    pygame.draw.rect(gameWindow, colorBLACK, rect1)
    pygame.draw.rect(gameWindow, colorRED, rect2)
    
    
    # Update our screen
    pygame.display.update()

    
