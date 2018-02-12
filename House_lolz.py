# Imports
import pygame
import math
import random

# Initialize game engine
pygame.mixer.pre_init()
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
red = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (23, 102, 15)
BLUE = (0, 15, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLACK = (5, 5, 5)
ORANGE = (255, 125 , 0)
PURPLE = (125, 0, 125)
BROWN = (102, 47, 0)
LIGHT_BROWN = (147, 108, 10)
LIGHT_YELLOW = (255, 255, 140)
YELLOW = (255, 236, 35)
DARK_BLUE =(27, 26, 38)
LIGHT_BLUE = (0, 255, 242)
LIGHT_GRAY = (168, 168, 168)
GRAY = (95, 95, 95)
WHITE = (255,255,255)
WHITE_GREEN = (219, 255, 219)
GRAY_GREEN = (57, 71, 56)

#PRE-SETS
Clear = False
stormy = True
day = False
night = True
lights_on = True
lights_off = False

print("SPACE controls the weather")
print("SHIFT controls the time of day")
print("ALT controls the street and house lights")

#SFX
flowers = pygame.mixer.music.load("flowers.ogg")
thunder = pygame.mixer.Sound("thunder.ogg")

#BLOCK_STAT

m_loc = [380, 280]
vel = [0,0]
speed = 2
UFO = pygame.image.load('UFO.png')

def draw_move(m_loc):
    x = m_loc[0]
    y = m_loc[1]
    screen.blit(UFO, (x, y))

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, LIGHT_GRAY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, LIGHT_GRAY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, LIGHT_GRAY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, LIGHT_GRAY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, LIGHT_GRAY, [x + 20, y + 20, 60, 40])

def draw_grass(loc_g):
    x, y = loc_g
    pygame.draw.polygon(screen, GREEN, [[x+x/75, y],[x, y+y/25], [x+5, y+y/25]])
    

def draw_tree(x, y):
    pygame.draw.polygon(screen, GREEN, [[x+50, y],[x, y+150], [x+100, y+150]])

def draw_fence(y):
    for x in range(5,800,30):
        post = [x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]

        pygame.draw.polygon(screen, WHITE, post)

    pygame.draw.rect(screen, WHITE, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y+30, 800, 5])

def draw_door(x,y):
    pygame.draw.circle(screen, LIGHT_BROWN, [x+10, y-10], 20)
    pygame.draw.rect(screen, LIGHT_BROWN, [x-9.33, y-10, 40, 60])
    pygame.draw.circle(screen, BLACK, [x+22, y+5], 5)

def draw_window(y):
    for x in range(565, 720,30):
        if lights_off:
            pygame.draw.rect(screen, LIGHT_GRAY, [x, y, 20, 20])
        elif lights_on:
            pygame.draw.rect(screen, YELLOW, [x, y, 20, 20])
        pygame.draw.rect(screen, BLACK, [x, y, 20, 2])
        pygame.draw.rect(screen, BLACK, [x, y, 2, 20])
        pygame.draw.rect(screen, BLACK, [x, y+18, 20, 2])
        pygame.draw.rect(screen, BLACK, [x+18, y, 2, 20])
        pygame.draw.rect(screen, BLACK, [x+9, y, 2, 20])
        pygame.draw.rect(screen, BLACK, [x, y+9, 20, 2])

def draw_back_clouds(bgc_loc):
    x = bgc_loc[0]
    y = bgc_loc[1]
    
    pygame.draw.ellipse(screen, GRAY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GRAY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GRAY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GRAY, [x + 20, y + 20, 60, 40])

def draw_star(star_loc):
    x = star_loc[0]
    y = star_loc[1]

    pygame.draw.rect(screen, LIGHT_YELLOW, [x, y, 10, 10])

background_clouds = []
for i in range(40):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 350)
    bgc_loc = [x, y]
    background_clouds.append(bgc_loc)

rain = []
for i in range(1000):
    x = random.randrange(0, 800)
    y = random.randrange(50, 500)
    r = random.randrange(1, 5)
    n = [x, y, r, r]
    rain.append(n)

clouds = []
for i in range(20):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 225)
    loc = [x, y]
    clouds.append(loc)

grass_loc = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(455, 475)
    loc_g = [x, y]
    grass_loc.append(loc_g)

star = []
x = 810
y = 30
star_loc = [x, y]
star.append(star_loc)

# Game loop
pygame.mixer.music.play(-1)

