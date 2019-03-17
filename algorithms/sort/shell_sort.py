def shell_sort(arr):
    n = len(arr)

    h = 1
    while h < n / 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and arr[j] < arr[j - h]:
                arr[j - h], arr[j] = arr[j], arr[j - h]
                j -= h
        h = int(h / 3)

    return arr


def is_h_sorted(arr, h):
    for i in range(h, len(arr)):
        if arr[i] < arr[i - h]:
            return False
    return True


if __name__ == '__main__':
    from script_benchmark_tools import Script
    from script_benchmark_tools.benchmarks_report import generate_benchmark_report, save_plot, save_benchmark_results
    from benchmarks.run_scripts.run_scripts_with_n_random_list import run_scripts_with_n_random_list

    filename = 'shell_sort_algorithm'

    benchmark_data = {
        'title': 'Shell Sort Benchmark Results',
        'proof_data': [6, 3, 1, 2, 5, 4],
        'filename': 'shell_sort_algorithm',
        'n_steps': [3, 5, 10, 100, 500, 1000],
        'benchmark': run_scripts_with_n_random_list,
        'scripts': (
            Script(shell_sort, 'sarcoma'),
        ),
    }

    output, plot = generate_benchmark_report(**benchmark_data)

    save_benchmark_results(output, filename)
    print(output)

    save_plot(plot, filename)
    plot.show()
