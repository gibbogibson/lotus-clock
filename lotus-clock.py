from datetime import datetime
import pygame, os

os.environ["SDL_FBDEV"] = "/dev/fb1"

pygame.init()

#icon = pygame.image.load('digitalClock.png')
#pygame.display.set_icon(icon)

screen = pygame.display.set_mode((320,240))
#pygame.display.set_caption('Digital Clock')
font = pygame.font.SysFont('Comic Sans MS',150)

s2Img = pygame.image.load('s2_logo.jpeg')

white = (255,255,255)
black = (0,0,0)

screen.blit(s2Img, (10,40))
pygame.display.update()
pygame.time.delay(3000)

running = True
while running:
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
    now = datetime.now()

    minute = now.strftime('%M')
    hour = int(now.strftime('%H'))
    print(hour," : ", minute)
    if hour < 10:
        hour = "0" + str(hour)
    
    time = str(hour) + ":" + str(minute)
    print(time)
    text = font.render(time,True,white)
    screen.blit(text, (10,40))

    pygame.display.update()
 
    
