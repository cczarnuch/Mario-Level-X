## @file coin_box.py
#  @title Coin Box Component Class
__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
from .. import tools
from .. import constants as c
from . import powerups
from . import coin


## @brief A class to represent a Coin Box
class Coin_box(pg.sprite.Sprite):

    ## @brief Coin Box Constructor
    #  @details intializes Coin Box component
    #  @param x x-pixel coordinate 
    #  @param y y-pixel coordinate 
    #  @param contents string representing contents inside the coin box when bumped (optional)
    #  @param group pygame.sprite group that the powerup belongs to (optional) 
    def __init__(self, x, y, contents='coin', group=None):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['tile_set']
        self.frames = []
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()

        self.set_dimensions(x,y)
        self.mask = pg.mask.from_surface(self.image)
        self.animation_timer = 0
        self.first_half = True   # First half of animation cycle
        self.state = c.RESTING
        self.gravity = 1.2
        self.y_vel = 0
        self.contents = contents
        self.group = group

    ## @brief sets the x and y values of the screen
    #  @param x x-pixel coordinate 
    #  @param x y-pixel coordinate 
    def set_dimensions(self,x,y):
        x -= self.rect.w // 2
        y -= self.rect.h // 2
        self.rect.x = tools.round_to_multiple(x, self.rect.w)
        refy = max(0,tools.round_to_multiple(c.GROUND_HEIGHT - y, self.rect.h))
        self.rect.y = c.GROUND_HEIGHT - refy
        #return y after bounce
        self.rest_height = self.rect.y


    ## @brief Gets object x and y values as dictionary
    #  @return dictionary object with the x,y,content key values
    def serialize(self):
        return {
            'x': self.rect.x,
            'y': self.rect.y,
            'contents': self.contents
        }

    def get_image(self, x, y, width, height):
        """Extract image from sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)

        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image


    def setup_frames(self):
        """Create frame list"""
        self.frames.append(
            self.get_image(384, 0, 16, 16))
        self.frames.append(
            self.get_image(400, 0, 16, 16))
        self.frames.append(
            self.get_image(416, 0, 16, 16))
        self.frames.append(
            self.get_image(432, 0, 16, 16))


    def update(self, game_info):
        """Update coin box behavior"""
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_states()


    def handle_states(self):
        """Determine action based on RESTING, BUMPED or OPENED
        state"""
        if self.state == c.RESTING:
            self.resting()
        elif self.state == c.BUMPED:
            self.bumped()
        elif self.state == c.OPENED:
            self.opened()


    def resting(self):
        """Action when in the RESTING state"""
        if self.first_half:
            if self.frame_index == 0:
                if (self.current_time - self.animation_timer) > 375:
                    self.frame_index += 1
                    self.animation_timer = self.current_time
            elif self.frame_index < 2:
                if (self.current_time - self.animation_timer) > 125:
                    self.frame_index += 1
                    self.animation_timer = self.current_time
            elif self.frame_index == 2:
                if (self.current_time - self.animation_timer) > 125:
                    self.frame_index -= 1
                    self.first_half = False
                    self.animation_timer = self.current_time
        else:
            if self.frame_index == 1:
                if (self.current_time - self.animation_timer) > 125:
                    self.frame_index -= 1
                    self.first_half = True
                    self.animation_timer = self.current_time

        self.image = self.frames[self.frame_index]


    def bumped(self):
        """Action after Mario has bumped the box from below"""
        self.rect.y += self.y_vel
        self.y_vel += self.gravity

        if self.rect.y > self.rest_height + 5:
            self.rect.y = self.rest_height
            self.state = c.OPENED
            if self.contents == 'mushroom':
                self.group.add(powerups.Mushroom(self.rect.centerx, self.rect.y))
            elif self.contents == 'fireflower':
                self.group.add(powerups.FireFlower(self.rect.centerx, self.rect.y))
            elif self.contents == '1up_mushroom':
                self.group.add(powerups.LifeMushroom(self.rect.centerx, self.rect.y))


        self.frame_index = 3
        self.image = self.frames[self.frame_index]


    def start_bump(self, score_group):
        """Transitions box into BUMPED state"""
        self.y_vel = -6
        self.state = c.BUMPED

        if self.contents == 'coin':
            self.group.add(coin.Coin(self.rect.centerx,
                                     self.rect.y,
                                     score_group))
            setup.SFX['coin'].play()
        else:
            setup.SFX['powerup_appears'].play()


    def opened(self):
        """Placeholder for OPENED state"""
        pass
