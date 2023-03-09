import numpy as np
import pygame
import time

WIDTH = 800
HEIGHT = 600
COLOR_BACKGROUND = (45, 20, 90)
COLOR_GRID = (80, 20, 90)
LIVE = (150, 155, 105)
SHAPE = 60, 80
GRID_CELL_SIZE = 20

def update(screen, cells, size, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BACKGROUND if cells[row, col] == 0  else LIVE
        
        if cells[row, col] == 1:
            if 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = LIVE
            else:
                if with_progress:
                    color = COLOR_BACKGROUND
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = LIVE
        
        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size -1))

    return updated_cells

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    cells = np.zeros(SHAPE)
    screen.fill(COLOR_GRID)
    update(screen, cells, GRID_CELL_SIZE)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, GRID_CELL_SIZE)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // GRID_CELL_SIZE, pos[0] // GRID_CELL_SIZE] = 1
                update(screen, cells, GRID_CELL_SIZE)
                pygame.display.update()

        screen.fill(COLOR_GRID)
        if running:
            cells = update(screen, cells, GRID_CELL_SIZE, with_progress=True)
            pygame.display.update()

        time.sleep(0.2)

if __name__ == '__main__':
    main()