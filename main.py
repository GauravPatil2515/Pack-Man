import pygame
import random
import os

# Initialize the game
pygame.init()

# Set up display
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pac-Man")

# Set up clock
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Load images
try:
    pacman_img = pygame.image.load('pacman.png')
    ghost_img = pygame.image.load('ghost.png')
    food_img = pygame.image.load('food.png')
    background_img = pygame.image.load('background.png')
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Make sure pacman.png, ghost.png, food.png, and background.png are in the same directory as the script.")
    pygame.quit()
    quit()

# Resize images
pacman_img = pygame.transform.scale(pacman_img, (30, 30))
ghost_img = pygame.transform.scale(ghost_img, (30, 30))
food_img = pygame.transform.scale(food_img, (15, 15))
background_img = pygame.transform.scale(background_img, (600, 600))

# Pac-Man class
class Pacman:
    def __init__(self):
        self.x = 300
        self.y = 300
        self.speed = 5

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.x = max(0, min(self.x, 570))
        self.y = max(0, min(self.y, 570))

    def draw(self, screen):
        screen.blit(pacman_img, (self.x, self.y))

# Ghost class
class Ghost:
    def __init__(self):
        self.x = random.randint(0, 570)
        self.y = random.randint(0, 570)
        self.speed = 3

    def move(self):
        self.x += random.choice([-1, 1]) * self.speed
        self.y += random.choice([-1, 1]) * self.speed
        self.x = max(0, min(self.x, 570))
        self.y = max(0, min(self.y, 570))

    def draw(self, screen):
        screen.blit(ghost_img, (self.x, self.y))

# Food class
class Food:
    def __init__(self):
        self.x = random.randint(0, 585)
        self.y = random.randint(0, 585)

    def draw(self, screen):
        screen.blit(food_img, (self.x, self.y))

# Create game objects
pacman = Pacman()
ghosts = [Ghost() for _ in range(5)]
foods = [Food() for _ in range(10)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Pac-Man
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman.move(-pacman.speed, 0)
    if keys[pygame.K_RIGHT]:
        pacman.move(pacman.speed, 0)
    if keys[pygame.K_UP]:
        pacman.move(0, -pacman.speed)
    if keys[pygame.K_DOWN]:
        pacman.move(0, pacman.speed)

    # Move ghosts
    for ghost in ghosts:
        ghost.move()

    # Check for collisions
    for food in foods[:]:
        if pygame.Rect(pacman.x, pacman.y, 30, 30).colliderect(pygame.Rect(food.x, food.y, 15, 15)):
            foods.remove(food)

    for ghost in ghosts:
        if pygame.Rect(pacman.x, pacman.y, 30, 30).colliderect(pygame.Rect(ghost.x, ghost.y, 30, 30)):
            running = False

    # Draw everything
    screen.blit(background_img, (0, 0))
    pacman.draw(screen)
    for ghost in ghosts:
        ghost.draw(screen)
    for food in foods:
        food.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
