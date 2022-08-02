import random
import unittest
from visualizer import DisplayAlgorithm


def test_sorting_algorithms(func_num):

    class TestDisplayAlgorithm(unittest.TestCase):

        def __init__(self, methodName):
            super().__init__(methodName)
            self.arr1 = [23, 16, 501, 705, 999, 0, 1, 2, 4, 1, 5, 76]
            self.arr2 = random.sample(range(1, 999), 50)

        def iterate(self, gen):
            iterator = iter(gen)
            try:
                while True:
                    next(iterator)
            except StopIteration:
                pass
            finally:
                del iterator

        def test_algorithm(self):
            disp_alg = DisplayAlgorithm(800, 600, self.arr1)
            print(f"Testing {disp_alg.sorting_types[func_num][0]} ...")

            selection_sort_gen = disp_alg.sorting_types[func_num][1](disp_alg)
            self.iterate(selection_sort_gen)

            self.assertEqual(disp_alg.arr, sorted(self.arr1))

            disp_alg.arr_disp_setter(self.arr2)
            selection_sort_gen = disp_alg.sorting_types[func_num][1](disp_alg)
            self.iterate(selection_sort_gen)

            self.assertEqual(disp_alg.arr, sorted(self.arr2))

    return TestDisplayAlgorithm


def run_all_tests():
    suites_list = []
    loader = unittest.TestLoader()

    for i in range(1, 10):
        suite = loader.loadTestsFromTestCase(test_sorting_algorithms(i))
        suites_list.append(suite)

    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite(suites_list))


if __name__ == '__main__':
    run_all_tests()
