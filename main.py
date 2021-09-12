import pygame  # Press Ctrl+Alt+L  to look code good
import math
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


# Bullet
bulletImg = pygame.image.load("Bullet.png")  # size 32x32
bulletX = 0
bulletY = 480
bulletXChange = 0
bulletYChange = -3
bullet_state = "ready" # fire = we want to show bullet ; ready = we want to hide bullet


score = 0
def isCollision(enemyX,enemyY,bulletX,bulletY):

    dis = math.sqrt( (math.pow(bulletX-enemyX,2)) + (math.pow(bulletY-enemyY,2)) )
    if dis < 27:
        return True
    else:
        return False


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+15, y-30))



# Game Loop
running = True
while running:

    # Red Green Blue
    screen.fill((100, 50, 37))

    # adding background
    screen.blit(background, (0, 0))

    # Step 1 => Detect key + "playerXChange" value change
    for event in pygame.event.get():  # Collection of events [ QUIT , KEYDOWN{}  , KEYUP {}, ,   ,   , ]
        if event.type == pygame.QUIT:  # K_LEFT,K_RIGHT,
            running = False

        if event.type == pygame.KEYDOWN:
            # print("key is pressed")

            if event.key == pygame.K_LEFT:
                playerXChange = -1

            if event.key == pygame.K_RIGHT:
                playerXChange = 1

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bullet_state = "fire"


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
    playerX = playerX + playerXChange

    #bullet movement
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480


    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY = bulletY + bulletYChange

    #Collion Management
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bullet_state = "ready"
        bulletY = 480
        score = score + 1
        enemyX = 0
        enemyY = 50
        print("Score : "+str(score)) #print() support concatantion of  only string





    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()

"""
Player Motion Control
Step1: Detect key
Step2: Change coordinate
"""

"""
Bullet Motion Control
Step1: Player coordinates => Bullet coordinates
Step2: Bullet Y coordinate (decrease)

"""
# 2^2      54^3   math.pow(2,2)  math.pow(54,3)
"""
if else in python
String
if variable == "word"   if variable is "word":

Boolean
if variable == True   if variable:

"""



"""
if enemy is shooted
1.bullet_state = "ready"
2.score display
3.enemy is placed to inital position

"""