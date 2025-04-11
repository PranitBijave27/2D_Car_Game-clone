# importing packages
import time

import pygame
from pygame.locals import *  # importing key constants
import sys
import random

# Initialize pygame module
pygame.init()

# Constants for screen dimensions and frame rate
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 650
FPS = 60
# Creating a game screen with the specified dimensions
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

logo_png = pygame.image.load("D:\\pythongame\\FlappyBirdClone\\GameSprites\\pranitlogo.png")
pygame.display.set_caption("CAR_GAME BY PRANIT") # Setting window title
pygame.display.set_icon(logo_png) # Setting game window icon

# Loading the main car and background images
Car = pygame.image.load("D:\\pythongame\\Cargame\\Gamesprites\\car.png").convert_alpha()
highway = pygame.image.load("D:\\pythongame\\Cargame\\Gamesprites\\highway.png").convert_alpha()

# Additional images for logos and UI elements
logo = pygame.image.load("D:\\pythongame\\Cargame\\Gamesprites\\Logo1.png").convert_alpha()
logo2 = pygame.image.load("D:\\pythongame\\Cargame\\Gamesprites\\logo2.png").convert_alpha()
ready = pygame.image.load("D:\\pythongame\\FlappyBirdClone\\GameSprites\\ready.png").convert_alpha()
blastimg=pygame.image.load("D:\pythongame\Cargame\Gamesprites\\blast.png").convert_alpha()

# List of obstacle images (different types of cars)
obstacle_images = [
    pygame.image.load("D:\\pythongame\\Cargame\\Gamesprites\\redcar.png").convert_alpha(),
    pygame.image.load("D:\\pythongame\\Cargame\\Gamesprites\\pickup_truck.png").convert_alpha(),
    pygame.image.load("D:\\pythongame\\Cargame\\Gamesprites\\semi_trailer.png").convert_alpha(),
    pygame.image.load("D:\\pythongame\\Cargame\\Gamesprites\\van.png").convert_alpha()
]
# Loading number images for the score display
Game_number = {'numbers': tuple(
    pygame.image.load(f"D:\\pythongame\\FlappyBirdClone\\GameSprites\\{i}.png").convert_alpha()
    for i in range(10)
)}
# Game over and score images
gameover = pygame.image.load("D:\\pythongame\\Cargame\\Gamesprites\\gameover.png").convert_alpha()
score_name_img = pygame.image.load("D:\\pythongame\\Cargame\\Gamesprites\\score.png")

# Car starting position and movement variables
carX = 270
carY = 460
carx_change = 0
cary_change = 0
road_start = 0
speed_higway = 10
SCORE = 0

# Background music and car blast sound
background_song = pygame.mixer.Sound("D:\\pythongame\\cargame\\backgroundsong.mp3")
carblast = pygame.mixer.Sound("D:\\pythongame\\Cargame\\carblast.wav")
background_song.play(-1) # Looping background music

# Function to display the welcome screen
def welcome_Screen():
    # Positioning elements (car, logo, etc.)
    playerx = int(SCREEN_WIDTH / 2.5) + 17
    playery = int((SCREEN_HEIGHT - Car.get_height()) / 2.5)
    logox = int((SCREEN_WIDTH - logo.get_width()) / 2 + 5)
    logoy = int(SCREEN_HEIGHT * 0.08)
    logo2xx = logox + 88
    logo2yy = logoy + 35

    # Main game loop for the welcome screen
    while True:
        for i in pygame.event.get():
            if i.type == QUIT or (i.type == KEYDOWN and i.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif i.type == KEYDOWN and (i.key == K_SPACE or i.key == K_UP):
                return # Exit the welcome screen when space or up arrow is pressed

        # Drawing elements on the screens
        SCREEN.blit(highway, (75, 0))
        SCREEN.blit(obstacle_images[0], (200, 350))
        SCREEN.blit(Car, (playerx, playery))
        SCREEN.blit(obstacle_images[1], (340, 420))
        SCREEN.blit(obstacle_images[2], (160, 100))
        SCREEN.blit(logo, (logox, logoy))
        SCREEN.blit(logo2, (logo2xx, logo2yy))
        SCREEN.blit(ready, (logox + 45, logo2yy + 80))
        pygame.display.update() # Update the display

# Function to display the player's car on the screen
def player_car(x, y):
    SCREEN.blit(Car, (x, y))

# Function to display the background (scrolling effect)
def background(y):
    SCREEN.blit(highway, (75, y))
    SCREEN.blit(highway, (75, y - highway.get_height()))

# Class to represent obstacles on the road
class Obstacle:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.width = self.image.get_width()
        self.speed = 5 # Speed at which the obstacle moves
        self.passed = False # Whether the obstacle has been passed by the car


    # Function to move the obstacle down the screen
    def move(self):
        self.y += self.speed
        global SCORE

        # Check if the car has passed the obstacle
        closest_obstacle = min(
            (ob for ob in car_obstacles if abs(ob.x - carX) < 60 and ob.y > carY),
            key=lambda ob: ob.y,
            default=None
        )
        if closest_obstacle and not closest_obstacle.passed:
            closest_obstacle.passed = True
            SCORE += 1  # Increment score when the car passes an obstacle
        if self.y > SCREEN_HEIGHT:
            self.y = -random.randint(100, 500)   # Reset obstacle to top of the screen
            self.x = random.choice(lanes)
            self.passed = False

            while True:
                new_lane = random.choice(lanes)
                safe = True
                for ob in car_obstacles:
                    if ob != self and ob.x == new_lane and abs(ob.y - self.y) < 150:
                        safe = False
                        break
                if safe:
                    self.x = new_lane
                    break



    # Function to draw the obstacle on the screen
    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))

