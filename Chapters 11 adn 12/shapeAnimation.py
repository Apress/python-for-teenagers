# import our modules
import pygame
from pygame.locals import *
import sys
import random

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
pygame.display.set_caption('Box Animator 5000')

gameQuit = False

move_x = 300
move_y = 300

rect1 = pygame.Rect(move_x,move_y,50,50)
rect2 = pygame.Rect(100,100, 100,150)

# Game Loop
while not gameQuit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            pygame.qui()
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
                move_x -= 10
        # If arrow key right is pressed, move the object right
            if event.key == pygame.K_RIGHT:
                move_x += 10
        # If arrow key up is pressed, move the object up                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_y -=10
        # If arrow key down is pressed, move the object down         
            if event.key == pygame.K_DOWN:
                move_y +=10
        # if 't' is pressed, randomly teleport the object
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                move_y = int(random.randint(1,600))
                move_x = int(random.randint(1,600))
                
        # Check to see if we collide with the right screen end        
        if move_x > 750:
            move_x -= 50
            pygame.display.set_caption('Right Collision')
        if move_x < 1:
            move_x += 50
        # Check to see if we collide with the left screen end
            pygame.display.set_caption('Left Collision')
        # Check to see if we collide with the bottom of the screen
        if move_y > 550:
            move_y -= 50
            pygame.display.set_caption('Bottom Collision')
        # Check to see if we collide with the top of the screen
        if move_y < 1:
            move_y += 50
            pygame.display.set_caption('Top Collision')
            
            
    # Fill the gameWindow with the color white
    gameWindow.fill(colorWHITE)

    # Blit a black rectangle object
    pygame.draw.rect(gameWindow, colorBLACK, [move_x,move_y,50,50])
    pygame.draw.rect(gameWindow, colorBLACK, rect1)
    pygame.draw.rect(gameWindow, colorRED, rect2)
    
    
    # Update our screen
    pygame.display.update()

    
