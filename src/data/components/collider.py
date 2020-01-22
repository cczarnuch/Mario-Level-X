__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
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
        pipe_bottom = setup.GFX['pipe_bottom']

        pipe_bottom = pg.transform.scale(pipe_bottom, (83,height))
        pipe_top = setup.GFX['pipe_top']
        pipe_top = pg.transform.scale(pipe_top, (83,40))
        pipe_bottom.blit(pipe_top,(0,0))
        self.image = pipe_bottom
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 535 - height

class Ground(pg.sprite.Sprite):
    """Invisible ground platform"""
    def __init__(self, x, y, width):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, 60)).convert()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None

class Step(pg.sprite.Sprite):
    """Step blocks"""
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['tile_set']

        self.image = pg.Surface((width, height)).convert()
        rect = self.image.get_rect()
        #self.image.fill(c.RED)
        self.image.blit(self.sprite_sheet, (0, 0), (8, 0, 8, 8))
        self.image = pg.transform.scale(self.image,(40, 40))
                                        # (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                        # int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None
