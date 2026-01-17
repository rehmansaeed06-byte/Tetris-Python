from grid import Grid
from blocks import *
import random
import pygame
class Game:
    def __init__(self):
        self.grid=Grid()
        self.blocks =[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.curent_block=self.get_random_block()
        self.next_block=self.get_random_block()
        self.game_over=False
        self.score=0
        self.rotate_sound=pygame.mixer.Sound("Sound/rotate.ogg")
        self.clear_sound=pygame.mixer.Sound("Sound/clear.ogg")
        pygame.mixer.music.load("Sound/music.ogg")
        pygame.mixer.music.play(-1)
    def update_scores(self,lines_cleared,move_down_points):
        if lines_cleared==1:
            self.score+=100
        elif lines_cleared==2:
            self.score+=300
        elif lines_cleared==3:
            self.score+=500
        self.score+=move_down_points

    def get_random_block(self):
        if len(self.blocks)==0:
            self.blocks =[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        block=random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    def move_left(self):
        self.curent_block.move(0,-1)
        if self.block_inside()==False or self.block_fits()==False:
            self.curent_block.move(0,1)
    def move_right(self):
        self.curent_block.move(0,1)
        if self.block_inside()==False or self.block_fits()==False:
            self.curent_block.move(0,-1)
    def move_down(self):
        self.curent_block.move(1,0)
        if self.block_inside()==False or self.block_fits()==False:
            self.curent_block.move(-1,0)
            self.lock_block()
    def lock_block(self):
        tiles=self.curent_block.get_cell_position()
        for position in tiles:
            self.grid.grid[position.row][position.column] =self.curent_block.id
        self.curent_block=self.next_block
        self.next_block=self.get_random_block()
        row_cleared=self.grid.clear_full_row()
        if row_cleared > 0:
            self.clear_sound.play()
            self.update_scores(row_cleared,0)
        if self.block_fits()==False:
            self.game_over=True
    def reset(self):
        self.grid.reset()
        self.blocks =[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.curent_block=self.get_random_block()
        self.next_block=self.get_random_block()
        self.score=0

    def rotate(self):
        self.curent_block.rotate()
        if self.block_inside()==False or self.block_fits()==False:
            self.curent_block.undo_rotation()
        else:
            self.rotate_sound.play()
    def block_inside(self):
        tiles=self.curent_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row , tile.column) == False:
                return False
        return True
    def block_fits(self):
        tiles=self.curent_block.get_cell_position()
        for tile in tiles:
            if self.grid.is_empty(tile.row,tile.column)==False:
                return False
        return True
    def draw(self,screen):
        self.grid.draw(screen)
        self.curent_block.draw(screen,11,11)
        if self.next_block.id==3:
            self.next_block.draw(screen,255,290)
        elif self.next_block.id==4:
            self.next_block.draw(screen,255,280)
        else:
            self.next_block.draw(screen,270,270)
