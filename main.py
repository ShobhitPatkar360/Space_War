import pygame
pygame.init()

screen = pygame.display.set_mode((800,600)) #400,300

#Setting Title
pygame.display.set_caption("Space War")

#Setting Icon
icon = pygame.image.load("robot.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("player.png")
playerX = 368
playerY = 268
playerXChange = 0

def player(x,y):
    screen.blit(playerImg, (x,y))


#Game Loop
running = True
while running:

    # Red Green Blue
    screen.fill((255, 0, 0))


    player(playerX,playerY)

    #Step 1 => Detect key + "playerXChange" value change
    for event in pygame.event.get(): # Collection of events [ QUIT , KEYDOWN{}  , KEYUP {}, ,   ,   , ]
        if event.type == pygame.QUIT:               #               K_LEFT,K_RIGHT,
            running = False

        if event.type == pygame.KEYDOWN:
            #print("key is pressed")

            if event.key == pygame.K_LEFT:
                playerXChange -= 0.3

            if event.key == pygame.K_RIGHT:
                playerXChange += 0.3

        if event.type == pygame.KEYUP:
            playerXChange = 0



    #player movement => Step 2 => Change Coordinate
    playerX = playerX + playerXChange


    pygame.display.update()

"""
Player Motion Control
Step1: Detect key
Step2: Change coordinate
"""

