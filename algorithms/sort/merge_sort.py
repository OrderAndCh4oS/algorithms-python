from random import shuffle


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) and len(right):
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result + left + right


if __name__ == '__main__':
    print(merge([1, 4], [2, 3, 5]))
    unsorted_list = [6, 3, 1, 2, 5, 4, 8, 9, 10]
    print(merge_sort(unsorted_list))
    print(unsorted_list)

    long_unsorted_list = [x for x in range(101)]
    shuffle(long_unsorted_list)
    print(merge_sort(long_unsorted_list))
    print(long_unsorted_list)
