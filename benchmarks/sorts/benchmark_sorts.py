from script_benchmark_tools import generate_benchmarks
from script_benchmark_tools.run_benchmarks import run_benchmarks
from script_benchmark_tools.script import Script

from algorithms.sort.bubble_sort import bubble_sort
from algorithms.sort.insertion_sort import insertion_sort
from algorithms.sort.merge_sort import merge_sort
from algorithms.sort.quick_sort import quick_sort
from algorithms.sort.selection_sort import selection_sort
from algorithms.sort.shell_sort import shell_sort
from benchmarks.providers.random_list_provider import RandomListProvider


def run_scripts_with_n_random_list(scripts, n):
    arr_provider = RandomListProvider(n, 0, n * 2)
    return n, run_benchmarks(scripts, arr_provider, 100)


benchmark_data = {
    'title': 'Sorting Algorithm Benchmark Results',
    'proof_data': [6, 3, 1, 2, 5, 4],
    'filename': 'sorting_algorithm',
    'n_steps': [3, 5, 10, 100, 500, 1000, 2500, 5000, 10000],
    'benchmark': run_scripts_with_n_random_list,
    'scripts': (
        Script(bubble_sort, 'sarcoma'),
        Script(selection_sort, 'sarcoma'),
        Script(insertion_sort, 'sarcoma'),
        Script(shell_sort, 'sarcoma'),
        Script(merge_sort, 'sarcoma'),
        Script(quick_sort, 'sarcoma'),
    )
}

if __name__ == '__main__':
    generate_benchmarks(**benchmark_data)
