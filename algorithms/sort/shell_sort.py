from random import shuffle


def shell_sort(arr):
    n = len(arr)

    h = 1
    while h < n / 3:
        h = 3 * h+1

    while h >= 1:
        for i in range(h, n):
            for j in reversed(range(0, i + 1, h)):
                if j < h or arr[j] >= arr[j-h]:
                    break
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
        h = int(h / 3)


if __name__ == '__main__':
    unsorted_list = [6, 3, 1, 10, 2, 9,  5, 4, 7, 8]
    shell_sort(unsorted_list)
    print(unsorted_list)

    long_unsorted_list = [x for x in range(100)]
    shuffle(long_unsorted_list)
    print(long_unsorted_list)
    shell_sort(long_unsorted_list)
    print(long_unsorted_list)
