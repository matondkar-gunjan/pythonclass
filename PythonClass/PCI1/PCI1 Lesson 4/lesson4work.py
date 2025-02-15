#Importing necessary libraries
import pygame
import time

collisionTreasure = False
def checkCollision(playerX, playerY, treasureX, treasureY ):
  global textWin, screen
  collisionState = False


      if playerY >= treasureY and playerY <= treasureY + 35:

            if playerX >= treasureX and playerX <= treasureX + 40:
                  
                  playerX = 432.5
                  playerY = 650
                  collisionState = True

            elif playerX + 35 >= treasureX and playerX <= treasureX + 40:
                  screen.blit(textWin, (450-textWin.get_width()/2, 350-textWin.get_height()/2))
                  playerX = 432.5
                  playerY = 650
                  collisionState = True
                  
      elif playerY + 40 >=  treasureY and playerY + 40 <= treasureY + 35:

            if playerX >= treasureX and playerX <= treasureX + 40:
                  screen.blit(textWin, (450-textWin.get_width()/2, 350-textWin.get_height()/2))
                  playerX = 432.5
                  playerY = 650
                  collisionState = True

            elif playerX + 35 >= treasureX and playerX + 35 <= treasureX + 40:
                  screen.blit(textWin, (450-textWin.get_width()/2, 350-textWin.get_height()/2))
                  playerX = 432.5
                  playerY = 650
                  collisionState = True

return collisionState, playerX, playerY

#Setup
pygame.init()

#Initialize a window or screen for display
screen = pygame.display.set_mode( (900,700) )
finished = False

#Create an object to help track time
frame = pygame.time.Clock()

#Load new image from a file
playerImage = pygame.image.load("player.png")
playerImage = pygame.transform.scale(playerImage, (35,40))
playerImage = playerImage.convert()
playerImage = playerImage.convert_alpha()


#Position the treasure at the top
treasureImage = pygame.image.load("treasure.png")
treasureImage = pygame.transform.scale(treasureImage, (40,35))
treasureImage = treasureImage.convert()
treasureImage = treasureImage.convert_alpha()
treasureX = 430
treasureY = 50

#Add in Enemy Sprite
enemyImage = pygame.image.load("enemy.png")
enemyImage = pygame.transform.scale(enemyImage, (40, 35))
enemyImage = enemyImage.covert()
enemyImage = enemyImage.convert_alpha()
enemyX = 450
enemyY = 350

#Creating Font object
font = pygame.font.SysFont('comicsans', 60)
textWin = font.render("Great Job!", True, (0,0,0)) 

#Adding in the background
backgroundImage = pygame.image.load("background.png")
backgroundImage = pygame.transform.scale(backgroundImage, (900,700))
backgroundImage = backgroundImage.convert()

#Set player sprite coordinates
playerX = 450 - 35/2
playerY = 600

#Adding Levels - setup
level = 1

collisionTreasure, playerX, playerY = checkCollision(playerX, playerY, treasureX, treasureY)

#While loop to let your game run unless user decided to quit
while finished == False:
  #Detect if the user is closing the game
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  finished = True

  
      #Moving Player Sprites
      pressedKeys = pygame.key.get_pressed()
      if pressedKeys[pygame.K_UP] == 1:
            playerY -= 5
      if pressedKeys[pygame.K_DOWN] == 1:
            playerY += 5
      if pressedKeys[pygame.K_LEFT] == 1:
            playerX -= 5
      if pressedKeys[pygame.K_RIGHT] == 1:
            playerX += 5

            #Moving enemy left and right
            if enemyX >= 850 - 40:
              movingRight = False
            elif enemyX <= 50:
              movingRight = True
            if movingRight == True:
              enemyX += 5
            else:
              enemyX -= 5

  
      collisionTreasure, playerX, playerY = checkCollision(playerX, playerY, treasureX, treasureY)

      if collisionTreasure == True:
        level += 1
        textWIn = font.render("You have reached level " + str(level) + "!", True, (0,0,0))
        screen.blit(textWin, (450-textWin.get_width()/2,350-textWin.get_height()/2))
        pygame.display.flip()
        frame.tick(1)
       

  screen.blit(backgroundImage,(0,0))
  screen.blit(playerImage,(playerX, playerY))
  screen.blit(treasureImage, (treasureX, treasureY))
  screen.blit(enemyImage, (enemyX, enemyY)) 
     
      
    pygame.display.flip()
    frame.tick(30)
                    
pygame.quit()
