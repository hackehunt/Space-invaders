# Importing modules
import pygame
from pygame import mixer
import random

# Initializing modules
pygame.init()
pygame.mixer.init()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Game variables
score = 0
lives = 5

# Managing game window
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("space invaders")

# Background image
background = pygame.image.load("img/background.png")
background = pygame.transform.scale(background, (600, 600)).convert_alpha()

# Displaying icon
icon = pygame.image.load("img/play.png")
pygame.display.set_icon(icon)

# Displaying text on screen
font = pygame.font.SysFont("horroid", 30)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text, [x, y])


# displaying player
player_img = pygame.image.load("img/2.png")
playerX = 300
playerY = 520
playerX_change = 0

# displaying enemy
enemy_img = []
enemyX = []
enemyY = []
enemyY_change = []
no_of_enemies = 5

for i in range(no_of_enemies):
    enemy_img.append(pygame.image.load("img/first.ico"))
    enemyX.append(random.randint(10, 500))
    enemyY.append(random.randint(0, 1))
    enemyY_change.append(0.1)


def enemy(i, x, y):
    window.blit(enemy_img[i], (x, y))


# Player bullets
bullet_img = pygame.image.load("img/bullet (9).png")
bulletX = playerX + 20
bulletY = playerY - 25
mixer.music.load("img/shoot/shoot.wav")
mixer.music.play()
bulletY_change = 3.5
# Gameover text
over_font = pygame.font.SysFont("parry hotter",  50)
fnoooooot = pygame.font.SysFont("Gazzarelli",  25)
fnoooooot1 = pygame.font.SysFont("Gazzarelli",  20)
# fnoooooot = pygame.font.Sysfont("Gazzarelli", 20)


def player():
    window.blit(player_img, (playerX, playerY))


def bullet():
    window.blit(bullet_img, (bulletX, bulletY))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    if score >= 100 or score >= 60:
        cover_text = fnoooooot1.render(f";) Whoa!, you eliminate {score} enemies", True, (255, 0, 255))
    else:
        cover_text = fnoooooot.render(f":( Damn!, we have lost by aliens?", True, (255, 0, 255))
    window.blit(over_text, (150, 250))
    window.blit(cover_text, (0, 325))


running = True
while running:
    # Background
    window.blit(background, (0, 0))

    # Displaying score on screen
    text_screen(f"Score : {score}", white, 10, 10)

    # In game controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.6
            if event.key == pygame.K_LEFT:
                playerX_change = -0.6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_LEFT:
                playerX_change = 0

    # Calling functions and states
    playerX += playerX_change
    bulletY += -bulletY_change
    player()
    bullet()

    # Player mechanics
    if playerX <= 0:
        playerX = 0
    if playerX >= 535:
        playerX = 535

    # Multiple enemies
    for i in range(no_of_enemies):
        enemyY[i] += enemyY_change[i]
        # Collision
        if abs(enemyX[i] - bulletX) < 30 and abs(enemyY[i] - bulletY) < 30:
            mixer.music.load("img/invaderkilled/invaderkilled.wav")
            mixer.music.play()
            enemyX[i] = random.randint(10, 500)
            enemyY[i] = random.randint(0, 1)
            score += 1
            bulletX = playerX + 20
            bulletY = playerY - 25

        # Game Over
        if abs(enemyX[i] - playerX) < 30 and abs(enemyY[i] - playerY) < 30:
            window.fill(white)
        enemy(i, enemyX[i], enemyY[i])

    # Bullet mechanics
    if bulletY <= 0:
        bulletX = playerX + 20
        bulletY = playerY - 25
        mixer.music.load("img/shoot/shoot.wav")
        mixer.music.play()
        bulletY_change = 3.5

    for i in range(no_of_enemies):

        # Game Over
        if enemyY[i] > 600:
            # enemyX = (random.randint(10, 500))
            # enemyY = (random.randint(0, 1))
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            # break

    if score >= 50:
        bulletY_change = 3.5
        for i in range(no_of_enemies):
            enemyY[i] += enemyY_change[i]
            # Collision
            if abs(enemyX[i] - bulletX) < 30 and abs(enemyY[i] - bulletY) < 30:
                mixer.music.load("img/invaderkilled/invaderkilled.wav")
                mixer.music.play()
                enemyX[i] = random.randint(10, 500)
                enemyY[i] = random.randint(0, 1)
                score += 1
                bulletX = playerX + 20
                bulletY = playerY - 25
            # Game Over
            if abs(enemyX[i] - playerX) < 30 and abs(enemyY[i] - playerY) < 30:
                lives -= 1
                window.fill(red)
            enemy(i, enemyX[i], enemyY[i])
    if score >= 100:
        bulletY_change = 4.1
        # displaying enemy
        enemy_img = []
        # enemyX = []
        # enemyY = []
        enemyY_change = []
        enemyX_change = []
        # no_of_enemies = 5
        enemyX += enemyX_change
        for i in range(5):
            enemy_img.append(pygame.image.load("img/fo4.ico"))
            # enemyX.append(random.randint(10, 500))
            enemyY.append(random.randint(0, 1))
            enemyY_change.append(0.2)
            enemyX_change.append(2)
    if score >= 500:
        bulletY_change = 4
        for i in range(no_of_enemies):
            bulletY_change = 4.5
            # displaying enemy
            enemy_img = []
            # enemyX = []
            # enemyY = []
            enemyY_change = []
            enemyX_change = []
            # no_of_enemies = 5
            enemyX += enemyX_change
            for i in range(5):
                enemy_img.append(pygame.image.load("img/fo1.ico"))
                # enemyX.append(random.randint(10, 500))
                enemyY.append(random.randint(0, 1))
                enemyY_change.append(0.2)
                enemyX_change.append(2)
    if score >= 1000:
        bulletY_change = 5
        # displaying enemy
        enemy_img = []
        # enemyX = []
        # enemyY = []
        enemyY_change = []
        enemyX_change = []
        # no_of_enemies = 5
        enemyX += enemyX_change
        for i in range(5):
            enemy_img.append(pygame.image.load("img/fo7.ico"))
            # enemyX.append(random.randint(10, 500))
            enemyY.append(random.randint(0, 1))
            enemyY_change.append(0.2)
            enemyX_change.append(2)

    pygame.display.update()
