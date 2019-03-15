from random import shuffle


def selection_sort(arr):
    length = len(arr)
    for i in range(length):
        min_item = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_item]:
                min_item = j

        arr[min_item], arr[i] = arr[i], arr[min_item]

    return arr


if __name__ == '__main__':
    unsorted_list = [6, 3, 1, 2, 5, 4]
    selection_sort(unsorted_list)
    print(unsorted_list)

    long_unsorted_list = [x for x in range(100)]
    shuffle(long_unsorted_list)
    selection_sort(long_unsorted_list)
    print(long_unsorted_list)
