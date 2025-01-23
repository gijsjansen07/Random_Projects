import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    pygame.draw.rect(window,(100,100,100),(10,10,40,20))
    pygame.display.update()    

pygame.quit()

