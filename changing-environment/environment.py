from multiprocessing import current_process
import pygame
import random
import time

WIN_HEIGHT = 196
WIN_WIDTH = 392
ROWS = 7
COLUMNS = 14

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

AGENT = (0, 255, 0)
OBJECTIVE = (255, 0, 0)

global_start = time.time()
start = time.time()

class Spot():
    def __init__(self, row, column, width, total_rows):
        self.row = row
        self.column = column
        self.x = width * row
        self.y = width * column
        self.state = False
        self.spot_width = width
        self.total_rows = total_rows
        self.color = self.get_color()
    
    def get_color(self):
        if self.state:
            color = OBJECTIVE
        else:
            color = BLACK
        return color

    def get_pos(self):
        return (self.row, self.column)
        
    def draw(self, win):
        pygame.draw.rect(win, self.get_color(), (self.x/2, self.y/2, self.spot_width/2, self.spot_width/2))
    
class Agent():
    def __init__(self, column, row, width):
        self.row = row
        self.column = column
        self.agent_width = width
        self.color = AGENT
    def get_coordinates(self):
        x = self.agent_width * self.row
        y = self.agent_width * self.column
        return x, y

    def get_pos(self):
        return (self.row, self.column)
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.get_coordinates()[0], self.get_coordinates()[1], self.agent_width, self.agent_width))
    

def make_grid(rows, columns, width):
    grid = []
    gap = width // rows
    for i in range(columns):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid

def draw_grid(win, rows, columns, width, height):
    r_gap =  height // rows
    c_gap = width // columns
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * r_gap), (width, i * r_gap))
        for j in range(columns):
            pygame.draw.line(win, GREY, (j* c_gap, 0), (j * c_gap, height))

def draw(win, grid, rows, columns, width, height):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, columns, width, height)
    pygame.display.update()
    return grid

#to create a function that randomly assign states to different spot objects in the grid
def random_spot_chooser(grid):
    x = random.randint(0, len(grid)-1)
    y = random.randint(0, len(grid[x])-1)

    return x, y
    
def main():
    global SCREEN, CLOCK, start
    pygame.init()
    fps=30
    fpsclock=pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    grid = make_grid(ROWS, COLUMNS, WIN_WIDTH)
    agent = Agent(0, 0, 28)
    while True:
        if time.time() - start >= 1:
            start = time.time()
            x, y =random_spot_chooser(grid)
            grid[x][y].state = True
        grid = draw(SCREEN, grid, ROWS, COLUMNS, WIN_WIDTH, WIN_HEIGHT)
        agent.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if agent.get_pos()[0] != 0:
                        agent.row = agent.row - 1
                if event.key == pygame.K_w:
                    if agent.get_pos()[1] != 0:
                        agent.column = agent.column -1
                if event.key == pygame.K_s:
                    if agent.get_pos()[1] != 6:
                        agent.column = agent.column + 1
                if event.key == pygame.K_d:
                    if agent.get_pos()[0] != 13:
                        agent.row = agent.row + 1
        current_pos = agent.get_pos()
        if grid[current_pos[0]][current_pos[1]].state == True:
            grid[current_pos[0]][current_pos[1]].state = False

        
        pygame.display.update()
        fpsclock.tick(fps)

main()
