# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit

background_image = 'sushiplate.jpg'
mouse_image = 'fugu.png'
SCREEN_SIZE = (640, 480)

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('hello world!')

# 可以用pygame.font.get_fonts()方法来获得当前系统所有可用字体
# print(pygame.font.get_fonts())
font = pygame.font.Font("DroidSans.ttf", 40)
# font = pygame.font.SysFont("arial", 16)
text_surface = font.render(u"hello", True, (0, 0, 255))

background = pygame.image.load(background_image).convert()
mouse_cursor = pygame.image.load(mouse_image).convert_alpha()

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # if event.type == KEYDOWN:
        #     if event.key == K_f:
        #         Fullscreen = not Fullscreen
        #         if Fullscreen:
        #             screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        #         else:
        #             screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        screen.blit(background, (0, 0))
        # if event.type == VIDEORESIZE:
        #     SCREEN_SIZE = event.size
        #     screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        #     pygame.display.set_caption("Window resized to " + str(event.size))
        #
        # screen_width, screen_height = SCREEN_SIZE
        # # 这里需要重新填满窗口
        # for y in range(0, screen_height, background.get_height()):
        #     for x in range(0, screen_width, background.get_width()):
        #         screen.blit(background, (x, y))

    screen.blit(text_surface, (120, 120))
    pygame.display.update()
