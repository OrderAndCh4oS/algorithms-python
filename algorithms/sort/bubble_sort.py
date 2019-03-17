from script_benchmark_tools.benchmarks_report import generate_benchmark_report, save_benchmark_results, save_plot


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    from script_benchmark_tools import Script
    from benchmarks.run_scripts.run_scripts_with_n_random_list import run_scripts_with_n_random_list

    filename = 'bubble_sort_algorithm'

    benchmark_data = {
        'title': 'Bubble Sort Benchmark Results',
        'proof_data': [6, 3, 1, 2, 5, 4],
        'filename': filename,
        'n_steps': [3, 5, 10, 100, 500, 1000],
        'benchmark': run_scripts_with_n_random_list,
        'scripts': (
            Script(bubble_sort, 'sarcoma'),
        ),
    }

    output, plot = generate_benchmark_report(**benchmark_data)

    save_benchmark_results(output, filename)
    print(output)

    save_plot(plot, filename)
    plot.show()
