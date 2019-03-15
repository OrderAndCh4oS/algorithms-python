from random import shuffle


def not_bubble_sort(arr):
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


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    unsorted_list = [6, 3, 1, 2, 5, 4]
    not_bubble_sort(unsorted_list)
    print(unsorted_list)
    long_unsorted_list = [x for x in range(1000)]
    shuffle(long_unsorted_list)
    not_bubble_sort(long_unsorted_list)
    print(long_unsorted_list)
