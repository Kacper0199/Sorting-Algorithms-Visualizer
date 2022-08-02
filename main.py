import random
import pygame
from visualizer import DisplayAlgorithm


def main():
    min_val, max_val, n_arr = 1, 500, 50
    arr = random.sample(range(min_val, max_val), n_arr)
    fps = pygame.time.Clock()
    fps_val = 30
    execute, start_sorting = True, False
    disp = DisplayAlgorithm(800, 600, arr)

    algorithm, algorithm_name = disp.sorting_types[1][1], disp.sorting_types[1][0]
    algorithm_gen = None

    while execute:
        fps.tick(fps_val)

        if start_sorting:
            try:
                next(iter(algorithm_gen))
            except StopIteration:
                start_sorting = False
        else:
            disp.show_all(algorithm_name)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                execute = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_SPACE:
                arr = random.sample(range(min_val, max_val), n_arr)
                disp.arr_disp_setter(arr)
                start_sorting = False
            if event.key == pygame.K_RIGHT and not start_sorting and n_arr < 300:
                n_arr += 10
                arr = random.sample(range(min_val, max_val), n_arr)
                disp.arr_disp_setter(arr)
                start_sorting = False
            if event.key == pygame.K_LEFT and not start_sorting and n_arr > 10:
                n_arr -= 10
                arr = random.sample(range(min_val, max_val), n_arr)
                disp.arr_disp_setter(arr)
                start_sorting = False
            elif event.key == pygame.K_RETURN and start_sorting == False:
                start_sorting = True
                algorithm_gen = algorithm(disp)
            elif event.key == pygame.K_PAGEUP and not start_sorting:
                fps_val += 20
                fps.tick(fps_val)
            elif event.key == pygame.K_PAGEDOWN and not start_sorting:
                fps.tick(5)
            elif event.key == pygame.K_1 and not start_sorting:
                algorithm, algorithm_name = disp.sorting_types[1][1], disp.sorting_types[1][0]
            elif event.key == pygame.K_2 and not start_sorting:
                algorithm, algorithm_name = disp.sorting_types[2][1], disp.sorting_types[2][0]
            elif event.key == pygame.K_3 and not start_sorting:
                algorithm, algorithm_name = disp.sorting_types[3][1], disp.sorting_types[3][0]
            elif event.key == pygame.K_4 and not start_sorting:
                algorithm, algorithm_name = disp.sorting_types[4][1], disp.sorting_types[4][0]
            elif event.key == pygame.K_5 and not start_sorting:
                algorithm, algorithm_name = disp.sorting_types[5][1], disp.sorting_types[5][0]
            elif event.key == pygame.K_6 and not start_sorting:
                algorithm, algorithm_name = disp.sorting_types[6][1], disp.sorting_types[6][0]
            elif event.key == pygame.K_7 and not start_sorting:
                algorithm, algorithm_name = disp.sorting_types[7][1], disp.sorting_types[7][0]
            elif event.key == pygame.K_8 and not start_sorting:
                algorithm, algorithm_name = disp.sorting_types[8][1], disp.sorting_types[8][0]
            elif event.key == pygame.K_9 and not start_sorting:
                algorithm, algorithm_name = disp.sorting_types[9][1], disp.sorting_types[9][0]

    pygame.quit()


if __name__ == '__main__':
    main()
