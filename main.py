import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sorting Algorithm Visualizer")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def generate_array(n, min_val, max_val):
    array = []
    for _ in range(n):
        array.append(random.randint(min_val, max_val))
    return array

def draw_array(array, screen, width, height, spacing):
    start_x = 50
    start_y = 50
    rect_width = (width - 2 * start_x) // len(array)
    rect_height = height - 2 * start_y

    for i in range(len(array)):
        pygame.draw.rect(screen, white, (start_x + i * (rect_width + spacing), start_y, rect_width, array[i] * rect_height // max(array)))

def bubble_sort(array, screen, width, height, spacing):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_array(array, screen, width, height, spacing)
                pygame.display.update()
                pygame.time.delay(50)

def main():
    array_size = 50
    min_val = 1
    max_val = 100

    array = generate_array(array_size, min_val, max_val)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(black)
        draw_array(array, screen, screen_width, screen_height, 10)
        pygame.display.update()

        bubble_sort(array, screen, screen_width, screen_height, 10)

    pygame.quit()

if __name__ == "__main__":
    main()