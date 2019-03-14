from script_benchmark_tools.charts.plot_visual import display_benchmark_plot
from script_benchmark_tools.display_benchmark_results import display_benchmark_results
from script_benchmark_tools.run_benchmarks import run_benchmarks
from script_benchmark_tools.script import Script

from algorithms.sort.insertion_sort import insertion_sort
from algorithms.sort.selection_sort import selection_sort
from benchmarks.providers.random_list_provider import RandomListProvider


def run_scripts_with_n_random_list(scripts, n):
    arr_provider = RandomListProvider(n, 0, 100)
    return n, run_benchmarks(scripts, arr_provider, 100)


if __name__ == '__main__':

    all_scripts = (
        Script(selection_sort, 'sarcoma'),
        Script(insertion_sort, 'sarcoma'),
    )

    print('Proofs\n------')

    for script in all_scripts:
        print(script(arr=[6, 3, 1, 2, 5, 4]))

    title = 'Benchmarks\n----------'
    benchmarks = map(lambda n: run_scripts_with_n_random_list(all_scripts, n), [10, 50, 100, 500, 1000])
    results = [(n, result) for n, result in benchmarks]

    display_benchmark_plot(results, title)

    print(title)
    for n, result in results:
        print('N = %d\n------' % n)
        display_benchmark_results(result)
