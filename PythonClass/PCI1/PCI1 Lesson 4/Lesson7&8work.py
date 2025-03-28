
#Pygame - template - skeleton for a new pygame project
import pygame
import random
from os import path
#img_dir = path.join(path.dirname(__file__), 'image_folder')




#Constant for Screen Width, Height and FPS
WIDTH = 480
HEIGHT = 600
FPS = 60

#Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0 )
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Initialise pygame and create window
pygame.init()

#Enable sound effects in game 
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Set the caption of the screen
pygame.display.set_caption("Space explorers")


#Set speed of the game
clock = pygame.time.Clock()

#background = pygame.image.load(path.join(img_dir, 'background.png')).convert_alpha( ) 
background_rect = background.get_rect( )

player_img = pygame.image.load(path.join(img_dir,"playerShip1_red.png")).convert_alpha( )
meteor_img = pygame.image.load(path.join(img_dir,"meteorGrey_med1.png")).convert_alpha( )
bullet_img = pygame.image.load(path.join(img_dir,"laserBlue01.png")).convert_alpha( )

# Lesson 9-10 : Step B1
# Lesson 9-10 : Step B2
# Lesson 9-10 : Step B3

#Create our player class
class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    
    self.image = pygame.transform.scale(player_img, (50, 38)
    self.image.get_rect()
    # Lesson 9-10 : Step A1 


    # Lesson 9-10 : Step A2
 
    self.rect.centerx = WIDTH / 2
    self.rect.bottom = HEIGHT - 10
    self.speedx = 0
    
  
  def update(self):
    self.speedx = 0
    
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
      self.speeds =  -5
    if keystate[pygame.K_RIGHT]:
      self.speeds = 5

    self.rect.x += self.speedx
      
    if self.rect.right > WIDTH:
      self.rect.right = WIDTH
    if self.rect.left < 0:
      self.rect.right = 0

  def shoot(self):
    bullet = Bullet(self.rect.centerx, self.rect.top)
    all_sprites.add(bullet)
    bullets.add(bullet)
    
bullets = pygame.sprite.Group()

#Create our mob class
class Mob(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(bullet_img, (40,40))
    #Lesson 9-10 : C7
    #Lesson 9-10 : C8 (Remove B4)
    #Lesson 9-10 : B4
    #Lesson 9-10 : C8

    self.rect= self.image.get_rect()
    self.rectx = random.randrange(WIDTH - self.rect.width)    
    self.recty = random.randrange(-100, -40)
    self.speedy = random.randrange(1,8)
    self.speedx = random.randrange(-3, 3)

    # Lesson 9-10 : Step A3


      # Lesson 9-10 : Step A4


      # Lesson 9-10 : Step C9


      # Lesson 9-10 : Step C1


      # Lesson 9-10 : Step C2



   # Lesson 9-10 : Step C3



      # Lesson 9-10 : Step C4

         # Lesson 9-10 : Remove this code in Step C11

         # Lesson 9-10 : Step C5

         
         # Lesson 9-10 : Step C10

         # Lesson 9-10 : Step C12 overtakes C10, remove C10


         # Make meteor rotate around the same center
         # Lesson 9-10 : Step C14


         # Lesson 9-10 : Step C11


         # Lesson 9-10 : Step C13


         # Lesson 9-10 : Step C15

  def update(self):

    self.rect.y += self.speedy
    self.rect.x += self.speedy
    # Lesson 9-10 : Step C6

    if self.rect.top > HEIGHT + 10:
      self.rect.x = random.randrange(WIDTH = self.rect.width)
      self.rect.y = random.range(-100, -40)
      self.speedy = random.range(1, 8)

Class bullet(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(bullet_img, (10,20))
    
    self.rect = self.image.get_rect()
    self.rect.bottom = y
    self.rect.center = x
    self.speedy = -10

def update(self):
  self.rect.y += self.speedy
  
  if self.rect.bottom < 0:
    self.kill


#A sprite group is just a collection of sprites
that you can act on all at the same time
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

all_sprites.update()

for i in range(8):
  m = Mob()
  all_sprites.add(m)
  mobs.add(m)


#Game loop
running = True
while running:
  
  #Keep loop running at the same speed
  clock.tick(FPS)

  #Process input (events)
  for event in pygame.event.get():

    #Check for closing window
    if event.type == pygame.QUIT:
      running = False

    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        player.shoot()

  hits = pygame.sprite.groupcollide(mobs, bullets, True, True)

  for hit in hits:
     m = Mob()
     all_sprites.add(m)
     mobs.add(m)
  

  

  #Update function : Add in the update portion
  #Update
  all_sprites.update()

  hits = pygame.sprite.spritecollide(player, mobs, False)
  if hits:
    running = False

  

  #Drawing/Rendering
  screen.fill(BLACK)

  #Blit the sprites images
  all_spirtes.draw(screen)
  pygame.display.flip()

#Close the game
pygame.quit()
