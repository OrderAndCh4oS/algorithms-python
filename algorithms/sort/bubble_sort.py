from random import shuffle


def bubble_sort(arr):
    length = len(arr)
    while True:
        is_sorted = True
        for i in range(length - 1):
            if arr[i] > arr[i + 1]:
                is_sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        if is_sorted:
            break

    return arr


if __name__ == '__main__':
    unsorted_list = [6, 3, 1, 2, 5, 4]
    bubble_sort(unsorted_list)
    print(unsorted_list)
    long_unsorted_list = [x for x in range(1000)]
    shuffle(long_unsorted_list)
    bubble_sort(long_unsorted_list)
    print(long_unsorted_list)
