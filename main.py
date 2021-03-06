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
GRAVITY = 1
clock = pygame.time.Clock()
window = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
player = Player(0,500,
                pygame.image.load(r'images/player/r1.png'))
zemlya = Sprite(0,600,
                 pygame.image.load(r'images/z1.png'))

platforms = []
plat = Sprite(600,450,
                  pygame.image.load(r'images/ground.png'))
platforms.append(plat)
plat = Sprite(300,350,
                  pygame.image.load(r'images/ground.png'))
platforms.append(plat)

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
        ran = random.randint(0,1)
        if ran == 0:
            fire = Fireball(SCREEN_WIDTH,
                            random.randint(0, SCREEN_HEIGHT),
                            180)
            fire.speedX = -5
            fireballs.append(fire)
        elif ran == 1:
            fire = Fireball(random.randint(0, SCREEN_WIDTH),
                            -100,
                            -90)
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

    # ?????????????? ????????????????, ?? ?????????????? ?????? ?????????? ???? ????????????????!
    k = 0
    for platf in platforms:#?????? ???????????? ??????????????????
        if collide(player, platf):
            if platf.y<player.y+player.height<platf.y+platf.height:# ?????????? ?????????????? ???????????? ????????????
                if player.speedY>0:#?????????? ?????? ???????????????????????? ????????????
                # ?? ??????????????, ?? ???? ???? ????????????!
                    player.is_in_air =False #?????????? ???? ?? ??????????????!
        else:# ???????? ???? ???????????????? ??????????????????, +1!
            k+=1
    if k== len(platforms):#???????? ?????????? ???? ???????????????? ???????? ???????????????? - ???? ?? ??????????????!
        player.is_in_air = True

    if collide(player, zemlya):# ???????? ?????????? ???????????????? ?????????? - ???? ???? ?? ??????????????!
        player.is_in_air = False

    if player.is_in_air:#???????? ?????????? ?? ??????????????, ???????????? ??????!
        player.speedY += GRAVITY
    else:#???????? ???? ?? ??????????????, ???? ?????????????????????????? ?????? ???????????????? 0
        player.speedY=0
        if keys[pygame.K_SPACE]:#?????????????? ???????????? ???????? ???? ?? ??????????????!
            player.speedY = player.jumppower
            #?????? ?????? ???? ??????????????, ???? ?????????? ?? ??????????????!
            player.is_in_air= True
    player.y +=player.speedY




    text_hp = font1.render( 'HP: ' + str(player.hp),
                           True,
                           (0, 0, 0))
    text_fps = font1.render('FPS: '+ str(int(clock.get_fps())),
                           True,
                           (0, 0, 0))
    window.fill( (255,255,255) )# ???????????????? ???????? ?????????? ????????????
    window.blit(zemlya.image,
                (zemlya.x,zemlya.y))
    window.blit(player.image,
                (player.x,player.y))#!!!!!!!!!!!!!
    for plat in platforms:
        window.blit(plat.image,
                    (plat.x,plat.y))
    for fire in fireballs:
        window.blit(fire.image,
                    (fire.x,fire.y) )
    window.blit(text_hp,
                (0,0))
    window.blit(text_fps,
                (0,40))
    clock.tick(60)
    pygame.display.update()
pygame.quit()