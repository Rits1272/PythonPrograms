import pygame
from operator import add
pygame.init()

WIDTH, HEIGHT = 600,600
white = (255,255,255)
black = (0,0,0)
green = (0,0,255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MAZE SOLVER")

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows # // returns the floor division
    x = 0
    y = 0

    for _ in range(rows):
        x += sizeBtwn
        y += sizeBtwn
        pygame.draw.line(surface,black,(x,0),(x,w),2)
        pygame.draw.line(surface,black,(0,y),(w,y),2)


def printSolution(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")

def isSafe(maze,x,y):
    if x >= 0 and x < 5 and y >= 0 and y < 5 and maze[x][y] == 1:
        return True
    return False

def solveMaze(maze):
    sol = [[0 for i in range(5)] for j in range(5)]
    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("No solution")
    printSolution(sol)
    return sol

def solveMazeUtil(maze,x,y,sol):
    if x == 4 and y == 4:
        sol[x][y] = 1
        return True
    if isSafe(maze,x,y) == True:
        sol[x][y] = 1

        if solveMazeUtil(maze,x+1,y,sol) == True:
            return True
        if solveMazeUtil(maze,x+1,y+1,sol) == True:
            return True
        if solveMazeUtil(maze,x,y+1,sol) == True:
            return True
        if solveMazeUtil(maze,x-1,y+1,sol) == True:
            return True
        if solveMazeUtil(maze,x-1,y,sol) == True:
            return True
        if solveMazeUtil(maze,x-1,y-1,sol) == True:
            return True
        if solveMazeUtil(maze,x,y-1,sol) == True:
            return True
        if solveMazeUtil(maze,x+1,y-1,sol) == True:
            return True
        sol[x][y] = 0
        return False



def main_loop():
    maze_ = [[1 for i in range(5)] for i in range(5)]
    run = True
    screen.fill(white)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x,y =  int(pos[0]/120),int(pos[1]/120)
                maze_[y][x] = 0
                pygame.draw.rect(screen, (80,80,80), (x*120, y*120, 120, 120))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("Enter is pressed")
                    print(maze_)
                    res = solveMaze(maze_)
                    count = 0
                    if res != False:
                        for i in range(5):
                            for j in range(5):
                                if res[j][i] == 1:
                                    count += 1
                                    pygame.draw.rect(screen, (0,20+count*25,0), (i*120,j*120,120,120))


        drawGrid(WIDTH,5,screen)
        pygame.display.update()





main_loop()
exit()
