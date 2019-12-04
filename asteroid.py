import pygame
import random
import time
lives = 3
score = 0

def drawShip (screen, x, y, ship):
    screen.blit(ship, (x,y))

def drawAsteroid (asteroid, screen, x, y):
    asteroid = pygame.image.load("asteroid.png")
    screen.blit(asteroid, (x, y))

def collision(xship, yship, xaster, yaster):
    if((pointInside(xship, yship, xaster, yaster)) or
       (pointInside(xship + 92, yship, xaster, yaster)) or
       (pointInside(xship, yship + 92, xaster, yaster)) or
       (pointInside(xship+92, yship+92, xaster, yaster)) or
       (pointInside(xship+23, yship, xaster, yaster)) or
       (pointInside(xship+46, yship, xaster, yaster)) or
       (pointInside(xship+69, yship, xaster, yaster)) or
       (pointInside(xship+23, yship+92, xaster, yaster)) or
       (pointInside(xship+46, yship+92, xaster, yaster)) or
       (pointInside(xship+69, yship+92, xaster, yaster)) or
       (pointInside(xship, yship+23, xaster, yaster)) or
       (pointInside(xship, yship+46, xaster, yaster)) or
       (pointInside(xship, yship+69, xaster, yaster)) or
       (pointInside(xship+92, yship+23, xaster, yaster)) or
       (pointInside(xship+92, yship+46, xaster, yaster)) or
       (pointInside(xship+92, yship+69, xaster, yaster))):
         return True

def pointInside(x, y, a, b):
    if (x > a) and (x < a+32) and (y > b) and (y < b+32):
        return True
    else:
        return False

def asteroidPos():
    choice1 = random.randint(1,2)
    choice2 = random.randint(1,2)
    if choice1 == 1:
        x = random.randint(0, screen_width)
        if choice2 == 1:
            y = 0
        elif choice2 == 2:
            y = screen_height
    elif choice1 == 2:
        y = random.randint(0, screen_height)
        if choice2 == 1:
            x = 0
        elif choice2 == 2:
            x = screen_width
    return [x, y]

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('FreeMono', 30)
scoreText1 = myfont.render('Score: ', False, RED)
livesText1 = myfont.render('Lives: ', False, RED)
gameover = myfont.render('Game Over', False, RED)
credit = myfont.render('Game designed by: Lucas', False, RED)
credit2 = myfont.render('Game Art by: Lucas', False, RED)
clock = pygame.time.Clock()
screen_width = 500
screen_height = 400
size = (screen_width,screen_height)
screen = pygame.display.set_mode(size)
background = pygame.image.load('back1.png')
difficulty = 1
ship = pygame.image.load('ship.png')
xship_coord = screen_width * 0.45
yship_coord = screen_height * 0.45
xship_speed = 0
yship_speed = 0
shot = pygame.image
shotxcoord = 0
shotycoord = 0
shotspeedx = 0
shotspeedy = 0
aster1 = pygame.image
aster2 = pygame.image
aster3 = pygame.image
aster4 = pygame.image
aster5 = pygame.image
aster6 = pygame.image
aster7 = pygame.image
aster8 = pygame.image
aster9 = pygame.image
aster10 = pygame.image
asteroid_coord = [asteroidPos(), asteroidPos(), asteroidPos(), asteroidPos(),
                  asteroidPos(), asteroidPos(), asteroidPos(), asteroidPos(),
                  asteroidPos(), asteroidPos()]
aster1xspeed = 0
aster1yspeed = 0
aster2xspeed = 0
aster2yspeed = 0
aster3xpseed = 0
aster3yspeed = 0
aster4xspeed = 0
aster4yspeed = 0
aster5xspeed = 0
aster5yspeed = 0
aster6xpseed = 0
aster6yspeed = 0
aster7xspeed = 0
aster7yspeed = 0
aster8xspeed = 0
aster8yspeed = 0
aster9xpseed = 0
aster9yspeed = 0
aster10xspeed = 0
aster10yspeed = 0
if (asteroid_coord[0][0] > screen_width / 2):
    aster1xspeed = -1
