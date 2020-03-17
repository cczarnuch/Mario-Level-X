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
        self.rect.x = x * 43
        self.rect.y = y * 43 - 22
        self.state = None

class Pipe(pg.sprite.Sprite):
    """Moveable Pipes"""
    def __init__(self, x, height):
        pg.sprite.Sprite.__init__(self)
        self.pipe_bottom = setup.GFX['pipe_bottom']
        self.pipe_top = setup.GFX['pipe_top']
        self.set_dimensions(x,height)

    def set_dimensions(self, x, height):
        pipe_bottom = self.pipe_bottom
        pipe_top = self.pipe_top
        pipe_bottom = pg.transform.scale(pipe_bottom, (86, c.GROUND_HEIGHT - height))
        pipe_top = pg.transform.scale(pipe_top, (86,43))
        pipe_bottom.blit(pipe_top,(0,0))
        self.image = pipe_bottom
        self.rect = self.image.get_rect()
        self.rect.y = height
        self.rect.x = x

    def serialize(self):
        return {
            "x": self.rect.x,
            "height": self.rect.y
        }


class Ground(pg.sprite.Sprite):
    """Invisible ground platform"""
    def __init__(self, x, y, width):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width*43, 60)).convert()

        self.rect = self.image.get_rect()
        self.rect.x = x * 43
        self.rect.y = y
        self.state = None

    def serialize(self):
        return{
            "xStart": 0,
            "xEnd": 69
        }

class Hole:
    def __init__(self, x1,x2):
        self.x1 = x1
        self.x2 = x2


class Step(pg.sprite.Sprite):
    """Step blocks"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        width, height = 16, 16
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['tile_set']
        image = pg.Surface((width, height)).convert()
        image.blit(self.sprite_sheet, (0, 0), (0, 16, 16, 16))
        image = pg.transform.scale(image,(int(image.get_width()*c.BRICK_SIZE_MULTIPLIER),int(image.get_height()*c.BRICK_SIZE_MULTIPLIER)))
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x * 43
        self.rect.y = y * 43 - 22
        self.state = None
    
    def serialize(self):
        return {
            'x': self.x,
            'y': self.y,
        }
