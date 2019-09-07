import pygame
import neat
import time
import os
import random

# SCREEN DIMENSIONS
WIN_HEIGHT = 600
WIN_WIDTH = 800

#LOAD IMAGES
BIRD_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))] 
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

#BIRD CLASS
class Bird:
    IMGS = BASE_IMG
    MAX_ROT = 25
    MAX_VEL = 20
    ANIMATION_TIME = 5


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.titl = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]


    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):

        