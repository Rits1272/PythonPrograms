import pygame
import time
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
pause_score = 0
added_speed = 0

surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bit Racy")

white = (255,255,255)
black = (0,0,0)
green = (0,150,0)
red = (255,0,0)
blue = (0,0,100)
bright_blue = (0,0,255)
bright_green = (0,255,0)

clock = pygame.time.Clock()
carImg = pygame.image.load('car_resize.png')
car_width = 40


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(surface, color, [thingx,thingy,thingw,thingh])

def thingsDodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged : '+str(count), True, green)
    surface.blit(text, (0,0))

def car(x, y):
    surface.blit(carImg, (x,y)) #blit(text/image, text/image position)

def text_objects(text, font):
    textSurface = font.render(text, True, black) #bold = True
    return textSurface, textSurface.get_rect() #get_rect creates a rectangle with the size of the content with pos_x, pos_y = 0

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115) # pygame.font.Font creates a new Font object from a file.
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH/2, HEIGHT/2))
    surface.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    gameloop()

def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    
    largeText = pygame.font.SysFont('comicsansms',115)
    TextSurf, TextRect = text_objects('You Crashed', largeText)
    TextRect.center = (WIDTH/2, HEIGHT/2)
    surface.blit(TextSurf, TextRect)
    pause_score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again",150,450,100,50,green,bright_green,gameloop)
        button("Quit",550,450,100,50,red,bright_blue,quitgame)

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(surface, ac, (x,y,w,h))

        if click[0]==1 and action != None:
            action()
            
    else:
        pygame.draw.rect(surface, ic, (x,y,w,h))

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, small_text)
    textRect.center = (x + (w/2), y + (h/2))
    surface.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def paused():
    pygame.mixer.music.pause()
    
    largeText = pygame.font.SysFont('comicsansms', 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2))
    surface.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_blue,quitgame)

        pygame.display.update()
        clock.tick(15)

def unpause():
    pygame.mixer.music.unpause()
    
    global pause
    gameloop()
        
def gameIntro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                intro = False
                quit()
                
        surface.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('A BIT RACEY!', largeText)
        TextRect.center = (WIDTH/2, HEIGHT/2)
        surface.blit(TextSurf, TextRect)

        # getting the pos of the mouse
        mouse = pygame.mouse.get_pos()
        
        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(surface, bright_green,(150,450,100,50))
        else:
            pygame.draw.rect(surface, green,(150,450,100,50))
        if 550 + 100 > mouse[0] > 550 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(surface, bright_blue,(550,450,100,50))
        else:
            pygame.draw.rect(surface, blue,(550,450,100,50))

        #buttons
        button('Go!',150,450,100,50,green,bright_green,gameloop)
        button('Quit',550,450,100,50,blue,bright_blue,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def gameloop():
    #music
    global crash_sound
    global added_speed
    crash_sound = pygame.mixer.Sound('Crash.wav')
    pygame.mixer.music.load('bgsound.wav')
    pygame.mixer.music.play(-1) # play indefinitely

    global pause, pause_score
    
    x = WIDTH * 0.45 # 800 * 0.45  = 360px
    y = HEIGHT * 0.8 # 600 * 0.8 = 480px

    x_change = 0

    thing_startx = random.randrange(0, WIDTH)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    count = pause_score
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN: # that is a key is pressed.
                if event.key == pygame.K_LEFT:
                    x_change = -5-added_speed
                if event.key == pygame.K_RIGHT:
                    x_change = 5+added_speed
                if event.key == pygame.K_p:
                    pause = True
                    pause_score = count
                    paused()

            if event.type == pygame.KEYUP: # that is a key is released
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0


        x += x_change

        surface.fill(white)
        thingsDodged(count)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x,y)

        if x > (WIDTH - car_width) or x < 0:
            crash()

        if thing_starty > HEIGHT:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, WIDTH)
            # score
            count += 1
            # Increasing the difficulty of the game
            thing_width += count * 1.2
            thing_speed += 1
            added_speed += 0.5
            

        if y < thing_starty + thing_height:
            print('y crossover!')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x+car_width < thing_startx + thing_width:
                print('x crossover!')
                crash()
        

        pygame.display.update() # DON'T forget to write it!
        clock.tick(60) # 60 fps

gameIntro()
gameloop()
pygame.quit()
quit()
