def insertion_sort(arr):
    for i in range(len(arr)):
        for j in reversed(range(i + 1)):
            if j is 0 or arr[j-1] < arr[j]:
                break
            arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr


if __name__ == '__main__':
    from script_benchmark_tools import Script
    from script_benchmark_tools.benchmark_report import generate_benchmark_report
    from benchmarks.run_scripts.run_scripts_with_n_random_list import run_scripts_with_n_random_list

    filename = 'insertion_sort_algorithm'

    benchmark_data = {
        'title': 'Insertion Sort Benchmark Results',
        'proof_data': [6, 3, 1, 2, 5, 4],
        'filename': filename,
        'n_steps': [3, 5, 10, 100, 500, 1000],
        'benchmark': run_scripts_with_n_random_list,
        'scripts': (
            Script(insertion_sort, 'sarcoma'),
        ),
        'use_ansi': True
    }

    output, plot = generate_benchmark_report(**benchmark_data)

    print(output)
    plot.show()
