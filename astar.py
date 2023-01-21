#Projekt napisany z pomocą tutorialu: https://www.youtube.com/watch?v=JtiK0DOeI4A&ab_channel=TechWithTim

import pygame
from queue import PriorityQueue
from square import construct_path

def h(now, goal):
    x1, y1 = now
    x2, y2 = goal
    
    distance = abs(x1 - x2) + abs(y1 - y2) 
    return distance

def a_star(draw, grid, start, goal):
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
                    neighbour.make_open_star()

        draw()

        if temp != start:
           temp.make_closed_star()

    return False