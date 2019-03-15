from script_benchmark_tools.charts.plot_visual import display_benchmark_plot
from script_benchmark_tools.display_benchmark_results import display_benchmark_results
from script_benchmark_tools.run_benchmarks import run_benchmarks
from script_benchmark_tools.script import Script
from terminal_table import Table

from algorithms.sort.bubble_sort import not_bubble_sort, bubble_sort
from algorithms.sort.insertion_sort import insertion_sort
from algorithms.sort.selection_sort import selection_sort
from algorithms.sort.shell_sort import shell_sort
from benchmarks.providers.random_list_provider import RandomListProvider


def run_scripts_with_n_random_list(scripts, n):
    arr_provider = RandomListProvider(n, 0, 1000)
    return n, run_benchmarks(scripts, arr_provider, 100)


if __name__ == '__main__':

    all_scripts = (
        Script(not_bubble_sort, 'sarcoma'),
        Script(bubble_sort, 'geeks_for_geeks'),
        Script(selection_sort, 'sarcoma'),
        Script(insertion_sort, 'sarcoma'),
        Script(shell_sort, 'sarcoma'),
    )

    print('Proofs\n------')

    print(
        Table.create(
            [(
                "[6, 3, 1, 2, 5, 4]",
                str(script(arr=[6, 3, 1, 2, 5, 4])),
                script.name(),
                script.user()
            ) for script in all_scripts],
            ('Input', 'Output', 'Script', 'User')
        )
    )

    title = 'Benchmarks'
    benchmarks = map(lambda n: run_scripts_with_n_random_list(all_scripts, n),
                     [10, 50, 100, 500, 1000, 2500, 5000])
    results = [(n, result) for n, result in benchmarks]

    display_benchmark_plot(results, title, loglog=True)

    print('%s\n----------\n' % title)

    for n, result in results:
        print('N = %d\n------' % n)
        display_benchmark_results(result)
