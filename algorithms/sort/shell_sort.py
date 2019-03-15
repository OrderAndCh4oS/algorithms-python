from random import shuffle


def shell_sort(arr):
    n = len(arr)

    h = 1
    while h < n / 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and arr[j] < arr[j - h]:
                arr[j - h], arr[j] = arr[j], arr[j - h]
                j -= h
        h = int(h / 3)

    return arr


def is_h_sorted(arr, h):
    for i in range(h, len(arr)):
        if arr[i] < arr[i - h]:
            return False
    return True


if __name__ == '__main__':
    unsorted_list = [6, 3, 1, 10, 2, 9,  5, 4, 7, 8]
    shell_sort(unsorted_list)
    print(unsorted_list)

    long_unsorted_list = [x for x in range(100)]
    shuffle(long_unsorted_list)
    shell_sort(long_unsorted_list)
    print(long_unsorted_list)
