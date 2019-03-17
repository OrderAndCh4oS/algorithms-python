from script_benchmark_tools.run_benchmarks import run_benchmarks

from benchmarks.providers.random_list_provider import RandomListProvider


def run_scripts_with_n_random_list(scripts, n):
    arr_provider = RandomListProvider(n, 0, n * 2)
    return n, run_benchmarks(scripts, arr_provider, 100)
