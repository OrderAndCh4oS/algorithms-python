def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge(left, right):
    result = []
    while len(left) and len(right):
        result.append(
            left.pop(0) if left[0] < right[0] else right.pop(0)
        )

    return result + left + right


if __name__ == '__main__':
    from script_benchmark_tools import Script
    from script_benchmark_tools.benchmarks_report import generate_benchmark_report
    from benchmarks.run_scripts.run_scripts_with_n_random_list import run_scripts_with_n_random_list

    filename = 'merge_sort_algorithm'

    benchmark_data = {
        'title': 'Merge Sort Benchmark Results',
        'proof_data': [6, 3, 1, 2, 5, 4],
        'filename': filename,
        'n_steps': [3, 5, 10, 100, 500, 1000],
        'benchmark': run_scripts_with_n_random_list,
        'scripts': (
            Script(merge_sort, 'sarcoma'),
        ),
        'use_ansi': True
    }

    output, plot = generate_benchmark_report(**benchmark_data)

    print(output)
    plot.show()
