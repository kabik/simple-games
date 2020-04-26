import pygame
from pygame.locals import *
import random

INDEX_DIFFS = [
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1),
]


class Lifegame:
    def __init__(self, width, height, density):
        self.width = width
        self.height = height
        self.cells = [[False] * width for _ in range(height)]

        for y in range(height):
            for x in range(width):
                if random.random() < density:
                    self.cells[y][x] = True


    def update(self):
        neighbor_cnt = [[0] * self.width for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                for ind_diff in INDEX_DIFFS:
                    neighbor_x = x + ind_diff[1]
                    neighbor_y = y + ind_diff[0]
                    if 0 <= neighbor_x < self.width and 0 <= neighbor_y < self.height:
                        neighbor_cnt[neighbor_y][neighbor_x] += self.cells[y][x]
        for y in range(self.height):
            for x in range(self.width):
                self.cells[y][x] = \
                    neighbor_cnt[y][x] == 3 or \
                    (self.cells[y][x] and neighbor_cnt[y][x] == 2)


def draw(screen, lifegame, size):
    green = (0, 255, 0)
    for y in range(lifegame.height):
        for x in range(lifegame.width):
            if lifegame.cells[y][x]:
                pygame.draw.rect(screen, green, (x * size, y * size, size, size))

def main():
    WIDTH   = 1200
    HEIGHT  = 600
    CELL_SIZE = 10
    DENSITY = 0.3
    lifegame = Lifegame(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE, DENSITY)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Lifegame")
    background_color = (50,50,50)

    running = True
    while(running):
        lifegame.update()
        screen.fill(background_color)
        draw(screen, lifegame, CELL_SIZE)
        pygame.display.update()
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    pygame.quit()


if __name__ == "__main__":
    main()
