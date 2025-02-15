import pygame
pygame.init()

x = 0
y = 0

x1 = 0
y1 = 250

x2 = 350
y2 = 250

screen = pygame.display.set_mode( ( 400, 300 ) )

finished = False

while finished == False:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  finished = True

            pressedKeys = pygame.key.get_pressed()
            pressKeys = pygame.key.get_pressed()
            

            if pressedKeys[pygame.K_UP] == 1:
                  y -= 5
                  y1 -= 5
                  y2 -= 5

            if pressedKeys[pygame.K_DOWN] == 1:
                  y += 5
                  y1 += 5
                  y2 += 5

            if pressKeys[pygame.K_LEFT] == 1:
                  x -= 5
                  x1 -= 5
                  x2 -= 5

            if pressKeys[pygame.K_RIGHT] == 1:
                  x += 5
                  x1 += 5
                  x2 += 5

                  
      rectOne = pygame.Rect(x, y, 50, 50)
      rectTwo = pygame.Rect(x1, y1, 50, 50)
      rectThree = pygame.Rect(x2, y2, 50, 50)
      
      color = (0, 0, 255)
      color2 = (0, 255, 0)
      color3 = (255, 0, 0)
      
      black = (0, 0, 0)

      screen.fill(black)
      pygame.draw.rect(screen, color, rectOne)
      pygame.draw.rect(screen, color2, rectTwo)
      pygame.draw.rect(screen, color3, rectThree)
      pygame.display.flip()
      
pygame.quit()
