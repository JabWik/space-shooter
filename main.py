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

def player():
    screen.blit(playerImg,(playerX,playerY))

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to sprawia, że okno się nie zamyka
            running = False
    screen.fill((0, 100, 100))

    player()
    pygame.display.update()
