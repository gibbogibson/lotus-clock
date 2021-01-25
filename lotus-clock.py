from datetime import datetime
import pygame

pygame.init()

#icon = pygame.image.load('digitalClock.png')
#pygame.display.set_icon(icon)

screen = pygame.display.set_mode((320,240))
#pygame.display.set_caption('Digital Clock')
#font = pygame.font.SysFont('Comic Sans MS',130)

white = (255,255,255)
black = (0,0,0)

running = True
while running:
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
    now = datetime.now()

    minute = now.strftime('%M:%S')
    hour = int(now.strftime('%H'))
    
    if hour > 12:
        hour = hour-12
    
    time = f'{hour}:{minute}'

    text = font.render(time,True,white)
    screen.blit(text, (0,0))

    pygame.display.update()
