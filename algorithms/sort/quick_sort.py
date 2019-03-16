from random import shuffle


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr):
    def f(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)

            f(arr, low, pi - 1)
            f(arr, pi + 1, high)

        return arr

    return f(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    unsorted_list = [6, 3, 1, 2, 5, 4, 8, 9, 10]
    print(quick_sort(unsorted_list))
    print(unsorted_list)

    long_unsorted_list = [x for x in range(101)]
    shuffle(long_unsorted_list)
    print(quick_sort(long_unsorted_list))
    print(long_unsorted_list)
