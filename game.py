from grid import Grid
from blocks import *
import random
class Game:
    def __init__(self):
        self.grid=Grid()
        self.blocks =[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.curent_block=self.get_random_block()
        self.next_block=self.get_random_block()
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
        self.grid.clear_full_row()
    def rotate(self):
        self.curent_block.rotate()
        if self.block_inside()==False or self.block_fits()==False:
            self.curent_block.undo_rotation()
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
        self.curent_block.draw(screen)

