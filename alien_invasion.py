#coding=utf-8
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from person import  Person
from pygame.sprite import Group
from game_stats import GameStats
def run_game():
    # 初始化pygame,设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aline Invasion")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于管理子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            # 更新飞船的状态
            ship.update()
            # 更新子弹
            bullets.update()
            # 删除已消失的子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            #print(len(bullets))
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
