import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

red = (255, 0, 0)
white = (255, 255, 255)

x = 350
y = 350
step = 20
radius = 25
clock = pygame.time.Clock()
    
done = False
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        if y - step >= 20:
            y -= step
        else:
            y = 20
    elif pressed[pygame.K_DOWN]: 
        if y + step <= 480:
            y += step
        else:
            y = 480
    elif pressed[pygame.K_LEFT]: 
        if x - step >= 20:
            x -= step
        else:
            x = 20
    elif pressed[pygame.K_RIGHT]: 
        if x + step <= 480:
            x += step
        else:
            x = 480
    screen.fill(white)
    pygame.draw.circle(screen, red, (x,y), radius) #ball

    pygame.display.flip()
    clock.tick(60)