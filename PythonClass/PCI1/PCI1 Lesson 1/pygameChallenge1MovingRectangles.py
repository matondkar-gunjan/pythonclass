import pygame
pygame.init()

x = 0
y = 0

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

            if pressedKeys[pygame.K_DOWN] == 1:
                  y += 5

            if pressKeys[pygame.K_LEFT] == 1:
                  x -= 5

            if pressKeys[pygame.K_RIGHT] == 1:
                  x += 5

                  
      rectOne = pygame.Rect(x, y, 50, 50)

      color = (0, 0, 225)
      black = (0, 0, 0)

      screen.fill(black)
      pygame.draw.rect(screen, color, rectOne)
      pygame.display.flip()
      
pygame.quit()
