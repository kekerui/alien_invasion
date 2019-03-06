#coding=utf-8
import pygame
class Person():
    def __init__(self, screen):
        """初始化人物并设置其初始位置"""
        self.screen = screen
        # 加载人物图像并获取其外接矩形
        self.image = pygame.image.load("images/person.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将人物放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        # 在指定位置绘制人物
        self.screen.blit(self.image, self.rect)