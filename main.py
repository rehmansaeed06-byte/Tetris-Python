import pygame,sys
from game import Game
from colors import Colors
pygame.init()
title_font= pygame.font.Font(None,40)
score_surface=title_font.render("Score",True,Colors.white)
next_surface=title_font.render("Next",True,Colors.white)
game_over_surface=title_font.render(" Game Over",True,Colors.white)
score_rect=pygame.Rect(320,55,170,60)
next_rect=pygame.Rect(320,215,170,180)


screen=pygame.display.set_mode((500,620))
pygame.display.set_caption("Tetris Python")
clock=pygame.time.Clock()
game=Game()
Game_update=pygame.USEREVENT
pygame.time.set_timer(Game_update,250)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if game.game_over==True:
                game.game_over=False
                game.reset()
            if event.key==pygame.K_LEFT and game.game_over==False:
                game.move_left()
            if event.key==pygame.K_RIGHT and game.game_over==False:
                game.move_right()
            if event.key==pygame.K_DOWN and game.game_over==False:
                game.move_down()
            if event.key==pygame.K_UP and game.game_over==False:
                game.rotate()
        if event.type==Game_update and game.game_over==False:
            game.move_down()
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365,20,50,50))
    screen.blit(next_surface, (375,180,50,50))
    if game.game_over==True:
       screen.blit(game_over_surface, (320,450,50,50))
    game.draw(screen)
    pygame.draw.rect(screen,Colors.light_blue,score_rect,0,10)
    pygame.draw.rect(screen,Colors.light_blue,next_rect,0,10)
    pygame.display.update()
    clock.tick(60)
