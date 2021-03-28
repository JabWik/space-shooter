#icons from flaticon by freepik & smashicons
import pygame

#Initialization
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800,600))

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

def player(x,y):
    screen.blit(playerImg,(x,y))

#Game Loop
running = True
while running:

    screen.fill((0, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to sprawia, że okno się nie zamyka
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_DOWN:
                playerY_change = 0.2
            if event.key == pygame.K_UP:
                playerY_change = -0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0






    playerX += playerX_change
    playerY += playerY_change

    if playerX <=10:
        playerX = 10
    elif playerX >= 726:
        playerX = 726
    if playerY >= 526:
        playerY = 526
    elif playerY <= 400:
        playerY = 400



    player(playerX, playerY)
    pygame.display.update()
