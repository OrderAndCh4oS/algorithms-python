from random import shuffle


def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        index = i
        for j in range(i + 1, length):
            if arr[j] < arr[index]:
                arr[index], arr[j] = arr[j], arr[index]

    return arr


if __name__ == '__main__':
    unsorted_list = [6, 3, 1, 2, 5, 4]
    selection_sort(unsorted_list)
    print(unsorted_list)

    long_unsorted_list = [x for x in range(100)]
    shuffle(long_unsorted_list)
    selection_sort(long_unsorted_list)
    print(long_unsorted_list)
