import pygame
import random
#import time

WIDTH = 400
HEIGHT = 800
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (200,0,0)
GREEN = (0,200,0)
BLUE = (0, 0, 200)
CYAN = (163, 255, 224)
YELLOW = (255, 248, 48)

bright_red = (255,0,0)
bright_green = (0,255,0)

# initialize pygame
pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Game")
win_sound = pygame.mixer.Sound("/Users/Hank/Desktop/Python_Week/Z_FinalFile/winwin2.wav")
smash_sound = pygame.mixer.Sound("/Users/Hank/Desktop/Python_Week/Z_FinalFile/smash.wav")

#win_sound = pygame.mixer.Sound("C:\winwin2.wav")
#smash_sound = pygame.mixer.Sound("C:\smash.wav")
clock = pygame.time.Clock()
#t0 = time.time()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.fill(WHITE)
        largeText = pygame.font.SysFont("Impact", 45)
        TextSurf, TextRect = text_objects("Dodoge Game", largeText)
        
        TextRect.center = ((WIDTH/2), (HEIGHT/2 - 150))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Start!", 150, 350,100, 50, GREEN, bright_green,game_loop)
        button("Quit!", 150,550,100,50, RED, bright_red,quitgame)
        #button("Help", 150,450,100,50, GREEN, bright_green,game_help)
		
        pygame.display.update()
        clock.tick(15)
        
def quitgame():
    pygame.quit()
    quit()

    
def button(msg,x,y,w,h,c1,c2,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, c2,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, c1,(x,y,w,h))

    smallText = pygame.font.SysFont("Impact",20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(TextSurf, TextRect)


    
def convertMill(millis):
    millSeconds=(millis)%60
    millSeconds = int(millSeconds)
    seconds=(millis)%60
    seconds = int(seconds)
    minutes=(millis/(1000*60))%60
    minutes = int(minutes)

    return ("%d:%d:%d" % (minutes, seconds, millSeconds))

def text_objects(text, font):
    TextSurface = font.render(text, True, BLACK)
    return TextSurface, TextSurface.get_rect()

def got_hit():

    pygame.mixer.Sound.play(smash_sound)
    pygame.mixer.music.stop()
    
    hitted = True
    #print(time)
    
    while hitted:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        #gameDisplay.fill(WHITE)
        largeText = pygame.font.SysFont("Impact", 45)
        
        TextSurf, TextRect = text_objects("Game Over", largeText)

        TextRect.center = ((WIDTH/2), (HEIGHT/2 - 150))
        
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Again", 150,350,100,50, GREEN, bright_green,game_loop)
        button("Quit!", 150,450,100,50, RED, bright_red,quitgame)
        button("Help", 150,550,100,50, GREEN, bright_green,game_help)
        
        
		
        pygame.display.update()
        clock.tick(15)

def game_won():
#    global time
#    t1 = time.time()
#    dt = t1-t0
#    print (t1)
#    print (t0)
#    print (dt)
#   time = pygame.time.get_ticks()
    pygame.mixer.Sound.play(win_sound)
    pygame.mixer.music.stop()
    
    reached = True
    while reached:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        #gameDisplay.fill(WHITE)
        largeText = pygame.font.SysFont("Impact", 45)
        
        
        
        TextSurf, TextRect = text_objects("YOU WON!", largeText)
        #TextSurf2, TextRect2 = text_objects("Time Cost: "+convertMill(time), largeText)
        
        TextRect.center = ((WIDTH/2), (HEIGHT/2 - 150))
        #TextRect2.center = ((WIDTH/2), (HEIGHT/2 - 100))
        
        gameDisplay.blit(TextSurf, TextRect)
        #gameDisplay.blit(TextSurf2, TextRect2)
        
        button("Again", 150,350,100,50, GREEN, bright_green,game_loop)
        button("Quit!", 150,450,100,50, RED, bright_red,quitgame)
		
        pygame.display.update()
        clock.tick(15)        

def game_help():
    
    helpping = True
    while helpping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.fill(WHITE)
        smallText = pygame.font.SysFont("Impact", 20)
        TextSurf, TextRect = text_objects("Reach all the way to the top to", smallText)
        TextSurf2, TextRect2 = text_objects("win the game without hitting by objects", smallText)
        TextRect.center = ((WIDTH/2), (HEIGHT/2 - 200))
        TextRect2.center = ((WIDTH/2), (HEIGHT/2 - 150))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        
        button("Start!", 150,350,100,50, GREEN, bright_green,game_loop)
        button("Quit!", 150,450,100,50, RED, bright_red,quitgame)
		
        pygame.display.update()
        clock.tick(15)        
        

def game_loop():
    #pygame.init()
    class Player(pygame.sprite.Sprite):
        #sprite for the player
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50,50))
            self.image.fill(CYAN)
            self.rect = self.image.get_rect()
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0
            self.speedy = 0
            
        def update(self):
            self.speedx = 0
            self.speedy = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -5
            if keystate[pygame.K_RIGHT]:
                self.speedx = 5
            if keystate[pygame.K_UP]:
                self.speedy = -5
            if keystate[pygame.K_DOWN]:
                self.speedy = 5
                
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
                
            if self.rect.top > HEIGHT - 70:
                self.rect.top = HEIGHT - 70
            if self.rect.top < 0:
                game_won()
                
    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((30,40))
            self.image.fill(YELLOW)
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)
            self.speedx = random.randrange(-3,3)
            
        def update(self):
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            if self.rect.top > HEIGHT + 10:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100,-40)
                self.speedy = random.randrange(2,10)

    
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
    for i in range(18):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
            
    running = True  
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quitgame()
    
        all_sprites.update()
        
        hits = pygame.sprite.spritecollide(player,mobs,False)
        
        if hits:
            #print(int(str(time)[:1]))
            #print("seconds")
            #pygame.time.Clock.get_time()
            got_hit()
            running = False
        
        
        
        #print(time)
        gameDisplay.fill(WHITE)
        all_sprites.draw(gameDisplay)
        pygame.display.flip()
        #pygame.display.update()
        #clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()