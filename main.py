#Program napisany z pomocą tutorialu: https://www.youtube.com/watch?v=JtiK0DOeI4A&ab_channel=TechWithTim

import pygame
import math
from queue import PriorityQueue

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

def h(now, goal):
    x1, y1 = now
    x2, y2 = goal
    
    distance = abs(x1 - x2) + abs(y1 - y2) 
    return distance

def algorithm(draw, grid, start, goal):
    open_set = PriorityQueue()
    came_from = {}
    steps = 0
    
    f_score = {square: 100 for row in grid for square in row}
    f_score[start] = h(start.get_pos(), goal.get_pos())
    
    g_score = {square: 100 for row in grid for square in row}
    g_score[start] = 0

    open_set.put((f_score[start], steps, start))
    open_hash = {start}

    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        temp = open_set.get()[2]
        open_hash.remove(temp)

        if temp == goal:
            construct_path(came_from, goal, start, goal, draw)
            return True

        for neighbour in temp.neighbours:
            temp_g_score = g_score[temp] + 1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = temp
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), goal.get_pos())

                if neighbour not in open_hash:
                    steps += 1
                    open_hash.add(neighbour)
                    open_set.put((f_score[neighbour], steps, neighbour))
                    neighbour.make_open()

        draw()

        if temp != start:
           temp.make_closed()

    return False

def construct_path(came_from, temp, start, goal, draw):
    while temp in came_from:
        temp = came_from[temp]
        temp.make_path()
        draw()
    start.make_start()
    goal.make_goal()    

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

    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN

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

#Odczytanie klinku myszki
def get_mouse_position(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def main():
    width = 900
    window = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Wizualizacja algorytmu A*")
    
    ROWS = 50
    grid = create_grid(ROWS, width)

    start = None
    goal = None
    run = True

    while run:
        draw(window, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:       #Reakcja na LPM
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_position(pos, ROWS, width)
                square = grid[row][col]

                if not start and square != goal:
                    start = square
                    start.make_start()
                elif not goal and square != start:
                    goal = square
                    goal.make_goal()
                elif square != start and square != goal:
                    square.make_blocked()
            
            elif pygame.mouse.get_pressed()[2]:     #Reakcja na PPM
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_position(pos, ROWS, width)
                square = grid[row][col]
                square.reset()

                if square == start:
                    start = None
                if square == goal:
                    goal = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and goal:   #Reakcja na spacje
                    for row in grid:
                        for square in row:
                            square.update_neighbour(grid)
                    
                    algorithm(lambda: draw(window, grid, ROWS, width), grid, start, goal)
            
                if event.key == pygame.K_c:     #Reakcja na "c"
                    start = None
                    goal = None
                    grid = create_grid(ROWS, width)
    
    pygame.quit()

main()