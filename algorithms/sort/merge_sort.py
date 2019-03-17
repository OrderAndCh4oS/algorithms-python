from algorithms.sort.insertion_sort import insertion_sort


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2

    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge_insertion_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    if n < 15:
        insertion_sort(arr)
        return arr

    mid = len(arr) // 2

    return merge(merge_insertion_sort(arr[:mid]), merge_insertion_sort(arr[mid:]))


def merge_insertion_check_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    if n <= 15:
        insertion_sort(arr)
        return arr

    mid = len(arr) // 2

    left = merge_insertion_sort(arr[:mid])
    right = merge_insertion_sort(arr[mid:])

    return merge(left, right) if left[-1] > right[0] else left + right


def merge(left, right):
    result = []
    while len(left) and len(right):
        result.append(
            left.pop(0) if left[0] < right[0] else right.pop(0)
        )

    return result + left + right


if __name__ == '__main__':
    from script_benchmark_tools import Script, run_scripts_with_n_sized_list
    from script_benchmark_tools.benchmark_report import generate_benchmark_report

    filename = 'merge_sort_algorithm'

    benchmark_data = {
        'title': 'Merge Sort Benchmark Results',
        'proof_data': [6, 3, 1, 2, 5, 4],
        'filename': filename,
        'n_steps': [3, 5, 10, 100, 500, 1000, 10000, 25000],
        'benchmark': run_scripts_with_n_sized_list,
        'scripts': (
            Script(merge_sort, 'sarcoma'),
            Script(merge_insertion_sort, 'sarcoma'),
            Script(merge_insertion_check_sort, 'sarcoma'),
        ),
        'use_ansi': True
    }

    output, plot = generate_benchmark_report(**benchmark_data)

    print(output)
    plot.show()
