import pygame
import algorithms

pygame.init()


class DisplayProperties(object):
    WHITE = 255, 255, 255
    TITLE_CLR = 255, 0, 191
    BACKGROUND_COLOR = 115, 0, 230
    HORIZONTAL_PADDING = 50
    VERTICAL_PADDING = 50
    MENU_BLOCK_WIDTH = 150
    MENU_VERTICAL_PADDING = 150
    MENU_HORIZONTAL_PADDING = 20
    GRADIENTS = [(0, 132, 255), (0, 174, 255), (58, 209, 254)]
    TITLE_FONT = pygame.font.SysFont("georgia", 30, bold=True, italic=True)
    MENU_FONT = pygame.font.SysFont("helvetica", 20, bold=True, italic=False)

    def __init__(self, width, height, arr):
        self.height = height
        self.width = width
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Visualizer")
        self.arr_disp_setter(arr)

    def arr_disp_setter(self, arr):
        self.arr = arr
        self.n_arr = len(arr)
        self.max_val = max(arr)
        self.min_val = min(arr)
        self.bar_width = (self.width - self.HORIZONTAL_PADDING -
                          self.MENU_BLOCK_WIDTH + self.MENU_HORIZONTAL_PADDING/2)/self.n_arr
        self.unit_bar_height = (
            self.height - self.VERTICAL_PADDING)//(self.max_val - self.min_val)
        self.horizontal_start = self.HORIZONTAL_PADDING//2


class DisplayAlgorithm(DisplayProperties):

    def __init__(self, width, height, arr):
        super().__init__(width, height, arr)
        self.sorting_types = {
            1: ("Selection sort", algorithms.selection_sort),
            2: ("Insertion sort", algorithms.insertion_sort),
            3: ("Bubble sort", algorithms.bubble_sort),
            4: ("Cocktail sort", algorithms.cocktail_sort),
            5: ("Shell sort", algorithms.shell_sort),
            6: ("Quick sort", algorithms.quick_sort),
            7: ("Merge sort", algorithms.merge_sort),
            8: ("Heap sort", algorithms.heap_sort),
            9: ("Radix sort", algorithms.radix_sort)}

    def show_arr(self, clear_arr=False):
        if clear_arr:
            clear = (self.HORIZONTAL_PADDING//2,
                     self.VERTICAL_PADDING,
                     self.width-self.MENU_BLOCK_WIDTH-self.MENU_HORIZONTAL_PADDING-10,
                     self.height)
            pygame.draw.rect(self.window, self.BACKGROUND_COLOR, clear)

        for i, val in enumerate(self.arr):
            x_coord = self.horizontal_start + i*self.bar_width
            y_coord = self.height - val*self.unit_bar_height
            color = self.GRADIENTS[i % 3]
            pygame.draw.rect(self.window, color,
                             (x_coord, y_coord, self.bar_width, self.height))

        if clear_arr:
            pygame.display.update()

    def show_menu(self):
        y_coord = self.MENU_VERTICAL_PADDING
        for i, type in self.sorting_types.items():
            menu_list = self.MENU_FONT.render(
                f"{i}. {type[0]}", 1, self.WHITE)
            self.window.blit(menu_list,
                             (self.width - self.MENU_BLOCK_WIDTH - self.MENU_HORIZONTAL_PADDING//2 + 10, y_coord))
            y_coord += menu_list.get_height()

    def show_title(self, algorithm_name):
        title = self.TITLE_FONT.render(f"{algorithm_name}", 1, self.TITLE_CLR)
        self.window.blit(title,
                         (self.bar_width*self.n_arr//2, self.VERTICAL_PADDING//4))

    def show_all(self, algorithm_name="", clear_arr=False):
        self.window.fill(self.BACKGROUND_COLOR)
        self.show_menu()
        self.show_arr(clear_arr)
        self.show_title(algorithm_name)
        pygame.display.update()
