from random import shuffle


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    unsorted_list = [6, 3, 1, 2, 5, 4]
    bubble_sort(unsorted_list)
    print(unsorted_list)
    long_unsorted_list = [x for x in range(1000)]
    shuffle(long_unsorted_list)
    bubble_sort(long_unsorted_list)
    print(long_unsorted_list)
