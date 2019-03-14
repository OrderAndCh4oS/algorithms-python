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
