import pygame
import random

pygame.init()

screenWidth = 1000
screenHeight = 500
white = (255, 255, 255)

size = screenWidth, screenHeight
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

bg = pygame.image.load('bgg.png')
frogImg = pygame.image.load('frog1.png')

frogWidth = frogImg.get_width()
frogHeight = frogImg.get_height()
w, h = 50, 50

def homeScreen():
    font = pygame.font.SysFont(None, 100)
    text = font.render("Welcome to the jungle", True, white)

    font_2 = pygame.font.SysFont(None, 60)
    text_2 = font_2.render("Press Space key to start..", True, white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.blit(bg, (0, 0))
        screen.blit(text, (100, 100))
        screen.blit(text_2, (30, 200))
        pygame.display.update()

def gameOver(counter):
    font = pygame.font.SysFont(None, 100)
    text = font.render("Game Over", True, white)

    font_2 = pygame.font.SysFont(None, 60)
    text_2 = font_2.render(f"Your score: {counter}", True, white)

    font_3 = pygame.font.SysFont(None, 40)
    text_3 = font_3.render("Press R to restart", True, white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    homeScreen()

        screen.blit(bg, (0, 0))
        screen.blit(text, (100, 100))
        screen.blit(text_2, (30, 200))
        screen.blit(text_3, (30, 300))
        pygame.display.update()

def drawSnake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen, white, [snakeList[i][0], snakeList[i][1], w, h])

def score(counter):
    font_3 = pygame.font.SysFont(None, 30)
    text_3 = font_3.render(f"Score: {counter}", True, white)
    screen.blit(text_3, (60, 20))

def game():
    frogX = random.randint(1, screenWidth - frogWidth)
    frogY = random.randint(1, screenHeight - frogHeight)
    move_x = 0
    move_y = 0
    speed = 2
    x, y = 0, 0
    counter = 0
    snakeList = []
    snakeLength = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = speed
                    move_y = 0
                elif event.key == pygame.K_LEFT:
                    move_x = -speed
                    move_y = 0
                elif event.key == pygame.K_DOWN:
                    move_y = speed
                    move_x = 0
                elif event.key == pygame.K_UP:
                    move_y = -speed
                    move_x = 0

        x += move_x
        y += move_y

        screen.blit(bg, (0, 0))
        screen.blit(frogImg, (frogX, frogY))
        score(counter)

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        drawSnake(snakeList)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        snake = pygame.draw.rect(screen, white, [x, y, w, h])
        frog = pygame.Rect(frogX, frogY, frogWidth, frogHeight)

        if frog.colliderect(snake):
            frogX = random.randint(1, screenWidth - frogWidth)
            frogY = random.randint(1, screenHeight - frogHeight)
            snakeLength += 50
            counter += 1
        for each in snakeList[0:-1]:
            if each==snakeList[-1]:
                gameOver(counter)    

        pygame.display.flip()

homeScreen()
