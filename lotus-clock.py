from datetime import datetime
import pygame, os

os.environ["SDL_FBDEV"] = "/dev/fb1"

pygame.init()
pygame.mouse.set_visible(False)
#icon = pygame.image.load('digitalClock.png')
#pygame.display.set_icon(icon)

screen = pygame.display.set_mode((320,240))
#pygame.display.set_caption('Digital Clock')
font = pygame.font.Font('DS-DIGII.TTF',100)
tempFont = pygame.font.Font('DS-DIGII.TTF',30)

lotusImg = pygame.image.load('lotus_black_320.jpg')
s2Img = pygame.image.load('esprit_s2_logo_250.jpg')
s2SmallImg = pygame.image.load('esprit_s2_logo_125.jpg')

white = (100,255,150)
black = (0,0,0)
#tempColour = (100,255,150)


screen.blit(lotusImg, (0,30))
pygame.display.update()
pygame.time.delay(2000)

screen.fill(black)

#screen.blit(s2Img, (35,40))
#pygame.display.update()
#pygame.time.delay(2000)

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

    screen.blit(s2SmallImg, (95,5))
        
    minute = now.strftime('%M')
    hour = int(now.strftime('%H'))
    #print(hour," : ", minute)
    if hour < 10:
        hour = "0" + str(hour)
    
    month = now.strftime('%m')
    year = now.strftime("%Y")
    day = now.strftime("%d")
    
    time = str(hour) + ":" + str(minute)
    #print(time)
    text = font.render(time,True,white)
    screen.blit(text, (60,70))
    
    date = day + "/" + month + "/" + year
    dateText = tempFont.render(date,True,white)
    screen.blit(dateText, (10,200))
    
    temp = str("10 *C")
    tempText = tempFont.render(temp,True,white)
    screen.blit(tempText, (260,200))
    
    pygame.display.update()
 
    
