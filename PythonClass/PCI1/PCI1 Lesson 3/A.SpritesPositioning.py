import pygame

pygame.init()

screen = pygame.display.set_mode( (900,700) )
finished = False

playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (35,40))
playerImage = playerImage.convert()
playerImage = playerImage.convert_alpha()
playerX = 450 - 35/2
playerY = 600


treasureImage = pygame.image.load("treasure.png")
treasureImage = pygame.transform.scale(treasureImage, (40,35))
treasureImage = treasureImage.convert()
treasureImage = treasureImage.convert_alpha()
treasureX = 430
treasureY = 50

font = pygame.font.SysFont('comicsans', 60)
textWin = font.render("Great Job!", True, (0,0,0)) 


backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (900,700))
backgroundImage = backgroundImage.convert()

frame = pygame.time.Clock()

while finished == False:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  finished = True

      pressedKeys = pygame.key.get_pressed()
      if pressedKeys[pygame.K_UP] == 1:
            playerY -= 5
      if pressedKeys[pygame.K_DOWN] == 1:
            playerY += 5
      if pressedKeys[pygame.K_LEFT] == 1:
            playerX -= 5
      if pressedKeys[pygame.K_RIGHT] == 1:
            playerX += 5


      if playerY >= treasureY and playerY <= treasureY + 35:

            if playerX >= treasureX and playerX <= treasureX + 40:
                  screen.blit(textWin, (450-textWin.get_width()/2, 350-textWin.get_height()/2))
                  playerX = 432.5
                  playerY = 650

            elif playerX + 35 >= treasureX and playerX <= treasureX + 40:
                  screen.blit(textWin, (450-textWin.get_width()/2, 350-textWin.get_height()/2))
                  playerX = 432.5
                  playerY = 650
                  
      elif playerY + 40 >=  treasureY and playerY + 40 <= treasureY + 35:

            if playerX >= treasureX and playerX <= treasureX + 40:
                  screen.blit(textWin, (450-textWin.get_width()/2, 350-textWin.get_height()/2))
                  playerX = 432.5
                  playerY = 650

            elif playerX + 35 >= treasureX and playerX + 35 <= treasureX + 40:
                  screen.blit(textWin, (450-textWin.get_width()/2, 350-textWin.get_height()/2))
                  playerX = 432.5
                  playerY = 650


      
      
      screen.blit(backgroundImage,(0,0))
      screen.blit(playerImage,(playerX, playerY))
      screen.blit(treasureImage, (treasureX, treasureY))
      screen.blit(textWin, (432.5,350))

      frame.tick(100)
      pygame.display.flip()
      
pygame.quit()
