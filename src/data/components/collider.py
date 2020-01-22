__author__ = 'justinarmstrong'

import pygame as pg
from .. import constants as c
# from .. import setup

class Collider(pg.sprite.Sprite):
    """Invisible sprites placed overtop background parts
    that can be collided with (pipes, steps, ground, etc."""
    def __init__(self, x, y, width, height, name='collider'):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height)).convert()
        #self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None

class Pipe(pg.sprite.Sprite):
    """Moveable Pipes"""
    def __init__(self, x, height):
        pg.sprite.Sprite.__init__(self)
        #self.image = pg.Surface((83, height))
        #self.image.fill(c.GREEN)
        pipe_bottom = pg.image.load('./resources/graphics/pipe_bottom.png')
        #self.image = pg.transform.scale(pipe_bottom, (83, height))
        pipe_bottom = pg.transform.scale(pipe_bottom, (83,height))
        #todo
        pipe_top = pg.image.load('./resources/graphics/pipe_top.png')
        pipe_top = pg.transform.scale(pipe_top, (83,40))
        pipe_bottom.blit(pipe_top,(0,0))
        self.image = pipe_bottom
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 535 - height