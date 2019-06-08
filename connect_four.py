import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    #  Check Horizontal Locations
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3]:
                return True

    #  Check for Vertical Locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c]:
                return True

    #  Check for Positively sloped Diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3]:
                return True


    #  Check for Negative sloped Diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3]:
                return True

def  draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):    
                if board[r][c] == 1:
                    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
    pygame.display.update()            

board = create_board()
game_over = False
turn = 0
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2  - 5)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

#  Displaying it
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

pygame.init()
myfont = pygame.font.SysFont('monospace', 75)
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEMOTION:
            posx = event.pos[0]
            pygame.draw.rect(screen, BLACK, (0,0,width, height))
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            elif turn == 1:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            #  Ask for player 1 Input
            if turn == 0:
                turn = 1
                posx = event.pos[0]
                col = math.floor(posx/SQUARESIZE)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
                        pygame.display.update()
                        label = myfont.render("Player 1 WINS!", 1, RED)
                        screen.blit(label,(40,10))
                        game_over = True

            #  Ask for player 2 Input
            else:
                turn = 0
                posx = event.pos[0]
                col = math.floor(posx/SQUARESIZE)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
                        pygame.display.update()
                        label = myfont.render("Player 2 WINS!", 2, YELLOW)
                        screen.blit(label,(40,10))
                        game_over = True
    
       
    print_board(board)
    draw_board(board)
    if game_over:
        pygame.time.wait(3000)

