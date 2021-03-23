# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
from ball import Ball
 
pygame.init()
 
# Define some colors
BLACK = (0,0,0)
RED= (233,40,37)
WHITE = (255,255,255)
GREY = (158,153,153)
YELLOW = (254,250,16)
 
# Open a new window
size = (900, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game")
 
paddleA = Paddle(WHITE, 10, 80)
paddleA.rect.x = 20
paddleA.rect.y = 150
 
paddleB = Paddle(WHITE, 10, 80)
paddleB.rect.x = 870
paddleB.rect.y = 150
 
ball = Ball(RED,10,10)
ball.rect.x = 445
ball.rect.y = 145
 
#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
 
# Add the car to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
 
# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
#Initialise player scores
scoreA = 0
scoreB = 0
 
# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False
 
    #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)    
 
    # --- Game logic should go here
    all_sprites_list.update()
    
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=890:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>690:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]     
 
    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
      ball.bounce()
    
    # --- Drawing code should go here
    # First, clear the screen to black. 
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen,GREY, [449, 0], [449, 700], 5)
    
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen) 
 
    #Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, YELLOW)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, YELLOW)
    screen.blit(text, (620,10))
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 60 frames per second
    clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()