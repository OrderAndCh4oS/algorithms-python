from random import shuffle


def insertion_sort(arr):
    for i in range(len(arr)):
        for j in reversed(range(i + 1)):
            if j is 0 or arr[j-1] < arr[j]:
                break
            arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr


if __name__ == '__main__':
    unsorted_list = [6, 3, 1, 2, 5, 4]
    insertion_sort(unsorted_list)
    print(unsorted_list)
    long_unsorted_list = [x for x in range(100)]
    shuffle(long_unsorted_list)
    insertion_sort(long_unsorted_list)
    print(long_unsorted_list)
