from turtle import width
import pygame
import os
from pygame import mixer
import time
import random


pygame.font.init()
WIDHT,HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDHT,HEIGHT))

# компоненты
game_dir = os.path.dirname(__file__)
components_dir = os.path.join(game_dir,'components')
# имя и иконка игры
pygame.display.set_caption('Space inviders')
icon = pygame.image.load(os.path.join(components_dir,'ufo.png'))
pygame.display.set_icon(icon)

# загрузка изображения астероида
RED_SPACE_SHIP = pygame.image.load(os.path.join(components_dir,'enemy.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join(components_dir,'enemy.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join(components_dir,'enemy.png'))

# загрузка изображения корабля игрока
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join(components_dir,'player.png'))


# загрузка изображения лазера
RED_LASER = pygame.image.load(os.path.join(components_dir,'bullet.png'))
GREEN_LASER = pygame.image.load(os.path.join(components_dir,'bullet.png'))
BLUE_LASER = pygame.image.load(os.path.join(components_dir,'bullet.png'))
YELLOW_LASER = pygame.image.load(os.path.join(components_dir,'bullet.png'))

# !!!!! фоновая музыка временно закоментированна pygame.error: mixer not initialized
#mixer.music.load(os.path.join(components_dir,'background.wav'))
#mixer.music.play(-1)

# бэкграунд
BG = pygame.transform.scale(pygame.image.load(os.path.join(components_dir,'background.png')), (WIDHT,HEIGHT))

class Laser():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    def move(self, vel):
        self.y += vel
    def off_screen(self, height):
        return self.y <= height and self.y >= 0
    def collision(self, obj):
        return collide(self,obj)



class Ship():
    COOLDOWN = 30
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.enemy_img = None
        self.laser_img = None
        self.ship_img = YELLOW_SPACE_SHIP
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1
    
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(x, y, self.laser_img)
            self.lazers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health 

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs: 
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

class Enemy(Ship):
    COLOR_MAP = {
                "red":(RED_SPACE_SHIP, RED_LASER),
                "green":(GREEN_SPACE_SHIP, GREEN_LASER),
                "blue":(BLUE_SPACE_SHIP, BLUE_LASER)
                }
    
    
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
            self.y += vel

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y- obj1.y
    return obj1.mask.overlap(obj2.mask,(offset_x, offset_y)) !=None

def main(): 
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    global wave_length 
    wave_length = 5
   

    player_vel = 5

    enemy_vel = 1

    player = Player(300,650)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        WIN.blit(BG,(0,0))
        # текст
        lives_label = main_font.render(f"Lives:{lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level:{level}", 1, (255,255,255))

        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDHT- level_label.get_width()-10, 10))

        for enemy in enemies:
            enemy.draw(WIN)
        
        player.draw(WIN)
        if lost:
            lost_label = lost_font.render("You Lost!!!", 1,(255, 255,255))
            WIN.blit(lost_label, (WIDHT/2 - lost.label.get_widht()/2, 350))
        pygame.display.update()
    while run:
        clock.tick(FPS)
        redraw_window()
        wave_length = 5

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        if len(enemies) == 0:
            level += 1
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDHT-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: #влево
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDHT: #вправо
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: #вверх
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT: #вниз
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)


        

main()

