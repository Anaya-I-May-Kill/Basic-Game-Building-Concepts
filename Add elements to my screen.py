import pygame

# Initialize Pygame
pygame.init()

# Variables
SCREEN_WIDTH, SCREEN_HEIGHT = 640 , 480
RECT_WIDTH, RECT_HEIGHT = 100 , 50
BACKGROUND_COLOR = (255 , 255 , 255)  # White
RECT_COLOR = (0 , 128 , 255)  # Blue
TEXT_COLOR = (0 , 0 , 0)  # Black
FONT_SIZE = 36

# Create Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first game screen")

# Create a font object
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

# Define the rectangle position
rect_x = (SCREEN_WIDTH - RECT_WIDTH) // 2
rect_y = (SCREEN_HEIGHT - RECT_HEIGHT) // 2

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the background
    screen.fill(BACKGROUND_COLOR)

    # Draw the rectangle
    pygame.draw.rect(screen, RECT_COLOR, [rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT])

    # Render the text
    text = font.render("RANDOM SCREEENNNNN", True, TEXT_COLOR)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(text, text_rect)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()