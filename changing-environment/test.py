import pygame
import random
import time
import numpy as np

WIN_HEIGHT = 196
WIN_WIDTH = 392
ROWS = 7
COLUMNS = 14

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

AGENT = (0, 255, 0)
OBJECTIVE = (255, 0, 0)

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
    
    def __repr__(self):
        return f'position: {(self.row, self.column)}, \n state: {self.state}\n'
    
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
    def __init__(self, column, row, width, score):
        self.row = row
        self.column = column
        self.agent_width = width
        self.score = score
        self.color = AGENT
        self.actions = ['up', 'down', 'left', 'right']
        self.exp_rate = 0.3
    
    def get_coordinates(self):
        x = self.agent_width * self.row
        y = self.agent_width * self.column
        return x, y

    def get_pos(self):
        return (self.row, self.column)
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.get_coordinates()[0], self.get_coordinates()[1], self.agent_width, self.agent_width))
    
    def choose_action(self):
        if np.random.uniform(0, 1) <= self.exp_rate:
            action = random.choice(self.actions)
        else:
            for a in self.actions:
                pass
        return action
    

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
    new_grid = []
    for row in grid:
        for spot in row:
            if spot.state == False:
                new_grid.append(spot)
            
    if len(new_grid)<=1:
        return None

    spot = random.choice(new_grid)

    return spot

def event_listerners():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def agent_listerner(agent):
    action = agent.choose_action()
    if action == 'left':
        if agent.get_pos()[0] != 0:
            agent.row = agent.row - 1
    if action == 'up':
        if agent.get_pos()[1] != 0:
            agent.column = agent.column -1
    if action == 'down':
        if agent.get_pos()[1] != 6:
            agent.column = agent.column + 1
    if action == 'right':
        if agent.get_pos()[0] != 13:
            agent.row = agent.row + 1

def agent_object_picker(agent, grid):
    current_pos = agent.get_pos()
    if grid[current_pos[0]][current_pos[1]].state == True:
        agent.score = agent.score + 1
        grid[current_pos[0]][current_pos[1]].state = False

def main():
    global SCREEN
    start = time.time()
    time_limit = time.time()
    pygame.init()
    fps=30
    fpsclock=pygame.time.Clock()
    SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    grid = make_grid(ROWS, COLUMNS, WIN_WIDTH)
    agent = Agent(0, 0, 28, 0)
    while True:
        # if time.time() - time_limit >= 120:
        #     print('time limit reached')
        #     print(f'score: {agent.score}')
        #     break

        # if time.time() - start >= 0.4:
        #     start = time.time()
        #     chosen_spot = random_spot_chooser(grid)
        #     if chosen_spot == None:
        #         print('Mission Failed!! All cells have been occupied')
        #         print(f'score: {agent.score}')
        #         break
        #     grid[chosen_spot.row][chosen_spot.column].state = True
        
        grid = draw(SCREEN, grid, ROWS, COLUMNS, WIN_WIDTH, WIN_HEIGHT)
        
        agent.draw(SCREEN)
        
        if time.time() - start >= 0.3:
            start = time.time()
            agent_listerner(agent)

        event_listerners()        
        
        agent_object_picker(agent, grid)
        
        pygame.display.update()
        fpsclock.tick(fps)

main()
