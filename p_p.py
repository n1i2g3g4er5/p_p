from pygame import *
from random import randint
from time import time as timer

clock = time.Clock()
FPS = 60
win_width = 700
win_height = 500
display.set_caption("ping_pong")
window = display.set_mode((win_width, win_height))







class GameSprite(sprite.Sprite):
   
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def uptade(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x< win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed    
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y  += self.speed
        def update(self):
            self.rect.y += self.speed
            global lost
#исчезает, если дойдёт до края экрана
            if self.rect.y > win_height:
                self.rect.x = randint(80, win_width - 80)
                self.rect.y = 0
                lost = lost + 1
finish = False
img_back =  "images.jfif"
background = transform.scale(image.load(img_back), (win_width, win_height))   
racket1 = Player("raketka1.png",30,200,4,50,150)
racket2 = Player("raketka2.png",30,200,4,50,150)
ball = GameSprite("sharik.png",200,200,4,50,50)
game = True
while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
    if finish != True:
        racket1.update_1()       
  
   window.blit(background,(0, 0))
 
   
  
 
   
   
 
   display.update()
   clock.tick(FPS)               