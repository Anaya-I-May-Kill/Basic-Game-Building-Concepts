import pygame

pygame.init()
window = pygame.display.set_mode((400 , 400))

window.fill((5 , 38 , 206))

PINKY = (255 , 189 , 189)

pygame.draw.circle(window , PINKY , (300 , 300), 50)

pygame.draw.circle(window , PINKY , (100 , 100), 50, 3)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()