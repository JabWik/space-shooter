#icons from flaticon by freepik & smashicons
import pygame
import random

#Initialization
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load("space-background.jpg")

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
enemyImg = pygame.image.load('space-ship.png')
enemyX = random.randint(10, 726)
enemyY = random.randint(10, 390)
enemyX_change = 0.3
enemyY_change = 40

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#Game Loop
running = True
while running:

    screen.fill((0, 100, 100))

    screen.blit(background,(0,0))

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

    enemyX += enemyX_change

    if enemyX <= 10:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 726:
        enemyX_change = -0.3
        enemyY += enemyY_change



    player(playerX, playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()
