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
    from script_benchmark_tools import Script
    from script_benchmark_tools.benchmark_report import generate_benchmark_report
    from benchmarks.run_scripts.run_scripts_with_n_random_list import run_scripts_with_n_random_list

    filename = 'selection_sort_algorithm'

    benchmark_data = {
        'title': 'Selection Sort Benchmark Results',
        'proof_data': [6, 3, 1, 2, 5, 4],
        'filename': 'selection_sort_algorithm',
        'n_steps': [3, 5, 10, 100, 500, 1000],
        'benchmark': run_scripts_with_n_random_list,
        'scripts': (
            Script(selection_sort, 'sarcoma'),
        ),
        'use_ansi': True
    }

    output, plot = generate_benchmark_report(**benchmark_data)

    print(output)
    plot.show()
