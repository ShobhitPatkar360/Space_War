import pygame   #Press Ctrl+Alt+L  to look code good

pygame.init()

screen = pygame.display.set_mode((800, 600))  # 400,300

# Setting Title
pygame.display.set_caption("Space War")

# Setting Icon
icon = pygame.image.load("robot.png")  # Size = 32x32
pygame.display.set_icon(icon)

# Adding Background
background = pygame.image.load("background.png")

# enemy
enemyImg = pygame.image.load("enemy.png")  # size 64x64
enemyX = 0
enemyY = 50
enemyXChange = 1
enemyYChange = 40


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# player
playerImg = pygame.image.load("player.png")
playerX = 368
playerY = 480
playerXChange = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True
while running:

    # Red Green Blue
    screen.fill((100, 50, 37))

    # adding backgroudn
    screen.blit(background, (0, 0))

    # Step 1 => Detect key + "playerXChange" value change
    for event in pygame.event.get():  # Collection of events [ QUIT , KEYDOWN{}  , KEYUP {}, ,   ,   , ]
        if event.type == pygame.QUIT:  # K_LEFT,K_RIGHT,
            running = False

        if event.type == pygame.KEYDOWN:
            # print("key is pressed")

            if event.key == pygame.K_LEFT:
                playerXChange = -0.3

            if event.key == pygame.K_RIGHT:
                playerXChange = 0.3

        if event.type == pygame.KEYUP:
            playerXChange = 0

    # Addig Boundries
    if playerX <= 0:
        playerX = 0

    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX = enemyX + enemyXChange
    if enemyX >= 736:
        enemyXChange = -1
        enemyY = enemyY + enemyYChange

    elif enemyX <= 0:
        enemyXChange = 1
        enemyY = enemyY + enemyYChange
    # player movement => Step 2 => Change Coordinate

    enemy(enemyX, enemyY)
    player(playerX, playerY)
    playerX = playerX + playerXChange
    pygame.display.update()

"""
Player Motion Control
Step1: Detect key
Step2: Change coordinate
"""
