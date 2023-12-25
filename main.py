import pygame
from pygame.locals import *
import random

pygame.init()
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 620

white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Pygame")

font_main = pygame.font.Font('freesansbold.ttf', 64)

text = font_main.render('FIGHTER MONSTER', True, black, None)
textRect = text.get_rect()
textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150)

font_tutorial = pygame.font.Font('freesansbold.ttf', 32)

text_tutorial1 = font_tutorial.render('How to play :', True, black, None)
text_tutorialRect1 = text_tutorial1.get_rect()
text_tutorialRect1.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2-50)
text_tutorial2 = font_tutorial.render('1. Jump over rock monsters an indestructible rock', True, black, None)
text_tutorialRect2 = text_tutorial2.get_rect()
text_tutorialRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
text_tutorial3 = font_tutorial.render('2. Click to attack the slime 3 times to death', True, black, None)
text_tutorialRect3 = text_tutorial3.get_rect()
text_tutorialRect3.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2+50)

try:
    image_heart = pygame.image.load("image/pngegg.png")
    image_heart = pygame.transform.scale(image_heart, (32, 32))

    image_bg = pygame.image.load("image/Blue.png")
    image_bg = pygame.transform.scale(image_bg, (128, 128))

    image_mouse = pygame.image.load("image/mouse.png")
    image_mouse = pygame.transform.scale(image_mouse, (64, 64))

    image_map = pygame.image.load("image/map.png")
    image_map = pygame.transform.scale(image_map, (128, 128))

    image_start = pygame.image.load("image/Play.png")
    image_start = pygame.transform.scale(image_start, (110, 110))
    image_start_rect = image_start.get_rect()
    image_start_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    image_tutorial = pygame.image.load("image/Leaderboard.png")
    image_tutorial = pygame.transform.scale(image_tutorial, (110, 110))
    image_tutorial_rect = image_tutorial.get_rect()
    image_tutorial_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150)

    image_exit = pygame.image.load("image/close.png")
    image_exit = pygame.transform.scale(image_exit, (80, 80))
    image_exit_rect = image_exit.get_rect()
    image_exit_rect.center = (SCREEN_WIDTH - 40, 40)

    image_back= pygame.image.load("image/Previous.png")
    image_back = pygame.transform.scale(image_back, (80, 80))
    image_back_rect = image_back.get_rect()
    image_back_rect.center = (SCREEN_WIDTH - 40, 40)

except FileNotFoundError:
    print("Image not found")
    pygame.quit()
    exit()


def drawBG(win):
    image_bg = pygame.image.load("image/bg.png")
    win.blit(image_bg, (0, 0))


def heart_count(win, num):
    i = 0
    x = 50
    while i < num:
        win.blit(image_heart, (x, 100))
        x += 50
        i += 1


class Character:
     def __init__(self,  x,  y,  width,  height,  color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.base = SCREEN_HEIGHT - 128
        self.health = 100
        self.jumpCount = 10
        self.getRect = None
        self.speed = 0
        self.heart = 3

     def update (self,  win, image):
        image_character = pygame.image.load(image)
        image_character = pygame.transform.scale(image_character, (self.width, self.height))
        image_character_rect = image_character.get_rect()
        image_character_rect.center = (self.x, self.y)
        if self.y <= self.base:
            self.y += 10
        if (self.y < 500) and (self.y > 490):
            self.y = 500

        win.blit(image_character, image_character_rect)
        self.getRect = image_character_rect

        pygame.display.update()

         
class Stone(Character):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

    def update(self, win, image):
        super().update(win, image)

    def move(self, win):
        self.x -= 5


class Slime(Character):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)

    def update(self, win, image):
        super().update(win, image)

    def move(self, win):
        self.x -= 2 + self.speed


loop_bg = 0
kill = 0

page = "main"

man = Character(50, 200, 90, 90, (0, 0, 255))
stone = Stone(4000, 200, 90, 90, (0, 0, 255))
slime1 = Slime(random.randint(1500, 3500), 200, 90, 75, (0, 0, 255))
slime2 = Slime(random.randint(1500, 3500), 200, 90, 75, (0, 0, 255))
slime3 = Slime(random.randint(1500, 3500), 200, 90, 75, (0, 0, 255))
slime4 = Slime(random.randint(1500, 3500), 200, 90, 75, (0, 0, 255))

