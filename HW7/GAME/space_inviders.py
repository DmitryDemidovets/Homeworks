'''
Написать игру space inviders
1) Добавляем констаны (экран, цвета и т.п)
2) Параметры игрока, параметры врагов, выстрелов
3) Игровые функции и условия
'''
import pygame
import time
import random
import math
import os
from pygame import mixer
from modules import *
pygame.init()
screen = pygame.display.set_mode((800, 600))
#components
game_dir = os.path.dirname(__file__)
components_dir = os.path.join(game_dir,'components')

background = pygame.image.load(os.path.join(components_dir,'background.png'))
enemyImg = pygame.image.load(os.path.join(components_dir,'enemy.png'))
playerImg = pygame.image.load(os.path.join(components_dir,'player.png'))

mixer.music.load(os.path.join(components_dir,'background.wav'))
mixer.music.play(-1)
pygame.display.set_caption('Space invider')
icon = pygame.image.load(os.path.join(components_dir,'ufo.png'))
pygame.display.set_icon(icon)

for i in range(num_of_enemies):
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)

bulletImg = pygame.image.load(os.path.join(components_dir,'bullet.png'))
# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10
 # Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
 
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
 
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
 
def player(x, y):
    screen.blit(playerImg, (x, y))
  
def enemy(x, y):
    screen.blit(enemyImg, (x, y))
 
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound(os.path.join(components_dir,"laser.wav"))
                    bulletSound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                playerX += playerX_change
                if playerX <= 0:
                    playerX = 0
                elif playerX >= 736:
                    playerX = 736
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
 
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()


 

