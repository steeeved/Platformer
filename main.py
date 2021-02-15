import pygame
import random

pygame.init()


window = pygame.display.set_caption("Simple Game")
window = pygame.display.set_mode((500, 500))
font = pygame.font.Font('freesansbold.ttf', 32)

radius = 30
x = 250
y = 500 
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
vel = [10, 10]


jump = False

#enemy
enemy_x = []
global enemy_y 
enemy_y = []
number_of_enemies = 1
enemyimg = []
vel_enemy = []

def spawn_enemy():
    for i in range(number_of_enemies):
        enemyimg.append(pygame.image.load('enemy.png'))
        enemy_x.append(random.randint(10, 450))
        enemy_y.append(random.randint(-10, 0))
        vel_enemy.append(5)
    

def draw_enemy(x, y, i):
    window.blit(enemyimg[i], (x, y))
    pygame.display.update()

        

run = True
while run:
    window.fill ((255,255,255))
    pygame.time.delay(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    

    #keys
    keys = pygame.key.get_pressed()
    
   
    if keys[pygame.K_RIGHT] and x < 500 - radius:
        x += vel[0]
    if keys[pygame.K_LEFT] and x > 0 + radius:
        x -= vel[0]
    if jump is False and keys[pygame.K_UP]:
        jump = True

    if jump is True:
        y -= vel[1] * 4
        vel[1] -= 1
        if vel[1] < -10:
            jump = False
            vel[1] = 10
    
    for i in range(number_of_enemies):
        if enemy_y[i] > 250:
            spawn_enemy()
        enemy_y[i] += vel_enemy[0]
            # enemy_x[i].clear()
            # enemy_x[i].append(random.randint(10, 450))
        draw_enemy(enemy_x[i], enemy_y[i], i)
    
    
    pygame.draw.circle(window, (255, 0, 0), (int(x), int(y - radius)), radius)
    pygame.display.update()
    
pygame.quit()