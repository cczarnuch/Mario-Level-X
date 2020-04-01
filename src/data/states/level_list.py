__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup, tools
from .. import constants as c
from .. components import info, mario


class LevelList(tools._State):
    def __init__(self):
        """Initializes the state"""
        tools._State.__init__(self)
        self.selected = {
            'level' : ''
        }

        persist = {c.COIN_TOTAL: 0,
                   c.SCORE: 0,
                   c.LIVES: 3,
                   c.TOP_SCORE: 0,
                   c.CURRENT_TIME: 0.0,
                   c.LEVEL_STATE: None,
                   c.CAMERA_START_X: 0,
                   c.MARIO_DEAD: False}

        self.startup(0.0, persist)
    def startup(self, current_time, persist):
        """Called every time the game's state becomes this one.  Initializes
        certain values"""
        self.key_pressed=True
        self.next = c.LOAD_SCREEN
        self.persist = persist
        self.game_info = persist
        self.sprite_sheet = setup.GFX['title_screen']
        self.setup_background()
        self.setup_mario()
        self.setup_cursor()
        self.setup_list()
       
    def setup_list(self):
        self.levels = tools.get_level_list()
        self.level_count = len(self.levels)
        

    def setup_cursor(self):
        """Creates the mushroom cursor to select 1 or 2 player game"""
        self.cursor = pg.sprite.Sprite()
        dest = (150, 130)
        self.cursor.image, self.cursor.rect = self.get_image(
            24, 160, 8, 8, dest, setup.GFX['item_objects'])
        self.selected_index = 0


    def setup_mario(self):
        """Places Mario at the beginning of the level"""
        self.mario = mario.Mario()
        self.mario.rect.x = 110
        self.mario.rect.bottom = c.GROUND_HEIGHT


    def setup_background(self):
        """Setup the background image to blit"""
        self.background = setup.GFX['level_1']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                   (int(self.background_rect.width*c.BACKGROUND_MULTIPLER),
                                    int(self.background_rect.height*c.BACKGROUND_MULTIPLER)))
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

        self.image_dict = {}



    def get_image(self, x, y, width, height, dest, sprite_sheet):
        """Returns images and rects to blit onto the screen"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(sprite_sheet, (0, 0), (x, y, width, height))
        if sprite_sheet == setup.GFX['title_screen']:
            image.set_colorkey((255, 0, 220))
            image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        else:
            image.set_colorkey(c.BLACK)
            image = pg.transform.scale(image,
                                   (int(rect.width*3),
                                    int(rect.height*3)))

        rect = image.get_rect()
        rect.x = dest[0]
        rect.y = dest[1]
        return (image, rect)


    def update(self, surface, keys, current_time):
        """Updates the state every refresh"""
        self.current_time = current_time
        self.game_info[c.CURRENT_TIME] = self.current_time
        self.update_cursor(keys)

        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(self.mario.image, self.mario.rect)
        surface.blit(self.cursor.image, self.cursor.rect)
        self.draw_level_list(surface)

    def draw_level_list(self,surface):
        x,y = 180,130
        
        for i,filename in enumerate(self.levels):
            displayname = filename[:-5].upper() #remove .json
            size = 30
            text = tools.get_surface_text(str(i+1) + '. ' +displayname, c.BLACK, size)
            surface.blit(text, (x,y))
            y+=size

    def update_cursor(self, keys):
        """Update the position of the cursor"""
        #input_list = [pg.K_RETURN, pg.K_a, pg.K_s]
        
        if (keys[pg.K_RETURN] or keys[pg.K_DOWN] or keys[pg.K_UP]) and self.key_pressed: return
        self.key_pressed = False
        if keys[pg.K_RETURN]:
            #filename
            self.selected['level'] = self.levels[self.selected_index]
            self.next = c.LEVEL1
            self.done = True
        elif keys[pg.K_ESCAPE]:
            self.next = c.MAIN_MENU
            self.done = True
        elif keys[pg.K_DOWN] and self.selected_index + 1 < self.level_count:
            self.selected_index += 1
            self.key_pressed = True
            self.cursor.rect.y += 40
        elif keys[pg.K_UP] and self.selected_index > 0:
            self.selected_index -= 1
            self.key_pressed = True
            self.cursor.rect.y -= 40

