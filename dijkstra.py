#Projekt napisany z pomocą tutorialu: https://www.youtube.com/watch?v=JtiK0DOeI4A&ab_channel=TechWithTim

import pygame
from queue import PriorityQueue
from square import construct_path

def dijkstra(draw, grid, start, goal):
    open_set = PriorityQueue()
    came_from = {}
    visited = []
    distance = {square: float("inf") for row in grid for square in row}
    
    distance[start] = 0
    open_set.put((0, start))

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
        temp = open_set.get()[1]
        visited.append(temp)

        if temp == goal:
            construct_path(came_from, goal, start, goal, draw)
            return True

        for neighbour in temp.neighbours:
            if distance[neighbour] > distance[temp] + 1:
                distance[neighbour] = distance[temp] + 1
                came_from[neighbour] = temp
                open_set.put((distance[neighbour], neighbour))

                neighbour.make_open_dijkstra()
        
        draw()

        if temp != start:
            temp.make_closed_dijkstra()
    
    return False
