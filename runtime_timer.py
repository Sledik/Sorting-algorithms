import timeit
import random


def test_sorting_algorithms(list_size, run_count):
    # Pole obsahující daný počet (list_size) různých čísel od 1 do list_size
    list_of_numbers = random.sample(range(1, list_size + 1), list_size)

    algorithms = ["bubble_sort", "selection_sort", "insertion_sort", "merge_sort", "quick_sort"]

    for alg in algorithms:
        setup = "from {0} import {0}".format(alg)
        statement = "{0}({1})".format(alg, list_of_numbers)
        print("{0} na {1} čísel proběhl {2}krát za {3} sekund".format(
            alg, list_size, run_count, round(timeit.timeit(stmt=statement, setup=setup, number=run_count), 3)
        ))


if __name__ == '__main__':
    test_sorting_algorithms(1000, 100)
