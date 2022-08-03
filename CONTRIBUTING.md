# Contribution

This is an open source project. Feel free to add new algorithm implementations or issues related to the app. There are many other sorting algorithms that are waiting for you!

## Make a pull request

* Fork and clone repo with `git clone https://github.com/<YOUR-USERNAME>/Sorting-Algorithms-Visualizer`
* Make changes to the `develop` or based off branch
* Pass the unit tests
* Submit a pull request

## How to apply new sorting algorithm?

### 1. Create sorting algorithm function in **_algorithms.py_**

Make changes to the **_algorithms.py_** file. Your function has to take as the argument *disp* object that has array implemented in the **_visualizer.py_** and **_main.py_**. Remember, your main sorting function must always return `True` generator. You can take the piece of code below as the template:

```python
def NAME_sort(disp):
    # Access elements in the array
    # via passed 'disp' object:
    disp.arr
  
    '''Your code'''
  
    # Write following code whenever
    # elements in the array change position:
	disp.show_arr(clear_arr=True)
	yield True
```

### 2. List your algorithm function in **_visualizer.py_**

Add to the class attribute dictionary `self.sorting_types` your function:

```python
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
            9: ("Radix sort", algorithms.radix_sort),
            10: ("NAME sort", algorithms.NAME_sort), # YOUR FUNCTION !!!
        }
```

### 3. Bind new keyboard key with your function in **_main.py_** to select it inside the app

Bind any available keyboard using `pygame` module. For example `pygame.K_a` (check [ pygame documentation](https://www.pygame.org/docs/ref/key.html)). Therefore, at the end of the while loop in the **_main.py_** add following code:

```python
elif event.key == pygame.K_a and not start_sorting:
    algorithm, algorithm_name = disp.sorting_types[10][1], disp.sorting_types[10][0]
```

(where `pygame.K_a` can also be other selected key and number `10` in `disp.sorting_types` is the number of your function keyword in `self.sorting_types` dictionary inside `class DisplayAlgorithm` - check step number 2)

### 4. Visualize your function running **_main.py_** file

### 5. Test your function in **_tests.py_**

Add suite for your function to test it in **_tests.py_** file. To do that change the range of for loop inside `run_all_tests` function:

```python
def run_all_tests():
    suites_list = []
    loader = unittest.TestLoader()

    for i in range(1, 11): # 10+1 : YOUR FUNCTION KEY NUMBER (check step number 2) INCREMENTED BY 1
        suite = loader.loadTestsFromTestCase(test_sorting_algorithms(i))
        suites_list.append(suite)

    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite(suites_list))
```

#### 6. Pass the tests and make a pull request
