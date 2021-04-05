#icons from flaticon by freepik & smashicons
import pygame
import random
import math
from pygame import mixer

#Initialization
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

#Background
#background = pygame.image.load("space-background.jpg")

#music
mixer.music.load('lib/music/chronos.mp3')
mixer.music.play(-1)

#Title & Icon
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load('stars.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('human-ship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('space-ship.png'))
    enemyX.append(random.randint(10, 726))
    enemyY.append(random.randint(10, 390))
    enemyX_change.append(0.3)
    enemyY_change.append(40)


#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready" #ready - invisible, fire - visible

#score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

def show_score(x,y):
    scoreShow = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(scoreShow, (x, y))

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision (enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#Game Loop
running = True
while running:

    screen.fill((0, 100, 100))

    #screen.blit(background,(0,0)) nie podoba mi się

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to sprawia, że okno się nie zamyka
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.25
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.25
            if event.key == pygame.K_DOWN:
                playerY_change = 0.25
            if event.key == pygame.K_UP:
                playerY_change = -0.25
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('lib/music/laser.wav')
                    bullet_sound.play(1)
                    bulletX = playerX
                    fire_bullet(bulletX ,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0






    playerX += playerX_change
    playerY += playerY_change

#boundaries
    if playerX <=10:
        playerX = 10
    elif playerX >= 726:
        playerX = 726
    if playerY >= 526:
        playerY = 526
    elif playerY <= 400:
        playerY = 400

    for i in range (num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 10:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 726:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(10, 726)
            enemyY[i] = random.randint(10, 390)

        enemy(enemyX[i], enemyY[i], i)

    #bullet movement
    if bulletY<=0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    show_score(textX, textY)


    pygame.display.update()