imageStone = []
for i in range(11):
    imageStone.append("image/s" + str(i + 1) + ".png")

imagesMan = []
for i in range(11):
    imagesMan.append("image/m" + str(i + 1) + ".png")

imagesSlime = []
for i in range(8):
    imagesSlime.append("image/sl" + str(i + 1) + ".png")

running = True
walkman = 0
walkstone = 0
walkslime = 0
jumpCount = 11

while running:
    FRAME_PER_SECOND_CLOCK = pygame.time.Clock()

    FRAME_PER_SECOND_CLOCK.tick(60)

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if page == "game":
                    if man.base <= man.y:
                        if jumpCount >= 11:
                            jumpCount = 0

        elif event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if page == "main":
                if image_start_rect.collidepoint(mouse_pos):
                    print('game')
                    page = "game"
                elif image_exit_rect.collidepoint(mouse_pos):
                    print('exit')
                    running = False
                elif image_tutorial_rect.collidepoint(mouse_pos):
                    print('tutorial')
                    page = "tutorial"
            elif page == "game":
                if (slime1.getRect).collidepoint(mouse_pos):
                    slime1.health -= 35
                    print(slime1.health)
                if (slime2.getRect).collidepoint(mouse_pos):
                    slime2.health -= 35
                    print(slime2.health)
                if (slime3.getRect).collidepoint(mouse_pos):
                    slime3.health -= 35
                    print(slime3.health)
                if (slime4.getRect).collidepoint(mouse_pos):
                    slime4.health -= 35
                    print(slime4.health)
                if image_back_rect.collidepoint(mouse_pos):
                    print('back')
                    page = "main"
                    kill = 0
                    man.heart = 3
            elif page == "gameover":
                if image_back_rect.collidepoint(mouse_pos):
                    print('back')
                    page = "main"
                    kill = 0
                    man.heart = 3
                    stone.x = random.randint(1500, 3500)
                    stone.y = random.randint(200, 400)
                    slime1.x = random.randint(1500, 3500)
                    slime1.y = random.randint(200, 400)
                    slime1.health = 100
                    slime2.x = random.randint(1500, 3500)
                    slime2.y = random.randint(200, 400)
                    slime2.health = 100
                    slime3.x = random.randint(1500, 3500)
                    slime3.y = random.randint(200, 400)
                    slime3.health = 100
                    slime4.x = random.randint(1500, 3500)
                    slime4.y = random.randint(200, 400)
                    slime4.health = 100
            elif page == "tutorial":
                if image_back_rect.collidepoint(mouse_pos):
                    print('back')
                    page = "main"
                    kill = 0
    # screen
    if page == "main":
        slime1.speed = 0
        slime2.speed = 0
        slime3.speed = 0
        slime4.speed = 0
        slime1.x = random.randint(1500, 3500)
        slime2.x = random.randint(1500, 3500)
        slime3.x = random.randint(1500, 3500)
        slime4.x = random.randint(1500, 3500)
        stone.x = random.randint(1500, 3500)
        for i in range(0, SCREEN_WIDTH, 128):
            for j in range(-128, SCREEN_HEIGHT, 128):
                screen.blit(image_bg, (i, j+loop_bg, SCREEN_WIDTH, SCREEN_HEIGHT))
        loop_bg += 0.25
        if loop_bg == 128:
            loop_bg = 0

        screen.blit(image_start, image_start_rect)
        screen.blit(image_tutorial, image_tutorial_rect)
        screen.blit(image_exit, image_exit_rect)
        screen.blit(text, textRect)
    elif page == "game":
        if (slime1.x <= man.x) or (slime2.x <= man.x) or (slime3.x <= man.x) or (slime4.x <= man.x):
            man.heart -= 1
            if slime1.x <= man.x:
                slime1.x = random.randint(1500, 3500)
                slime1.y = random.randint(200, 400)
                slime1.health = 100
                slime1.speed += 1
            if slime2.x <= man.x:
                slime2.x = random.randint(1500, 3500)
                slime2.y = random.randint(200, 400)
                slime2.health = 100
                slime2.speed += 1
            if slime3.x <= man.x:
                slime3.x = random.randint(1500, 3500)
                slime3.y = random.randint(200, 400)
                slime3.health = 100
                slime3.speed += 1
            if slime4.x <= man.x:
                slime4.x = random.randint(1500, 3500)
                slime4.y = random.randint(200, 400)
                slime4.health = 100
                slime4.speed += 1
            print(man.heart)
            if man.heart <= 0:
                page = "gameover"
        elif stone.x <= 60 and man.y > 470 and stone.x >= 20:
            page = "gameover"
        else:
            if walkman == 11:
                walkman = 0
            if walkstone == 11:
                walkstone = 0
            if walkslime == 8:
                walkslime = 0

            if stone.x < -64:
                stone.x = random.randint(1500, 3500)
                stone.y = random.randint(200, 400)
            if slime1.health < 0 or slime1.x < -64:
                slime1.x = random.randint(1500, 3500)
                slime1.y = random.randint(200, 400)
                slime1.health = 100
                kill += 1
                slime1.speed += 1
            if slime2.health < 0 or slime2.x < -64:
                slime2.x = random.randint(1500, 3500)
                slime2.y = random.randint(200, 400)
                slime2.health = 100
                kill += 1
                slime2.speed += 1
            if slime3.health < 0 or slime3.x < -64:
                slime3.x = random.randint(1500, 3500)
                slime3.y = random.randint(200, 400)
                slime3.health = 100
                kill += 1
                slime3.speed += 1
            if slime4.health < 0 or slime4.x < -64:
                slime4.x = random.randint(1500, 3500)
                slime4.y = random.randint(200, 400)
                slime4.health = 100
                kill += 1
                slime4.speed += 1


            if jumpCount <= 10:
                man.y -= 30
                jumpCount += 1
            drawBG(screen)
            for i in range(0, SCREEN_WIDTH, 128):
                screen.blit(image_map, (i, SCREEN_HEIGHT-100, SCREEN_WIDTH, SCREEN_HEIGHT))

            text_kill = font_main.render(f'Kill : {kill}', True, black, None)
            text_killRect = text.get_rect()
            text_killRect.center = (350, 50)
            heart_count(screen, man.heart)
            screen.blit(text_kill, text_killRect)
            screen.blit(image_back, image_back_rect)

            man.update(screen, imagesMan[walkman])
            stone.update(screen, imageStone[walkstone])
            slime1.update(screen, imagesSlime[walkslime])
            slime1.move(screen)
            slime2.update(screen, imagesSlime[walkslime])
            slime2.move(screen)
            slime3.update(screen, imagesSlime[walkslime])
            slime3.move(screen)
            slime4.update(screen, imagesSlime[walkslime])
            slime4.move(screen)

            stone.move(screen)

            walkman += 1
            walkstone += 1
            walkslime += 1

    elif page == "gameover":
        for i in range(0, SCREEN_WIDTH, 128):
            for j in range(-128, SCREEN_HEIGHT, 128):
                screen.blit(image_bg, (i, j + loop_bg, SCREEN_WIDTH, SCREEN_HEIGHT))
        loop_bg += 0.25
        if loop_bg == 128:
            loop_bg = 0
        screen.blit(image_back, image_back_rect)
        screen.blit(text_kill, (SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2))
    elif page == "tutorial":
        for i in range(0, SCREEN_WIDTH, 128):
            for j in range(-128, SCREEN_HEIGHT, 128):
                screen.blit(image_bg, (i, j + loop_bg, SCREEN_WIDTH, SCREEN_HEIGHT))
        loop_bg += 0.25
        if loop_bg == 128:
            loop_bg = 0
        screen.blit(image_back, image_back_rect)
        screen.blit(text_tutorial1, text_tutorialRect1)
        screen.blit(text_tutorial2, text_tutorialRect2)
        screen.blit(text_tutorial3, text_tutorialRect3)

    mouse_pos = pygame.mouse.get_pos()
    screen.blit(image_mouse, (mouse_pos[0]-30, mouse_pos[1]-30))
    pygame.display.update()


pygame.quit()
