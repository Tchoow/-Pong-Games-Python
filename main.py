"""
          _____                   _______                   _____                    _____          
         /\    \                 /::\    \                 /\    \                  /\    \         
        /::\    \               /::::\    \               /::\____\                /::\    \        
       /::::\    \             /::::::\    \             /::::|   |               /::::\    \       
      /::::::\    \           /::::::::\    \           /:::::|   |              /::::::\    \      
     /:::/\:::\    \         /:::/~~\:::\    \         /::::::|   |             /:::/\:::\    \     
    /:::/__\:::\    \       /:::/    \:::\    \       /:::/|::|   |            /:::/  \:::\    \    
   /::::\   \:::\    \     /:::/    / \:::\    \     /:::/ |::|   |           /:::/    \:::\    \   
  /::::::\   \:::\    \   /:::/____/   \:::\____\   /:::/  |::|   | _____    /:::/    / \:::\    \  
 /:::/\:::\   \:::\____\ |:::|    |     |:::|    | /:::/   |::|   |/\    \  /:::/    /   \:::\ ___\ 
/:::/  \:::\   \:::|    ||:::|____|     |:::|    |/:: /    |::|   /::\____\/:::/____/  ___\:::|    |
\::/    \:::\  /:::|____| \:::\    \   /:::/    / \::/    /|::|  /:::/    /\:::\    \ /\  /:::|____|
 \/_____/\:::\/:::/    /   \:::\    \ /:::/    /   \/____/ |::| /:::/    /  \:::\    /::\ \::/    / 
          \::::::/    /     \:::\    /:::/    /            |::|/:::/    /    \:::\   \:::\ \/____/  
           \::::/    /       \:::\__/:::/    /             |::::::/    /      \:::\   \:::\____\    
            \::/____/         \::::::::/    /              |:::::/    /        \:::\  /:::/    /    
             ~~                \::::::/    /               |::::/    /          \:::\/:::/    /     
                                \::::/    /                /:::/    /            \::::::/    /      
                                 \::/____/                /:::/    /              \::::/    /       
                                  ~~                      \::/    /                \::/____/        
                                                           \/____/                                  
                                                                                                    
                                                                                                    
"""
# Pong by @Tchoow

# Imports
import pygame
import time
import sys

pygame.init()

# create windows and set size
window = pygame.display.set_mode((800, 600))


background = [0, 0, 0]
#window.fill(white)
pygame.display.set_caption("🏓 Pong Game")


print(sys.argv[0])
# loop
running    = True
gameState  = False
lastWinner = 0

class Joueur:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 1
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
        self.vel = 1
        self.x_dir = 1
        self.y_dir = 1

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


joueur1 = Joueur(10, 300, 10, 100,  (255,255,255))
joueur2 = Joueur(780, 300, 10, 100, (255,255,255))
ball    = Ball  (400, 300, 10,    (255, 255, 255))


while running:
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_z] and joueur1.y   > 0:
        joueur1.y -= joueur1.vel
    if keys[pygame.K_s] and joueur1.y < 500:
        joueur1.y += joueur1.vel
    if keys[pygame.K_UP] and joueur2.y    > 0:
        joueur2.y -= joueur2.vel
    if keys[pygame.K_DOWN] and joueur2.y    < 500:
        joueur2.y += joueur2.vel
    if keys[pygame.K_g] and gameState == False:
        gameState = True

    if gameState == True:

        if ball.y <= 0 or ball.y >= 600:
            ball.y_dir *= -1

        # point joueur 2
        if ball.x <= 0:
            ball.x = 400
            ball.y = 300
            joueur2.score += 1
            gameState = False
            lastWinner = 2

        # point joueur 1    
        if ball.x >= 800:
            ball.x = 400
            ball.y = 300
            joueur1.score += 1
            gameState = False
            lastWinner = 1

        if (lastWinner == 1):
            ball.x += 0.2
            ball.y -= 0.25
        else:
            ball.x -= 0.2
            ball.y -= 0.25


        if ball.x <= joueur1.x + joueur1.width and ball.y >= joueur1.y and ball.y <= joueur1.y + joueur1.height:
            ball.x_dir *= -1
        if ball.x >= joueur2.x and ball.y >= joueur2.y and ball.y <= joueur2.y + joueur2.height:
            ball.x_dir *= -1

        ball.x += ball.x_dir * ball.vel
        ball.y += ball.y_dir * ball.vel
        #ball.x += ball.x_dir * ball.vel


    # draw
    window.fill(background)
    joueur1.draw(window)
    joueur2.draw(window)
    ball.draw(window)

    # draw middle line
    pygame.draw.line(window, (255, 255, 255), (400, 0), (400, 600), 1)

    # draw score
    font = pygame.font.SysFont("comicsans", 40)
    text = font.render(str(joueur1.score) + " - " + str(joueur2.score), 1, (255, 255, 255))
    window.blit(text, (355, 10))

    
    pygame.display.flip()
    time.sleep(0.001)
            
    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

pygame.quit()