else:
    aster1xspeed = 1
if (asteroid_coord[0][1] > screen_height / 2):
    aster1yspeed = -1
else:
    aster1yspeed = 1

if (asteroid_coord[1][0] > screen_width / 2):
    aster2xspeed = -1
else:
    aster2xspeed = 1
if (asteroid_coord[1][1] > screen_height / 2):
    aster2yspeed = -1
else:
    aster2yspeed = 1

if (asteroid_coord[2][0] > screen_width / 2):
    aster3xspeed = -1
else:
    aster3xspeed = 1
if (asteroid_coord[2][1] > screen_height / 2):
    aster3yspeed = -1
else:
    aster3yspeed = 1
if (asteroid_coord[3][0] > screen_width / 2):
    aster4xspeed = -1
else:
    aster4xspeed = 1
if (asteroid_coord[3][1] > screen_height / 2):
    aster4yspeed = -1
else:
    aster4yspeed = 1

if (asteroid_coord[4][0] > screen_width / 2):
    aster5xspeed = -1
else:
    aster5xspeed = 1
if (asteroid_coord[4][1] > screen_height / 2):
    aster5yspeed = -1
else:
    aster5yspeed = 1

if (asteroid_coord[5][0] > screen_width / 2):
    aster6xspeed = -1
else:
    aster6xspeed = 1
if (asteroid_coord[5][1] > screen_height / 2):
    aster6yspeed = -1
else:
    aster6yspeed = 1
if (asteroid_coord[6][0] > screen_width / 2):
    aster7xspeed = -1
else:
    aster7xspeed = 1
if (asteroid_coord[6][1] > screen_height / 2):
    aster7yspeed = -1
else:
    aster7yspeed = 1

if (asteroid_coord[7][0] > screen_width / 2):
    aster8xspeed = -1
else:
    aster8xspeed = 1
if (asteroid_coord[7][1] > screen_height / 2):
    aster8yspeed = -1
else:
    aster8yspeed = 1

if (asteroid_coord[8][0] > screen_width / 2):
    aster9xspeed = -1
else:
    aster9xspeed = 1
if (asteroid_coord[8][1] > screen_height / 2):
    aster9yspeed = -1
else:
    aster9yspeed = 1
if (asteroid_coord[9][0] > screen_width / 2):
    aster10xspeed = -1
else:
    aster10xspeed = 1
if (asteroid_coord[9][1] > screen_height / 2):
    aster10yspeed = -1
