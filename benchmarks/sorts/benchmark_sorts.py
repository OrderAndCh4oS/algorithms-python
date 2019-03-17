from script_benchmark_tools.benchmark_report import benchmark_report
from script_benchmark_tools.script import Script

from algorithms.sort.bubble_sort import bubble_sort
from algorithms.sort.insertion_sort import insertion_sort
from algorithms.sort.merge_sort import merge_sort, merge_insertion_sort, merge_insertion_check_sort
from algorithms.sort.quick_sort import quick_sort
from algorithms.sort.selection_sort import selection_sort
from algorithms.sort.shell_sort import shell_sort
from benchmarks.run_scripts.run_scripts_with_n_random_list import run_scripts_with_n_random_list

if __name__ == '__main__':
    n_steps_full = [3, 5, 10, 100, 500, 1000, 2500, 5000, 10000]
    n_steps_quick = [3, 5, 10, 25, 50, 75, 100]

    benchmark_data = {
        'title': 'Sorting Algorithm Benchmark Results',
        'proof_data': [6, 3, 1, 2, 5, 4],
        'filename': 'sorting_algorithm',
        'n_steps': n_steps_full,
        'benchmark': run_scripts_with_n_random_list,
        'scripts': (
            Script(bubble_sort, 'sarcoma'),
            Script(selection_sort, 'sarcoma'),
            Script(insertion_sort, 'sarcoma'),
            Script(shell_sort, 'sarcoma'),
            Script(merge_sort, 'sarcoma'),
            Script(merge_insertion_sort, 'sarcoma'),
            Script(merge_insertion_check_sort, 'sarcoma'),
            Script(quick_sort, 'sarcoma'),
        )
    }

    benchmark_report(**benchmark_data)
