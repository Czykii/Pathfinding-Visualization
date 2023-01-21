#Projekt napisany z pomocą tutorialu: https://www.youtube.com/watch?v=JtiK0DOeI4A&ab_channel=TechWithTim

import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Square:
    def __init__(self, row, col, width, number_of_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.number_of_rows = number_of_rows
    
    def get_pos(self):
        return self.row, self.col

#Sprawdzamy stan klocka    
    def is_open(self):
        return self.color == GREEN

    def is_closed(self):
        return self.color == RED

    def is_blocked(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_goal(self):
        return self.color == TURQUOISE

#Zmiana stanu klocka    
    def reset(self):
        self.color = WHITE

    def make_closed_star(self):
        self.color = RED
    
    def make_open_star(self):
        self.color = GREEN

    def make_closed_dijkstra(self):
        self.color = BLUE
    
    def make_open_dijkstra(self):
        self.color = YELLOW

    def make_blocked(self):
        self.color = BLACK
    
    def make_start(self):
        self.color = ORANGE
    
    def make_goal(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbour(self, grid):
        self.neighbours = []
        
        #Sprawdzam, czy kratka na gorze jest blokadą
        if self.row > 0 and not grid[self.row - 1][self.col].is_blocked():
            self.neighbours.append(grid[self.row - 1][self.col])
        
        #Sprawdzam, czy kratka na dole jest blokadą
        if self.row < self.number_of_rows - 1 and not grid[self.row + 1][self.col].is_blocked():
            self.neighbours.append(grid[self.row + 1][self.col])
        
        #Sprawdzam, czy kratka po lewej jest blokadą
        if self.col > 0 and not grid[self.row][self.col - 1].is_blocked():
            self.neighbours.append(grid[self.row][self.col - 1])
        
        #Sprawdzam, czy kratka po prawej jest blokadą
        if self.col < self.number_of_rows - 1 and not grid[self.row][self.col + 1].is_blocked():
            self.neighbours.append(grid[self.row][self.col + 1])

    def __lt__(self, other):
        return False

#Ustalenie ilości kratek
def create_grid(rows, width):
    grid = []

    for i in range(rows):
       grid.append([])
       for j in range(rows):
            square = Square(i, j, width // rows, rows)
            grid[i].append(square)
    
    return grid

#Namalowanie lini miedzy kratkami
def paint_grid(window, rows, width):

    for i in range(rows):
        pygame.draw.line(window, GREY, (0, i * (width // rows)), (width, i * (width // rows)))
    for j in range(rows):
        pygame.draw.line(window, GREY, (j * (width // rows), 0), (j * (width // rows), width))

#Pokolorowanie wszystkich kratek
def draw(window, grid, rows, width):
    window.fill(WHITE)

    for row in grid:
        for square in row:
            square.draw(window)
    
    paint_grid(window, rows, width)
    pygame.display.update()

#Zaznaczenie najkrótszej znalezionej ścieżki
def construct_path(came_from, temp, start, goal, draw):
    while temp in came_from:
        temp = came_from[temp]
        temp.make_path()
        draw()
    start.make_start()
    goal.make_goal()

#Odczytanie klinku myszki
def get_mouse_position(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col