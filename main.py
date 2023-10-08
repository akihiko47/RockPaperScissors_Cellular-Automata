import pygame
import sys
import copy
import random

pygame.init()


"""settings"""
matrix_size = 100
cube_size = 10
rand = True
rand_cof = 1
near_win_count = 2


"""display part"""
display_width = (matrix_size + 2) * cube_size
display_height = (matrix_size + 2) * cube_size

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Rock Paper Scissors")

"""colors"""
all_colors = [[(16, 19, 35), (214, 212, 203), (113, 25, 25)],
              [(255, 238, 187), (255, 102, 204), (119, 51, 102)],
              [(37, 43, 44), (86, 174, 196), (225, 240, 240)],
              [(254, 254, 254), (237, 50, 55), (55, 52, 53)],
              [(0, 108, 0), (255, 117, 16), (255, 245, 247)],
              [(241, 183, 139), (82, 28, 20), (149, 66, 30)]]

colors = [(16, 19, 35), (214, 212, 203), (113, 25, 25)]

"""fps part"""
clock = pygame.time.Clock()
FPS = 30


def draw_matrix(mat):
    display.fill((0, 0, 0))
    for y in range(len(mat)):
        for x in range(len(mat)):
            sqr = mat[y][x]
            if sqr != 8 and sqr != 0:
                pygame.draw.rect(display, colors[sqr-1], (y * cube_size, x * cube_size, cube_size, cube_size))


def grow(mat):
    new_mat = copy.deepcopy(mat)
    for y in range(len(mat)-1):
        for x in range(len(mat)-1):
            sqr = mat[y][x]

            near = [mat[y-1][x], mat[y-1][x+1], mat[y][x+1],
                    mat[y+1][x+1], mat[y+1][x], mat[y+1][x-1],
                    mat[y][x-1], mat[y-1][x-1]]

            if sqr == len(colors):
                beat = 1
            else:
                beat = sqr + 1

            cof = near_win_count
            if rand:
                cof += random.randint(0, rand_cof)

            if sqr == 0:
                for i in range(len(colors)):
                    if near.count(i + 1) > cof:
                        new_mat[y][x] = i + 1
            elif near.count(beat) > cof:
                new_mat[y][x] = beat

    return new_mat


def create_matrix():
    matrix = [[8] * (matrix_size + 2)]
    matrix += [[8] + ([0] * matrix_size) + [8] for _ in range(matrix_size)]
    matrix += [[8] * (matrix_size + 2)]
    return matrix


def game():
    global colors, near_win_count, FPS
    matrix = create_matrix()

    """placing faze"""
    started = False
    mode = 1
    color_mode = 0

    in_game = True
    while in_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    color_mode += 1
                elif event.key == pygame.K_LEFT:
                    color_mode -= 1
                elif event.key == pygame.K_EQUALS:
                    FPS += 5
                elif event.key == pygame.K_MINUS:
                    if FPS > 5:
                        FPS -= 5
                elif event.key == pygame.K_ESCAPE:
                    matrix = create_matrix()
                    started = False
                elif event.key == pygame.K_UP:
                    if near_win_count > 0:
                        near_win_count -= 1
                elif event.key == pygame.K_DOWN:
                    if near_win_count < 4:
                        near_win_count += 1
        """user inputs"""
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)

        """drawing"""
        if click[0]:
            m_x, m_y = mouse[0] // cube_size, mouse[1] // cube_size
            if matrix[m_x][m_y] != 8:
                matrix[m_x][m_y] = mode

        """colors"""
        colors = all_colors[color_mode % len(all_colors)]

        """end of start faze and mode"""
        if keys[pygame.K_SPACE]:
            started = True
        if keys[pygame.K_1]:
            mode = 1
        if keys[pygame.K_2]:
            mode = 2
        if keys[pygame.K_3]:
            mode = 3

        """grow matrix"""
        if started:
            matrix = grow(matrix)
            clock.tick(FPS)

        """display update"""
        draw_matrix(matrix)
        pygame.display.update()


if __name__ == '__main__':
    game()
