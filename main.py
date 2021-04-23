from sprites import *
import random

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
clock = pygame.time.Clock()
window = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
player = Player(0,500,
                pygame.image.load(r'images/player/r1.png'))
zemlya = Sprite(0,600,
                 pygame.image.load(r'images/z1.png'))
fireballs = []
fire = Fireball(random.randint(0,SCREEN_WIDTH),
                    0,-90)
fire.speedY = 5
fireballs.append(fire)

game = True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    player.update(keys)


    for f in fireballs:
        f.update()
        f.y += f.speedY


    window.fill( (255,255,255) )# заливаем окно белым цветом
    window.blit(zemlya.image,
                (zemlya.x,zemlya.y))
    window.blit(player.image,
                (player.x,player.y))#!!!!!!!!!!!!!
    for fire in fireballs:
        window.blit(fire.image,
                    (fire.x,fire.y) )
    clock.tick(60)
    pygame.display.update()
pygame.quit()