else:
    aster10yspeed = 1
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship = pygame.image.load('shipleft.png')
                xship_speed = -6
            elif event.key == pygame.K_RIGHT:
                ship = pygame.image.load('shipright.png')
                xship_speed = 6
            elif event.key == pygame.K_UP:
                ship = pygame.image.load('ship.png')
                yship_speed = -6
            elif event.key == pygame.K_DOWN:
                ship = pygame.image.load('shipdown.png')
                yship_speed = 6
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xship_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                yship_speed = 0
    xship_coord += xship_speed
    yship_coord += yship_speed
    scoreText2 = myfont.render(str(score), False, RED)
    livesText2 = myfont.render(str(lives), False, RED)
    if(score >= 1000):
        diffuculty = 3
    elif(score >= 300):
        difficulty = 2
    if(difficulty == 3):
        background = pygame.image.load('back3.png')
        if asteroid_coord[0][0] < 0 or asteroid_coord[0][0] > screen_width or asteroid_coord[0][1] < 0 or asteroid_coord[0][1] > screen_height:
            asteroid_coord[0] = asteroidPos()
            score += 10
            if (asteroid_coord[0][0] > screen_width / 2):
                aster1xspeed = -3
            else:
                aster1xspeed = 3
            if (asteroid_coord[0][1] > screen_height / 2):
                aster1yspeed = -3
            else:
                aster1yspeed = 3
        if asteroid_coord[1][0] < 0 or asteroid_coord[1][0] > screen_width or asteroid_coord[1][1] < 0 or asteroid_coord[1][1] > screen_height:
            asteroid_coord[1] = asteroidPos()
            score += 10
            if (asteroid_coord[1][0] > screen_width / 2):
                aster1xspeed = -3
            else:
                aster1xspeed = 3
            if (asteroid_coord[1][1] > screen_height / 2):
                aster1yspeed = -3
            else:
                aster1yspeed = 3
        if asteroid_coord[2][0] < 0 or asteroid_coord[2][0] > screen_width or asteroid_coord[2][1] < 0 or asteroid_coord[2][1] > screen_height:
            asteroid_coord[2] = asteroidPos()
            score += 10
            if (asteroid_coord[2][0] > screen_width / 2):
                aster3xspeed = -3
            else:
                aster3xspeed = 3
            if (asteroid_coord[2][1] > screen_height / 2):
                aster3yspeed = -3
            else:
                aster3yspeed = 3
        if asteroid_coord[3][0] < 0 or asteroid_coord[3][0] > screen_width or asteroid_coord[3][1] < 0 or asteroid_coord[3][1] > screen_height:
            asteroid_coord[3] = asteroidPos()
            score += 10
            if (asteroid_coord[3][0] > screen_width / 2):
                aster4xspeed = -3
            else:
                aster4xspeed = 3
            if (asteroid_coord[3][1] > screen_height / 2):
                aster4yspeed = -3
            else:
                aster4yspeed = 3
        if asteroid_coord[4][0] < 0 or asteroid_coord[4][0] > screen_width or asteroid_coord[4][1] < 0 or asteroid_coord[4][1] > screen_height:
            asteroid_coord[4] = asteroidPos()
            score += 10
            if (asteroid_coord[4][0] > screen_width / 2):
                aster5xspeed = -3
            else:
                aster5xspeed = 3
            if (asteroid_coord[4][1] > screen_height / 2):
                aster5yspeed = -3
            else:
                aster5yspeed = 3
        if asteroid_coord[5][0] < 0 or asteroid_coord[5][0] > screen_width or asteroid_coord[5][1] < 0 or asteroid_coord[5][1] > screen_height:
            asteroid_coord[5] = asteroidPos()
            score += 10
            if (asteroid_coord[5][0] > screen_width / 2):
                aster6xspeed = -3
            else:
                aster6xspeed = 3
            if (asteroid_coord[5][1] > screen_height / 2):
                aster6yspeed = -3
            else:
                aster6yspeed = 3
        if asteroid_coord[6][0] < 0 or asteroid_coord[6][0] > screen_width or asteroid_coord[6][1] < 0 or asteroid_coord[6][1] > screen_height:
            asteroid_coord[6] = asteroidPos()
            score += 10
            if (asteroid_coord[6][0] > screen_width / 2):
                aster7xspeed = -3
            else:
                aster7xspeed = 3
            if (asteroid_coord[6][1] > screen_height / 2):
                aster7yspeed = -3
            else:
                aster7yspeed = 3
        if asteroid_coord[7][0] < 0 or asteroid_coord[7][0] > screen_width or asteroid_coord[7][1] < 0 or asteroid_coord[7][1] > screen_height:
            asteroid_coord[7] = asteroidPos()
            score += 10
            if(asteroid_coord[7][0] > screen_width / 2):
                aster8xspeed = -3
            else:
                aster8xspeed = 3
            if (asteroid_coord[7][1] > screen_height / 2):
                aster8yspeed = -3
            else:
                aster8yspeed = 3
        if asteroid_coord[8][0] < 0 or asteroid_coord[8][0] > screen_width or asteroid_coord[8][1] < 0 or asteroid_coord[8][1] > screen_height:
            asteroid_coord[8] = asteroidPos()
            score += 10
            if (asteroid_coord[8][0] > screen_width / 2):
                aster9xspeed = -3
            else:
                aster9xspeed = 3
            if (asteroid_coord[8][1] > screen_height / 2):
                aster9yspeed = -3
            else:
                aster9yspeed = 3
        if asteroid_coord[9][0] < 0 or asteroid_coord[9][0] > screen_width or asteroid_coord[9][1] < 0 or asteroid_coord[9][1] > screen_height:
            asteroid_coord[9] = asteroidPos()
            score += 10
            if (asteroid_coord[9][0] > screen_width / 2):
                aster10xspeed = -3
            else:
                aster10xspeed = 3
            if (asteroid_coord[9][1] > screen_height / 2):
                aster10yspeed = -3
            else:
                aster10yspeed = 3
        if lives == 0:
            print('Game Over')
            screen.fill(BLACK)
            screen.blit(gameover, (screen_width * .40, screen_height *.45))
            screen.blit(scoreText1, (screen_width * .40, screen_height *.80))
            screen.blit(scoreText2, (screen_width * .70, screen_height *.80))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(5)
            screen.fill(BLACK)
            screen.blit(credit, (screen_width * .10, screen_height *.45))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(5)
            screen.fill(BLACK)
            screen.blit(credit2, (screen_width * .10, screen_height *.45))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(5)
            break
        if(collision(xship_coord, yship_coord, asteroid_coord[0][0], asteroid_coord[0][1])):
            lives -= 1
            asteroid_coord[0] = asteroidPos()
            if (asteroid_coord[0][0] > screen_width / 2):
                aster1xspeed = -3
            else:
                aster1xspeed = 3
            if (asteroid_coord[0][1] > screen_height / 2):
                aster1yspeed = -3
            else:
                aster1yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[1][0], asteroid_coord[1][1])):
            lives -= 1
            asteroid_coord[1] = asteroidPos()
            if (asteroid_coord[1][0] > screen_width / 2):
                aster2xspeed = -3
            else:
                aster2xspeed = 3
            if (asteroid_coord[1][1] > screen_height / 2):
                aster2yspeed = -3
            else:
                aster2yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[2][0], asteroid_coord[2][1])):
            lives -= 1
            asteroid_coord[2] = asteroidPos()
            if (asteroid_coord[2][0] > screen_width / 2):
                aster3xspeed = -3
            else:
                aster3xspeed = 3
            if (asteroid_coord[2][1] > screen_height / 2):
                aster3yspeed = -3
            else:
                aster3yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[3][0], asteroid_coord[3][1])):
            lives -= 1
            asteroid_coord[3] = asteroidPos()
            if (asteroid_coord[3][0] > screen_width / 2):
                aster4xspeed = -3
            else:
                aster4xspeed = 3
            if (asteroid_coord[3][1] > screen_height / 2):
                aster4yspeed = -3
            else:
                aster4yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[4][0], asteroid_coord[4][1])):
            lives -= 1
            asteroid_coord[4] = asteroidPos()
            if (asteroid_coord[4][0] > screen_width / 2):
                aster5xspeed = -3
            else:
                aster5xspeed = 3
            if (asteroid_coord[4][1] > screen_height / 2):
                aster5yspeed = -3
            else:
                aster5yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[5][0], asteroid_coord[5][1])):
            lives -= 1
            asteroid_coord[5] = asteroidPos()
            if (asteroid_coord[5][0] > screen_width / 2):
                aster6xspeed = -3
            else:
                aster6xspeed = 3
            if (asteroid_coord[5][1] > screen_height / 2):
                aster6yspeed = -3
            else:
                aster6yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[6][0], asteroid_coord[6][1])):
            lives -= 1
            asteroid_coord[6] = asteroidPos()
            if (asteroid_coord[6][0] > screen_width / 2):
                aster7xspeed = -3
            else:
                aster7xspeed = 3
            if (asteroid_coord[6][1] > screen_height / 2):
                aster7yspeed = -3
            else:
                aster7yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[7][0], asteroid_coord[7][1])):
            lives -= 1
            asteroid_coord[7] = asteroidPos()
            if (asteroid_coord[7][0] > screen_width / 2):
                aster8xspeed = -3
            else:
                aster8xspeed = 3
            if (asteroid_coord[7][1] > screen_height / 2):
                aster8yspeed = -3
            else:
                aster8yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[8][0], asteroid_coord[8][1])):
            lives -= 1
            asteroid_coord[8] = asteroidPos()
            if (asteroid_coord[8][0] > screen_width / 2):
                aster9xspeed = -3
            else:
                aster9xspeed = 3
            if (asteroid_coord[8][1] > screen_height / 2):
                aster9yspeed = -3
            else:
                aster9yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[9][0], asteroid_coord[9][1])):
            lives -= 1
            asteroid_coord[9] = asteroidPos()
            if (asteroid_coord[9][0] > screen_width / 2):
                aster10xspeed = -3
            else:
                aster10xspeed = 3
            if (asteroid_coord[9][1] > screen_height / 2):
                aster10yspeed = -3
            else:
                aster10yspeed = 3
        asteroid_coord[0][0] += aster1xspeed
        asteroid_coord[0][1] += aster1yspeed
        asteroid_coord[1][0] += aster2xspeed
        asteroid_coord[1][1] += aster2yspeed
        asteroid_coord[2][0] += aster3xspeed
        asteroid_coord[2][1] += aster3yspeed
        asteroid_coord[0][0] += aster4xspeed
        asteroid_coord[0][1] += aster4yspeed
        asteroid_coord[1][0] += aster5xspeed
        asteroid_coord[1][1] += aster5yspeed
        asteroid_coord[2][0] += aster6xspeed
        asteroid_coord[2][1] += aster6yspeed
        asteroid_coord[0][0] += aster7xspeed
        asteroid_coord[0][1] += aster7yspeed
        asteroid_coord[1][0] += aster8xspeed
        asteroid_coord[1][1] += aster8yspeed
        asteroid_coord[2][0] += aster9xspeed
        asteroid_coord[2][1] += aster9yspeed
        asteroid_coord[2][0] += aster10xspeed
        asteroid_coord[2][1] += aster10yspeed
    elif(difficulty == 2):
        background = pygame.image.load('back2.png')
        if asteroid_coord[0][0] < 0 or asteroid_coord[0][0] > screen_width or asteroid_coord[0][1] < 0 or asteroid_coord[0][1] > screen_height:
            asteroid_coord[0] = asteroidPos()
            score += 10
            if (asteroid_coord[0][0] > screen_width / 2):
                aster1xspeed = -3
            else:
                aster1xspeed = 3
            if (asteroid_coord[0][1] > screen_height / 2):
                aster1yspeed = -3
            else:
                aster1yspeed = 3
        if asteroid_coord[1][0] < 0 or asteroid_coord[1][0] > screen_width or asteroid_coord[1][1] < 0 or asteroid_coord[1][1] > screen_height:
            asteroid_coord[1] = asteroidPos()
            score += 10
            if (asteroid_coord[1][0] > screen_width / 2):
                aster1xspeed = -3
            else:
                aster1xspeed = 3
            if (asteroid_coord[1][1] > screen_height / 2):
                aster1yspeed = -3
            else:
                aster1yspeed = 3
        if asteroid_coord[2][0] < 0 or asteroid_coord[2][0] > screen_width or asteroid_coord[2][1] < 0 or asteroid_coord[2][1] > screen_height:
            asteroid_coord[2] = asteroidPos()
            score += 10
            if (asteroid_coord[2][0] > screen_width / 2):
                aster3xspeed = -3
            else:
                aster3xspeed = 3
            if (asteroid_coord[2][1] > screen_height / 2):
                aster3yspeed = -3
            else:
                aster3yspeed = 3
        if asteroid_coord[3][0] < 0 or asteroid_coord[3][0] > screen_width or asteroid_coord[3][1] < 0 or asteroid_coord[3][1] > screen_height:
            asteroid_coord[3] = asteroidPos()
            score += 10
            if (asteroid_coord[3][0] > screen_width / 2):
                aster4xspeed = -3
            else:
                aster4xspeed = 3
            if (asteroid_coord[3][1] > screen_height / 2):
                aster4yspeed = -3
            else:
                aster4yspeed = 3
        if asteroid_coord[4][0] < 0 or asteroid_coord[4][0] > screen_width or asteroid_coord[4][1] < 0 or asteroid_coord[4][1] > screen_height:
            asteroid_coord[4] = asteroidPos()
            score += 10
            if (asteroid_coord[4][0] > screen_width / 2):
                aster5xspeed = -3
            else:
                aster5xspeed = 3
            if (asteroid_coord[4][1] > screen_height / 2):
                aster5yspeed = -3
            else:
                aster5yspeed = 3
        if asteroid_coord[5][0] < 0 or asteroid_coord[5][0] > screen_width or asteroid_coord[5][1] < 0 or asteroid_coord[5][1] > screen_height:
            asteroid_coord[5] = asteroidPos()
            score += 10
            if (asteroid_coord[5][0] > screen_width / 2):
                aster6xspeed = -3
            else:
                aster6xspeed = 3
            if (asteroid_coord[5][1] > screen_height / 2):
                aster6yspeed = -3
            else:
                aster6yspeed = 3
        if lives == 0:
            print('Game Over')
            screen.fill(BLACK)
            screen.blit(gameover, (screen_width * .40, screen_height *.45))
            screen.blit(scoreText1, (screen_width * .40, screen_height *.80))
            screen.blit(scoreText2, (screen_width * .70, screen_height *.80))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(5)
            screen.fill(BLACK)
            screen.blit(credit, (screen_width * .10, screen_height *.45))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(5)
            screen.fill(BLACK)
            screen.blit(credit2, (screen_width * .10, screen_height *.45))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(5)
            break
        if(collision(xship_coord, yship_coord, asteroid_coord[0][0], asteroid_coord[0][1])):
            lives -= 1
            asteroid_coord[0] = asteroidPos()
            if (asteroid_coord[0][0] > screen_width / 2):
                aster1xspeed = -3
            else:
                aster1xspeed = 3
            if (asteroid_coord[0][1] > screen_height / 2):
                aster1yspeed = -3
            else:
                aster1yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[1][0], asteroid_coord[1][1])):
            lives -= 1
            asteroid_coord[1] = asteroidPos()
            if (asteroid_coord[1][0] > screen_width / 2):
                aster2xspeed = -3
            else:
                aster2xspeed = 3
            if (asteroid_coord[1][1] > screen_height / 2):
                aster2yspeed = -3
            else:
                aster2yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[2][0], asteroid_coord[2][1])):
            lives -= 1
            asteroid_coord[2] = asteroidPos()
            if (asteroid_coord[2][0] > screen_width / 2):
                aster3xspeed = -3
            else:
                aster3xspeed = 3
            if (asteroid_coord[2][1] > screen_height / 2):
                aster3yspeed = -3
            else:
                aster3yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[3][0], asteroid_coord[3][1])):
            lives -= 1
            asteroid_coord[3] = asteroidPos()
            if (asteroid_coord[3][0] > screen_width / 2):
                aster4xspeed = -3
            else:
                aster4xspeed = 3
            if (asteroid_coord[3][1] > screen_height / 2):
                aster4yspeed = -3
            else:
                aster4yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[4][0], asteroid_coord[4][1])):
            lives -= 1
            asteroid_coord[4] = asteroidPos()
            if (asteroid_coord[4][0] > screen_width / 2):
                aster5xspeed = -3
            else:
                aster5xspeed = 3
            if (asteroid_coord[4][1] > screen_height / 2):
                aster5yspeed = -3
            else:
                aster5yspeed = 3
        if(collision(xship_coord, yship_coord, asteroid_coord[5][0], asteroid_coord[5][1])):
            lives -= 1
            asteroid_coord[5] = asteroidPos()
            if (asteroid_coord[5][0] > screen_width / 2):
                aster6xspeed = -3
            else:
                aster6xspeed = 3
            if (asteroid_coord[5][1] > screen_height / 2):
                aster6yspeed = -3
            else:
                aster6yspeed = 3
        asteroid_coord[0][0] += aster1xspeed
        asteroid_coord[0][1] += aster1yspeed
        asteroid_coord[1][0] += aster2xspeed
        asteroid_coord[1][1] += aster2yspeed
        asteroid_coord[2][0] += aster3xspeed
        asteroid_coord[2][1] += aster3yspeed
        asteroid_coord[0][0] += aster4xspeed
        asteroid_coord[0][1] += aster4yspeed
        asteroid_coord[1][0] += aster5xspeed
        asteroid_coord[1][1] += aster5yspeed
        asteroid_coord[2][0] += aster6xspeed
        asteroid_coord[2][1] += aster6yspeed
    elif(difficulty == 1):
        asteroid_coord[0][0] += aster1xspeed
        asteroid_coord[0][1] += aster1yspeed
        asteroid_coord[1][0] += aster2xspeed
        asteroid_coord[1][1] += aster2yspeed
        asteroid_coord[2][0] += aster3xspeed
        asteroid_coord[2][1] += aster3yspeed
        if asteroid_coord[0][0] < 0 or asteroid_coord[0][0] > screen_width or asteroid_coord[0][1] < 0 or asteroid_coord[0][1] > screen_height:
            asteroid_coord[0] = asteroidPos()
            score += 10
            if (asteroid_coord[0][0] > screen_width / 2):
                aster1xspeed = -2
            else:
                aster1xspeed = 2
            if (asteroid_coord[0][1] > screen_height / 2):
                aster1yspeed = -2
            else:
                aster1yspeed = 2
        if asteroid_coord[1][0] < 0 or asteroid_coord[1][0] > screen_width or asteroid_coord[1][1] < 0 or asteroid_coord[1][1] > screen_height:
            asteroid_coord[1] = asteroidPos()
            score += 10
            if (asteroid_coord[1][0] > screen_width / 2):
                aster1xspeed = -2
            else:
                aster1xspeed = 2
            if (asteroid_coord[1][1] > screen_height / 2):
                aster1yspeed = -2
            else:
                aster1yspeed = 2
        if asteroid_coord[2][0] < 0 or asteroid_coord[2][0] > screen_width or asteroid_coord[2][1] < 0 or asteroid_coord[2][1] > screen_height:
            asteroid_coord[2] = asteroidPos()
            score += 10
            if (asteroid_coord[2][0] > screen_width / 2):
                aster3xspeed = -2
            else:
                aster3xspeed = 2
            if (asteroid_coord[2][1] > screen_height / 2):
                aster3yspeed = -2
            else:
                aster3yspeed = 2
        if lives == 0:
            print('Game Over')
            screen.fill(BLACK)
            screen.blit(gameover, (screen_width * .40, screen_height *.45))
            screen.blit(scoreText1, (screen_width * .40, screen_height *.80))
            screen.blit(scoreText2, (screen_width * .70, screen_height *.80))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(5)
            screen.fill(BLACK)
            screen.blit(credit, (screen_width * .10, screen_height *.45))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(5)
            screen.fill(BLACK)
            screen.blit(credit2, (screen_width * .10, screen_height *.45))
            pygame.display.update()
            pygame.display.flip()
            time.sleep(5)
            break
        if(collision(xship_coord, yship_coord, asteroid_coord[0][0], asteroid_coord[0][1])):
            lives -= 1
            asteroid_coord[0] = asteroidPos()
            if (asteroid_coord[0][0] > screen_width / 2):
                aster1xspeed = -2
            else:
                aster1xspeed = 2
            if (asteroid_coord[0][1] > screen_height / 2):
                aster1yspeed = -2
            else:
                aster1yspeed = 2
        if(collision(xship_coord, yship_coord, asteroid_coord[1][0], asteroid_coord[1][1])):
            lives -= 1
            asteroid_coord[1] = asteroidPos()
            if (asteroid_coord[1][0] > screen_width / 2):
                aster2xspeed = -2
            else:
                aster2xspeed = 2
            if (asteroid_coord[1][1] > screen_height / 2):
                aster2yspeed = -2
            else:
                aster2yspeed = 2
        if(collision(xship_coord, yship_coord, asteroid_coord[2][0], asteroid_coord[2][1])):
            lives -= 1
            asteroid_coord[2] = asteroidPos()
            if (asteroid_coord[2][0] > screen_width / 2):
                aster3xspeed = -2
            else:
                aster3xspeed = 2
            if (asteroid_coord[2][1] > screen_height / 2):
                aster3yspeed = -2
            else:
                aster3yspeed = 2
    screen.fill(BLACK)
    screen.blit(background, (0,0))
    drawShip(screen, xship_coord, yship_coord, ship)
    if(difficulty == 3):
        drawAsteroid(aster1, screen, asteroid_coord[0][0], asteroid_coord[0][1])
        drawAsteroid(aster2, screen, asteroid_coord[1][0], asteroid_coord[1][1])
        drawAsteroid(aster3, screen, asteroid_coord[2][0], asteroid_coord[2][1])
        drawAsteroid(aster4, screen, asteroid_coord[3][0], asteroid_coord[3][1])
        drawAsteroid(aster5, screen, asteroid_coord[4][0], asteroid_coord[4][1])
        drawAsteroid(aster6, screen, asteroid_coord[5][0], asteroid_coord[5][1])
        drawAsteroid(aster7, screen, asteroid_coord[6][0], asteroid_coord[6][1])
        drawAsteroid(aster8, screen, asteroid_coord[7][0], asteroid_coord[7][1])
        drawAsteroid(aster9, screen, asteroid_coord[8][0], asteroid_coord[8][1])
        drawAsteroid(aster10, screen, asteroid_coord[9][0], asteroid_coord[9][1])
    elif(difficulty == 2):
        drawAsteroid(aster1, screen, asteroid_coord[0][0], asteroid_coord[0][1])
        drawAsteroid(aster2, screen, asteroid_coord[1][0], asteroid_coord[1][1])
        drawAsteroid(aster3, screen, asteroid_coord[2][0], asteroid_coord[2][1])
        drawAsteroid(aster4, screen, asteroid_coord[3][0], asteroid_coord[3][1])
        drawAsteroid(aster5, screen, asteroid_coord[4][0], asteroid_coord[4][1])
        drawAsteroid(aster6, screen, asteroid_coord[5][0], asteroid_coord[5][1])
    elif(difficulty == 1):
        drawAsteroid(aster1, screen, asteroid_coord[0][0], asteroid_coord[0][1])
        drawAsteroid(aster2, screen, asteroid_coord[1][0], asteroid_coord[1][1])
        drawAsteroid(aster3, screen, asteroid_coord[2][0], asteroid_coord[2][1])
    screen.blit(scoreText1, (5,5))
    screen.blit(scoreText2, (125, 5))
    screen.blit(livesText1, (screen_width - 125, 5))
    screen.blit(livesText2, (screen_width -25, 5))
    pygame.display.update()
    clock.tick(30)
pygame.quit()
