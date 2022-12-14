import pygame
import time
import random
from colors import *
from display import displ_width, displ_height
from snake import *
"""
Snake game using pygame
 
"""
 # окно
displ = pygame.display.set_mode((displ_width, displ_height))
# инициализация
pygame.init()
 
# подпись сверху
pygame.display.set_caption("SNAKE")
clock = pygame.time.Clock()
 # функция для экранных сообщений
font_style = pygame.font.SysFont(None, 50)
 
def message(msg, color):
    # рисуем текст
    mesg = font_style.render(msg, True, color)
    # тут меняем позицию текста, если надо
    displ.blit(mesg, [displ_width / 3, displ_height / 3])

def game_loop():
    # флаг game_over
    game_over = False
    # флаг game_close
    game_close = False
 
    # coords
    x1 = displ_width / 2
    y1 = displ_height / 2
 
    x1_change = 0
    y1_change = 0
 
    # coords для еды
    food_x = round(random.randrange(0, displ_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, displ_width - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            displ.fill(white)
            message("LOOSE, q-to quit, c-play again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        # условия проигрыша
        if x1 >= displ_width or x1 < 0 or y1 >= displ_height or y1 < 0:
            game_over = True
 
        x1 += x1_change
        y1 += y1_change
        displ.fill(white)
        # змея и еда
        pygame.draw.rect(displ, black, [food_x, food_y, snake_block, snake_block])
        pygame.draw.rect(displ, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()
 
        # скорость змеи = фпс
        if x1 == food_x and y1 == food_y:
            print("Yummy!!")
        clock.tick(snake_speed)
        
    pygame.quit()
    quit()
game_loop()