done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel[0] = speed
            if event.key == pygame.K_UP:
                vel[1] = (speed * -1)
            if event.key == pygame.K_LEFT:
                vel[0] = (speed * -1)
            if event.key == pygame.K_DOWN:
                vel[1] = speed
            if event.key == pygame.K_SPACE:
                if stormy:
                    stormy = False
                    clear = True
                elif clear:
                    stormy = True
                    clear = False
            if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                if night:
                    night = False
                    day = True
                elif day:
                    night = True
                    day = False
            if event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                if lights_on:
                    lights_on = False
                    lights_off = True
                elif lights_off:
                    lights_on = True
                    lights_off = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                vel[0] = 0
            if event.key == pygame.K_UP:
                vel[1] = 0
            if event.key == pygame.K_LEFT:
                vel[0] = 0
            if event.key == pygame.K_DOWN:
                vel[1] = 0


    # Game logic (Check for collisions, update points, etc.)
    m_loc[0] += vel[0]
    m_loc[1] += vel[1]
    
    for c in background_clouds:
        c[0] += 1
        
        if stormy:
            if c[0] > 900:
               c[0] = random.randrange(-900, -100)
               c[1] = random.randrange(-50, 350)
    if night:
        for s in star:
            s[0] -= 20
            s[1] += 1

            if s[0] == -1000:
                s[0] = 810
                s[1] = 30
    elif day:
        if s[0] > 0 and s[0] < 800:
            s[0] = 810
            s[1] = 30

    for c in clouds:
        c[0] += 2

        if c[0] > 900:
           c[0] = random.randrange(-200, -100)
           c[1] = random.randrange(-50, 255)
    
    for n in rain:
        n[1] += 5
        n[0] += 1
        drop = random.randrange(400, 800)

        if stormy:
            if n[1] > drop:
                n[0] = random.randrange(-100, 800)
                n[1] = random.randrange(-400, -1)

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    '''flash lighning'''
    lightning_timer = 0
    if stormy:
        if random.randrange(0, 150) == 0:
            lightning_timer = 5
            thunder.play()
        else:
            lightning_timer -= 1
    '''sky'''
    
    if lightning_timer > 0:
        screen.fill(YELLOW)
    elif night:
        screen.fill(DARK_BLUE)
    if day:
        screen.fill(LIGHT_BLUE)

    '''star'''
    for s in star:
        draw_star(star_loc)

    '''Moon'''
    pygame.draw.circle(screen, LIGHT_YELLOW, [800, 0], 100, 0)

    '''rain'''
    for n in rain:
        pygame.draw.ellipse(screen, BLUE, n)

    '''background_clouds'''
    for bgc_loc in background_clouds:
        draw_back_clouds(bgc_loc)

    '''tree'''
    draw_tree(313, 274)

    '''house'''
    pygame.draw.rect(screen, red, [550, 300, 200, 175])
    draw_door(640,425)
    draw_window(350)
    pygame.draw.rect(screen, BROWN, [325, 425, 75, 50])
    pygame.draw.polygon(screen, ORANGE, [[525, 300], [775,300], [650, 175]])

    '''street light'''
    pygame.draw.rect(screen, GRAY_GREEN, [100, 250, 20, 225])
    pygame.draw.arc(screen, GRAY_GREEN, [100, 225, 65, 65], 0, math.pi, 20)
    if lights_off:
        pygame.draw.circle(screen, LIGHT_GRAY, [155, 268], 9, 0)
    elif lights_on:
        pygame.draw.circle(screen, YELLOW, [155, 268], 9, 0)
    pygame.draw.polygon(screen, GRAY_GREEN, ((144, 258), (164, 258), (170, 268), (140, 268)))

    '''clouds'''
    for loc in clouds:
        draw_cloud(loc)

    '''grass'''
    for loc_g in grass_loc:
        draw_grass(loc_g)

    '''movement'''
    draw_move(m_loc)

    '''ground'''
    pygame.draw.rect(screen, BROWN, [0, 500, 800, 100])
    pygame.draw.rect(screen, DARK_GREEN, [0, 475, 800, 25, ])

    '''fence'''
    draw_fence(450)

    '''lights'''
    Dark = pygame.Surface(SIZE)
    Dark.set_alpha(150)
    Dark.fill((0, 0, 0))

    if night and lights_off:
        screen.blit(Dark, (0, 0))

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
