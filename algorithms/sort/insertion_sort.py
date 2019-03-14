def insertion_sort(arr):
    for i in range(len(arr)):
        for j in reversed(range(i + 1)):
            if j > 0 and arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]


if __name__ == '__main__':
    unsorted_list = [6, 3, 1, 2, 5, 4]
    insertion_sort(unsorted_list)
    print(unsorted_list)

