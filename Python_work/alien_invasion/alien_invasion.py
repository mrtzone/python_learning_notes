import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import  game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('外星人入侵')
    #创建一个外星人
    alien = Alien(ai_settings,screen)

    #创建一艘飞船，一个子弹组和一个外星人编组
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings,screen,aliens)

    #开始游戏的主循环blitme
    while True:

        #监视键盘和鼠标事件
        gf.check_event(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        #更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings,screen,ship,alien,bullets)

print('请开始游戏吧！！！')
run_game()



