import pygame

pygame.init()

screen = pygame.display.set_mode( (900,700) )
finished = False

playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (35,40))
playerImage = playerImage.convert()
playerImage = playerImage.convert_alpha()

backgroundImage = pygame.image.load("background2.jpg")
backgroundImage = pygame.transform.scale(backgroundImage, (900,700))
backgroundImage = backgroundImage.convert()

frame = pygame.time.Clock()

playerX = 450 - 35/2
playerY = 650
backgroundX = 0
backgroundY = 0

while finished == False:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  finished = True
            pressedKeys = pygame.key.get_pressed()
            pressKeys = pygame.key.get_pressed()
            

            if pressedKeys[pygame.K_UP] == 1:
                  playerY -= 5

            if pressedKeys[pygame.K_DOWN] == 1:
                  playerY += 5

            if pressKeys[pygame.K_LEFT] == 1:
                  playerX -= 5

            if pressKeys[pygame.K_RIGHT] == 1:
                  playerX += 5


      
      
      screen.blit(backgroundImage,(backgroundX,backgroundY))
      screen.blit(playerImage,(playerX, playerY))
      frame.tick(100)
      pygame.display.flip()
      
pygame.quit()
