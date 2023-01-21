#Projekt napisany z pomocą tutorialu: https://www.youtube.com/watch?v=JtiK0DOeI4A&ab_channel=TechWithTim

import pygame
from square import draw, create_grid, get_mouse_position
from astar import a_star
from dijkstra import dijkstra


def main():
    width = 800
    window = pygame.display.set_mode((width, width))
    pygame.display.set_caption("Wizualizacja algorytmu Dijkstry i A*")
    
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
                if event.key == pygame.K_a and start and goal:   #Reakcja na "a"
                    for row in grid:
                        for square in row:
                            square.update_neighbour(grid)
                    
                    a_star(lambda: draw(window, grid, ROWS, width), grid, start, goal)

                if event.key == pygame.K_d and start and goal:   #Reakcja na "d"
                    for row in grid:
                        for square in row:
                            square.update_neighbour(grid)

                    dijkstra(lambda: draw(window, grid, ROWS, width), grid, start, goal)
            
                if event.key == pygame.K_c:     #Reakcja na "c"
                    start = None
                    goal = None
                    grid = create_grid(ROWS, width)
    
    pygame.quit()

main()