def insertion_sort(arr):
    length = len(arr)
    for i in range(length):
        index = i
        for j in (x for x in reversed(range(i)) if x not in a):
            if arr[j] < arr[index]:
                arr[index], arr[j] = arr[j], arr[index]


if __name__ == '__main__':
    unsorted_list = [3, 1, 2, 5, 4]
    insertion_sort(unsorted_list)
    print(unsorted_list)