# Create obstacles and shuffle their positions
num_obstacles = 4
lanes = [155, 210, 290, 360]
random.shuffle(lanes)
car_obstacles = [Obstacle(lanes[i], random.randint(-500, -100), obstacle_images[i]) for i in range(num_obstacles)]

# Function to display the score
def show_score():
    SCREEN.blit(score_name_img, (200, 30)) # Display score label
    mydigits = [int(x) for x in list(str(SCORE))]  # Split score into individual digits
    width = 0
    # Calculate the total width of the digits to center the score on the screen
    for digit in mydigits:
        width += Game_number['numbers'][digit].get_width()

    # Center the score horizontally
    Xoffset = (SCREEN_WIDTH - width) / 2
    for digit in mydigits:
        SCREEN.blit(Game_number["numbers"][digit], (Xoffset, SCREEN_HEIGHT * 0.12)) # Draw each digit
        Xoffset += Game_number["numbers"][digit].get_width()

# Function to check for collisions between the car and obstacles
def collision(carX, carY, car_image, obstacle):
    car_width = car_image.get_width()
    car_height = car_image.get_height()
    ob_width = obstacle.image.get_width()
    ob_height = obstacle.image.get_height()

    #  Check if the car overlaps with the obstacle
    if (carX < obstacle.x + ob_width - 25 and
            carX + car_width - 25 > obstacle.x and
            carY < obstacle.y + ob_height - 17 and
            carY + car_height - 17 > obstacle.y):
        carblast.play() # Play car crash sound
        # redrawing and updating the background, obstacle and blast image
        background(road_start)
        for obs in car_obstacles:
            obs.draw()
        SCREEN.blit(blastimg,(carX+10,carY))  # Draw blast effect
        pygame.display.update()

        time.sleep(1)
        print(f"final score is {SCORE}")
        gameover_screen()  # Show game over screen
        return True
    return False

# Function to display the game over screen and reset the game
def gameover_screen():
    global SCORE, carX, carY, carx_change, cary_change, car_obstacles
    SCREEN.blit(highway, (75, 0))  # Draw background
    SCREEN.blit(gameover, (160, 55))  # Display game over image
    SCREEN.blit(score_name_img, (200, 150)) # Display score label

    # Display the final score
    mydigits = [int(x) for x in list(str(SCORE))]
    width = sum(Game_number['numbers'][digit].get_width() for digit in mydigits)
    Xoffset = (SCREEN_WIDTH - width) / 2
    for digit in mydigits:
        SCREEN.blit(Game_number["numbers"][digit], (Xoffset, SCREEN_HEIGHT * 0.4))
        Xoffset += Game_number["numbers"][digit].get_width()
    pygame.display.update()

    # Wait for user input to restart or quit
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                # Restart the game
                SCORE = 0
                carX = 270
                carY = 460
                carx_change = 0
                cary_change = 0
                random.shuffle(lanes)
                car_obstacles = [Obstacle(lanes[i], random.randint(-500, -100), obstacle_images[i]) for i in range(num_obstacles)]
                return

# Main game loop
if __name__ == "__main__":
    while True:
        SCREEN.fill((8, 107, 21))  # Fill screen with background color
        welcome_Screen()# Display welcome screen
        fpsclock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        carx_change -= 4.5
                    elif event.key == K_RIGHT:
                        carx_change += 4.5
                    if event.key == K_UP:
                        cary_change -= 5
                    elif event.key == K_DOWN:
                        cary_change += 5
                if event.type == KEYUP and (event.key in [K_LEFT, K_RIGHT, K_UP, K_DOWN]):
                    carx_change = 0
                    cary_change = 0

            road_start += speed_higway
            if road_start >= highway.get_height():
                road_start = 0
            background(road_start)

            carX += carx_change
            carY += cary_change

            # Move and draw obstacles
            for obstacle in car_obstacles:
                obstacle.move()
                obstacle.draw()

            # Boundaries for the car
            if carX >= 350:
                carX = 350
            elif carX <= 130:
                carX = 130
            if carY <= 0:
                carY = 0
            elif carY >= 480:
                carY = 480

            # Draw player car and score
            player_car(carX, carY)
            show_score()

            # Check for collisions with obstacles
            for obstacle in car_obstacles:
                if collision(carX, carY, Car, obstacle):
                    running = False
                    break

            pygame.display.update()   # Update the display
            fpsclock.tick(FPS)   # Maintain the frame rate
