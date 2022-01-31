import sys, random, math
import pygame as pg
import pygame.math as pymath
import pygame.draw as pydraw

def quit():
    pg.quit()
    sys.exit()

class Player:
    def __init__(self):
        self.pos = pymath.Vector2(200, 200)
        self.size = pymath.Vector2(100, 100)
        self.rect = pg.Rect(self.pos.x, self.pos.y, self.size.x, self.size.y)
        self.col = pymath.Vector3(22, 34, 82)

        self.surf = pg.image.load(r'C:\Users\Glenn\Downloads\player.png').convert_alpha()
        self.surf = pg.transform.scale(self.surf, (int(self.size.x), int(self.size.y)))

    def tick(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= 4
        if keys[pg.K_s]:
            self.pos.y += 4
        if keys[pg.K_a]:
            self.pos.x -= 4
        if keys[pg.K_d]:
            self.pos.x += 4

        if self.rect.left <= 0 + -19:
            self.pos.x += 4
        if self.rect.top <= 0 + -5:
            self.pos.y += 4
        if self.rect.right >= SCREEN_WIDTH - 1:
            self.pos.x -= 4
        if self.rect.bottom >= SCREEN_HEIGHT - 7:
            self.pos.y -= 4

        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

        screen.blit(self.surf, self.rect)

pg.mixer.pre_init(44100, -16, 2, 512)
pg.init()


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1140
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.toggle_fullscreen()
clock = pg.time.Clock()
game_font = pg.font.Font(None, 25)
isRunning = True
FPS = 60

player = Player()

while isRunning == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

    screen.fill((140, 140, 140))

    player.tick()

    pg.display.update()
    clock.tick(FPS)

quit()