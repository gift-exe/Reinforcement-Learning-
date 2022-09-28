from tkinter.tix import ROW
import pygame

WIN_HEIGHT = 400
WIN_WIDTH = 400
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
    
    def get_color(self):
        if self.state:
            color = OBJECTIVE
        else:
            color = BLACK
        return color

    def get_pos(self):
        return (self.row, self.column)
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.spot_width, self.spot_width))
        
def make_grid(rows, columns, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(columns):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid

def draw_grid(win, rows, columns, width, height):
    r_gap = width // rows
    c_gap = height // columns
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

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    while True:
        grid = make_grid(ROWS, COLUMNS, WIN_WIDTH)
        draw(SCREEN, grid, ROWS, COLUMNS, WIN_WIDTH, WIN_HEIGHT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()

main()