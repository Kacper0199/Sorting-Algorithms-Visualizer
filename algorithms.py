def selection_sort(disp):
    for i in range(len(disp.arr)-1):
        min_val_ind = i
        for j in range(i+1, len(disp.arr)):
            if disp.arr[j] < disp.arr[min_val_ind]:
                min_val_ind = j
        if min_val_ind != i:
            disp.arr[min_val_ind], disp.arr[i] = disp.arr[i], disp.arr[min_val_ind]
            disp.show_arr(clear_arr=True)
            yield True


def insertion_sort(disp):
    for i in range(1, len(disp.arr)):
        for j in range(i, 0, -1):
            if disp.arr[j] < disp.arr[j-1]:
                disp.arr[j], disp.arr[j-1] = disp.arr[j-1], disp.arr[j]
                disp.show_arr(clear_arr=True)
                yield True


def bubble_sort(disp):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(len(disp.arr)-1):
            if disp.arr[i] > disp.arr[i+1]:
                disp.arr[i], disp.arr[i+1] = disp.arr[i+1], disp.arr[i]
                sorted = False
                disp.show_arr(clear_arr=True)
                yield True


def cocktail_sort(disp):
    sorted = False
    left_ptr, right_ptr = 0, len(disp.arr)-1

    while not sorted:
        sorted = True
        for i in range(right_ptr):
            if disp.arr[i] > disp.arr[i+1]:
                disp.arr[i], disp.arr[i+1] = disp.arr[i+1], disp.arr[i]
                sorted = False
                disp.show_arr(clear_arr=True)
                yield True
        left_ptr += 1
        right_ptr -= 1
        for i in range(right_ptr, left_ptr-1, -1):
            if disp.arr[i-1] > disp.arr[i]:
                disp.arr[i], disp.arr[i-1] = disp.arr[i-1], disp.arr[i]
                sorted = False
                disp.show_arr(clear_arr=True)
                yield True


def shell_sort(disp):
    n_arr = len(disp.arr)
    gap = n_arr // 2
    right_ptr, current_ptr = 0, 0

    while gap >= 1:
        for i in range(n_arr):
            current_ptr, right_ptr = i, i + gap
            if right_ptr >= n_arr:
                break
            while current_ptr >= 0:
                if disp.arr[current_ptr] < disp.arr[right_ptr]:
                    break
                disp.arr[current_ptr], disp.arr[right_ptr] = disp.arr[right_ptr], disp.arr[current_ptr]
                current_ptr -= gap
                right_ptr -= gap
                disp.show_arr(clear_arr=True)
                yield True
        gap //= 2


def quick_sort(disp):

    def quick_sort_build(disp, left_ptr, right_ptr):
        if left_ptr < right_ptr:
            partition_ptr = partition(disp, left_ptr, right_ptr)
            disp.show_arr(clear_arr=True)
            yield disp.arr
            yield from quick_sort_build(disp, left_ptr, partition_ptr-1)
            yield from quick_sort_build(disp, partition_ptr+1, right_ptr)

    yield from quick_sort_build(disp, 0, len(disp.arr)-1)


def partition(disp, left_ptr, right_ptr):
    i, j = left_ptr, right_ptr - 1
    pivot_num = disp.arr[right_ptr]

    while i < j:
        while i < right_ptr and disp.arr[i] < pivot_num:
            i += 1
        while j > left_ptr and disp.arr[j] >= pivot_num:
            j -= 1
        if i < j:
            disp.arr[i], disp.arr[j] = disp.arr[j], disp.arr[i]
        disp.show_arr(clear_arr=True)

    if disp.arr[i] > pivot_num:
        disp.arr[i], disp.arr[right_ptr] = disp.arr[right_ptr], disp.arr[i]
        disp.show_arr(clear_arr=True)

    return i


def merge_sort(disp):

    def merge(left_ptr, right_ptr):
        if right_ptr - left_ptr > 1:
            ref_ptr = (left_ptr + right_ptr)//2

            yield from merge(left_ptr, ref_ptr)
            yield from merge(ref_ptr, right_ptr)

            left_arr = disp.arr[left_ptr:ref_ptr]
            right_arr = disp.arr[ref_ptr:right_ptr]

            output_ind, left_ind, right_ind = left_ptr, 0, 0

            while left_ind < len(left_arr) and right_ind < len(right_arr):
                if left_arr[left_ind] < right_arr[right_ind]:
                    disp.arr[output_ind] = left_arr[left_ind]
                    left_ind += 1
                else:
                    disp.arr[output_ind] = right_arr[right_ind]
                    right_ind += 1
                output_ind += 1
                disp.show_arr(clear_arr=True)

            while left_ind < len(left_arr):
                disp.arr[output_ind] = left_arr[left_ind]
                left_ind += 1
                output_ind += 1
                disp.show_arr(clear_arr=True)

            while right_ind < len(right_arr):
                disp.arr[output_ind] = right_arr[right_ind]
                right_ind += 1
                output_ind += 1
                disp.show_arr(clear_arr=True)

        yield disp.arr

    yield from merge(0, len(disp.arr))


def max_heapify(arr, n, i):
    heapify = True

    while heapify:
        max_val_ind = i
        left_child_ind, right_child_ind = i*2+1, i*2+2

        if left_child_ind < n and arr[max_val_ind] < arr[left_child_ind]:
            max_val_ind = left_child_ind

        if right_child_ind < n and arr[max_val_ind] < arr[right_child_ind]:
            max_val_ind = right_child_ind

        if max_val_ind != i:
            arr[i], arr[max_val_ind] = arr[max_val_ind], arr[i]
            i = max_val_ind
        else:
            heapify = False


def heap_sort(disp):
    n = len(disp.arr)

    for i in range(n//2-1, -1, -1):
        max_heapify(disp.arr, n, i)
        disp.show_arr(clear_arr=True)
        yield True

    for i in range(n-1, 0, -1):
        disp.arr[i], disp.arr[0] = disp.arr[0], disp.arr[i]
        max_heapify(disp.arr, i, 0)
        disp.show_arr(clear_arr=True)
        yield True


def radix_sort(disp):
    num_digits = len(str(max(disp.arr)))
    n_arr = len(disp.arr)

    for digit in range(num_digits):
        bucket_arr = [[] for _ in range(10)]
        for j in range(n_arr):
            bucket_index = disp.arr[j]//10**(digit) % 10
            bucket_arr[bucket_index].append(disp.arr[j])

        disp.arr = []
        for k in range(10):
            disp.arr += bucket_arr[k]
            disp.show_arr(clear_arr=True)
            yield True
