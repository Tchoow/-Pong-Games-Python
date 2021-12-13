# Pong by @Tchoow

# Imports
import pygame
import time

pygame.init()

# create windows and set size
window = pygame.display.set_mode((800, 600))
white = [255, 255, 255]
#window.fill(white)
pygame.display.set_caption("🏓 Pong Game")

# loop
running = True

class Joueur:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.score = 0
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 5
        self.x_dir = 1
        self.y_dir = 1

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


joueur1 = Joueur(10, 300, 10, 100, (255,255,255))
joueur2 = Joueur(780, 300, 10, 100, (255,255,255))

joueur1.draw(window)
joueur2.draw(window)

ball = Ball(400, 300, 10, (255, 255, 255))
ball.draw(window)

while running:

    joueur1.draw(window)
    joueur2.draw(window)
    ball.draw(window)

    # actualisation
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                joueur1.y -= joueur1.vel
                joueur1.draw(window)
                pygame.display.update()
                time.sleep(0.01)
                joueur1.y -= joueur1.vel
                joueur1.height -= joueur1.vel
                print("up")
                break
            if event.key == pygame.K_DOWN:
                joueur1.y += joueur1.vel
                joueur1.draw(window)
                pygame.display.update()
                time.sleep(0.01)
                joueur1.y += joueur1.vel
                joueur1.height += joueur1.vel
                print("down")
                break
        

pygame.quit()