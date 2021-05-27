import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen ,ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True  # 向右移动飞船
    elif event.key == pygame.K_LEFT:
        ship.movimg_left = True  # 向左移
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.movimg_left = False


def check_events(ai_settings, screen, ship, bullets):               #定义移动的形参
    """相应按键和鼠标事件"""
    for event in pygame.event.get():  # 使用这个方法进行事件循环
        if event.type == pygame.QUIT:  # 单击窗口关闭按钮时，检测此方法事件
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)   #调用重构后的函数
            """
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True       #向右移动飞船
            elif event.key == pygame.K_LEFT:
                ship.movimg_left = True        #向左移
            """


        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)      #调用重构后的函数
            """
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.movimg_left = False
            """
def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)  # 通过创建settings模块创建的类定义颜色
    for bullet in bullets.sprites():
        ship.blitme()
    pygame.display.flip()  # 让最近的屏幕可见

