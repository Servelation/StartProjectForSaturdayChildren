import pygame


class Sprite:
    def __init__(self, x, y, img):
        self.image = img
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()


class Player(Sprite):
    def __init__(self, x, y, img):
        Sprite.__init__(self, x, y, img)
        self.hp = 100
        self.speedX = 5
        self.is_in_air = False
        self.jumppower= -18
        self.dir = 'left'
        self.cadrsR = [pygame.image.load(r'images/player/r1.png'),
                       pygame.image.load(r'images/player/r2.png'),
                       pygame.image.load(r'images/player/r3.png'),
                       pygame.image.load(r'images/player/r4.png'),
                       pygame.image.load(r'images/player/r5.png'),
                       pygame.image.load(r'images/player/r6.png'),
                       ]
        self.img_jump_r = pygame.image.load(r'images/player/pr.png')
        self.cadrsL = []
        for x in self.cadrsR:
            l_image = pygame.transform.flip(x, True, False)
            self.cadrsL.append(l_image)
        self.img_jump_l = pygame.transform.flip(self.img_jump_r, True, False)
        #номер кадра
        self.n_cadr = 0
        #счетчик задержки между кадрами
        self.counter = 0

    def update(self, keys):
        if (keys[pygame.K_d] or
                keys[pygame.K_a]):
            if keys[pygame.K_d]:
                self.x += self.speedX
                self.dir = 'right'
            if keys[pygame.K_a]:
                self.x -= self.speedX
                self.dir = 'left'

            if self.dir == 'right':
                self.image = self.cadrsR[self.n_cadr]
            else:
                self.image = self.cadrsL[self.n_cadr]
            #Увеличиваем счетчик задержки
            self.counter+=1
            if self.counter == 9: #если прошло 9 тиков игры
                # меняем кадр на следующий:
                self.n_cadr = 0 if self.n_cadr == 5 else self.n_cadr + 1
                self.counter=0
        else:
            if self.dir == 'right':
                self.image = self.cadrsR[0]
            else:
                self.image = self.cadrsL[0]

class Fireball(Sprite):
    def __init__(self,x,y,angle):
        Sprite.__init__(self,x,y,pygame.image.load(r'images/fireball/hfireball1.png'))
        self.cadrs = [
            pygame.image.load(r'images/fireball/hfireball1.png'),
            pygame.image.load(r'images/fireball/hfireball2.png'),
            pygame.image.load(r'images/fireball/hfireball3.png'),
            pygame.image.load(r'images/fireball/hfireball4.png'),
            pygame.image.load(r'images/fireball/hfireball5.png'),
        ]
        #Цикл, который в переменную i закидывает числа от 0 до размера списка кадров(до 5)
        for i in range(len(self.cadrs)):
            img = pygame.transform.scale(self.cadrs[i], [
                int(  self.cadrs[i].get_width()*0.2  ),
                int(  self.cadrs[i].get_height()*0.2 )
            ])
            img = pygame.transform.rotate(img,angle)
            self.cadrs[i]= img
        self.width = self.cadrs[0].get_width()
        self.height = self.cadrs[0].get_height()
        self.image = self.cadrs[0]
        self.n_cadr = 0
        self.counter = 0

    def update(self):
        self.counter += 1
        if self.counter == 7:  # если прошло 9 тиков игры
            # меняем кадр на следующий:
            self.image = self.cadrs[self.n_cadr]
            self.n_cadr = 0 if self.n_cadr == len(self.cadrs)-1 else self.n_cadr + 1
            self.counter = 0

