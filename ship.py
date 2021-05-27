import pygame
class Ship():
    def __init__(self, ai_settings, screen):   #添加ai_settings形参来定义飞船的移动速度
        """初始化飞船并设置初始化位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        #移动标志
        self.moving_right = False    #定义右移
        self.movimg_left = False     #定义左移


    def update(self):
        """根据移动标志调整飞船的位置"""
        #if self.moving_right:
        if self.moving_right and self.rect.right < self.screen_rect.right:  #限制飞船的移动范围
            #self.rect.centerx += 1   #右移
            self.center += self.ai_settings.ship_speed_factor  #根据飞船的center值，而不是rect
        #if self.movimg_left:
        if self.movimg_left and self.rect.left > 0:
            #self.rect.centerx -= 1   #左移
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center   #根据self.center更新rect对象

    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
