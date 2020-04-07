## @file collider.py
#  @title Collider Classes

__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup,tools
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


## @brief A class to represent a Pipe
class Pipe(pg.sprite.Sprite):
    ## @brief Pipe Constructor
    #  @details intializes Pipe component
    #  @param x x-pixel coordinate 
    #  @param height number of pixels above the ground 
    def __init__(self, x, height):
        pg.sprite.Sprite.__init__(self)
        self.pipe_bottom = setup.GFX['pipe_bottom']
        self.pipe_top = setup.GFX['pipe_top']
        self.set_dimensions(x,height)


    ## @brief sets the x and height values of the screen
    #  @param x x-pixel coordinate 
    # #  @param height number of pixels above the ground 
    def set_dimensions(self, x, height):
        pipe_bottom = self.pipe_bottom
        pipe_top = self.pipe_top
        scaley =  max(0,c.GROUND_HEIGHT - height)
        pipe_bottom = pg.transform.scale(pipe_bottom, (86, scaley))
        pipe_top = pg.transform.scale(pipe_top, (86,43))
        pipe_bottom.blit(pipe_top,(0,0))
        self.image = pipe_bottom
        self.rect = self.image.get_rect()
        self.rect.y = height
        self.rect.x = tools.round_to_multiple(x, self.rect.w)
        

    ## @brief Gets object x and height values as dictionary
    #  @return dictionary object with the x,height key values
    def serialize(self):
        return {
            "x": self.rect.x,
            "height": self.rect.y
        }


## @brief A class to represent a Ground
class Ground(pg.sprite.Sprite):
    ## @brief Ground
    #  @details intializes Ground component
    #  @param x x-pixel coordinate 
    #  @param y y-pixel coordinate 
    #  @param width pixel width of ground 
    def __init__(self, x, y, width):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width*43, 60)).convert()

        self.rect = self.image.get_rect()
        self.rect.x = x * 43
        self.rect.y = y
        self.state = None


    ## @brief Gets dictionary with ground data
    #  @return dictionary object with the start x,y,width key values
    def serialize(self):
        return{
            "x": self.rect.x,
            "y": self.rect.y,
            "width": self.rect.w
        }


## @brief A class to represent a Step
class Step(pg.sprite.Sprite):
    ## @brief Step Constructor
    #  @details intializes Step component
    #  @param x x-pixel coordinate 
    #  @param y y-pixel coordinate 
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
        self.set_dimensions(x,y)
        self.state = None
    

    ## @brief sets the x and height values of the screen
    #  @param x x-pixel coordinate 
    #  @param y y-pixel coordinate 
    def set_dimensions(self,x,y):
        x -= self.rect.w // 2
        y -= self.rect.h // 2
        self.rect.x = tools.round_to_multiple(x, self.rect.w)
        refy = max(0,tools.round_to_multiple(c.GROUND_HEIGHT - y, self.rect.h))
        self.rect.y = c.GROUND_HEIGHT - refy
    
    ## @brief Gets dictionary with step data
    #  @return dictionary object with the start x,y key values
    def serialize(self):
        return {
            'x': self.rect.x,
            'y': self.rect.y,
        }
