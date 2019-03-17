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
    from script_benchmark_tools import Script
    from script_benchmark_tools.benchmarks_report import generate_benchmark_report
    from benchmarks.run_scripts.run_scripts_with_n_random_list import run_scripts_with_n_random_list

    filename = 'quick_sort_algorithm'

    benchmark_data = {
        'title': 'Quick Sort Benchmark Results',
        'proof_data': [6, 3, 1, 2, 5, 4],
        'filename': filename,
        'n_steps': [3, 5, 10, 100, 500, 1000],
        'benchmark': run_scripts_with_n_random_list,
        'scripts': (
            Script(quick_sort, 'sarcoma'),
        ),
        'use_ansi': True
    }

    output, plot = generate_benchmark_report(**benchmark_data)

    print(output)
    plot.show()
