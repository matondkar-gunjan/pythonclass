#Pygame - template - skeleton for a new pygame project
import pygame
import random

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

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((50, 50))
    self.image.fill(GREEN)
    self.rect = self.image.get_rect()
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

class Mob(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((30, 40))
    self.image.fill(RED)
    self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH / 2
    self.rect.bottom = HEIGHT - 10
    self.speedx = 0
    #Lesson 6 Challenge 2: Step 8
    #Lesson 6 Challenge 2: Step 9

  

    

    self.rect.x += self.speedx

    if self.rect.right > WIDTH:
      self.rect.right = WIDTH
    if self.rect.left < 0:
      self.rect.right = 0

player = Player()
all_sprites.add(player)
all_sprites.update()

#A sprite group is just a collection of sprites that you can act on all at the same time
all_sprites = pygame.sprite.Group()

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

  #Update function : Add in the update portion
  #Update
  all_sprites.update()

  #Drawing/Rendering
  screen.fill(BLACK)

  #Blit the sprites images
  all_spirtes.draw(screen)
  pygame.display.flip()

#Close the game
pygame.quit()

