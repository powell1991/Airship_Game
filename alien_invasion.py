import sys
import pygame
from settings import Settings
from ship import  Ship
import game_function as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings  = Settings()
    #screen = pygame.display.set_mode((1200,600))                  #创建显示窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))     #通过创建settings模块创建的类
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)              #创建一搜飞船
    bullets = Group()                             #创建一个用于存储子弹的编组
    bg_color = (230,230,230)        #设置背景颜色

    while True:                                               #开始游戏的主循环
        gf.check_events(ai_settings, screen, ship, bullets)   #通过创建的game_function函数重构监视键盘和鼠标事件，并传递移动参数
        ship.update()                                         #调用ship类的update方法
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)         #通过创建的game_function函数重构重绘屏幕
        """
        for event in pygame.event.get():       #使用这个方法进行事件循环
            if event.type == pygame.QUIT:      #单击窗口关闭按钮时，检测此方法事件
                sys.exit()        
        #每次循环都重绘屏幕
        #screen.fill(bg_color)                #用背景颜色填充屏幕
        screen.fill(ai_settings.bg_color)     #通过创建settings模块创建的类定义颜色
        ship.blitme()                         
        pygame.display.flip()                 #让最近的屏幕可见
        """
run_game()
