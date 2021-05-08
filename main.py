from sprites import *
import random

def collide(Sprite1 , Sprite2):
    if ((Sprite1.x <= Sprite2.x <= Sprite1.x + Sprite1.width
         and Sprite1.y <= Sprite2.y <= Sprite1.y + Sprite1.height)
            or (Sprite1.x <= Sprite2.x + Sprite2.width <= Sprite1.x + Sprite1.width
                and Sprite1.y <= Sprite2.y + Sprite2.height <= Sprite1.y + Sprite1.height)
            or (Sprite2.x <= Sprite1.x <= Sprite2.x + Sprite2.width
                and Sprite2.y <= Sprite1.y + Sprite1.height <= Sprite2.y + Sprite2.height)
            or (Sprite2.x <= Sprite1.x + Sprite1.width <= Sprite2.x + Sprite2.width
                and Sprite2.y <= Sprite1.y <= Sprite2.y + Sprite2.height)):
        return True
    else:
        return False

pygame.init()
font1 = pygame.font.Font(None,45)
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


firetimer = 0

game = True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    firetimer+=1
    if firetimer==60:
        firetimer=0
        fire = Fireball(random.randint(0, SCREEN_WIDTH),
                        -100, -90)
        fire.speedY = 5
        fireballs.append(fire)

    for f in fireballs:
        f.update()
        f.y += f.speedY
        f.x += f.speedX
        if collide(f,player):
            player.hp-=10
            fireballs.remove(f)
        if f.y>SCREEN_HEIGHT and f in fireballs:
            fireballs.remove(f)

    text_hp = font1.render( str(player.hp),
                           True,
                           (0, 0, 0))

    window.fill( (255,255,255) )# заливаем окно белым цветом
    window.blit(zemlya.image,
                (zemlya.x,zemlya.y))
    window.blit(player.image,
                (player.x,player.y))#!!!!!!!!!!!!!
    for fire in fireballs:
        window.blit(fire.image,
                    (fire.x,fire.y) )
    window.blit(text_hp,
                (0,0))

    clock.tick(60)
    pygame.display.update()
pygame.quit()