import timeit
import random


def test_sorting_algorithms(list_size, run_count):
    # Pole obsahující daný počet (list_size) různých čísel od 1 do list_size
    list_of_numbers = random.sample(range(1, list_size + 1), list_size)

    # Selection sort
    mysetup = "from selection_sort import selection_sort"
    mystatement = "selection_sort({})".format(list_of_numbers)

    print("Selection sort na", list_size, "čísel proběhl tisíckrát za",
          timeit.timeit(stmt=mystatement, setup=mysetup, number=run_count), "sekund")

    # Bubble sort
    mysetup = "from bubble_sort import bubble_sort"
    mystatement = "bubble_sort({})".format(list_of_numbers)

    print("Bubble sort na", list_size, "čísel proběhl tisíckrát za",
          timeit.timeit(stmt=mystatement, setup=mysetup, number=run_count), "sekund")

    # Quick sort
    mysetup = "from quick_sort import quick_sort"
    mystatement = "quick_sort({})".format(list_of_numbers)

    print("Quick sort na", list_size, "čísel proběhl tisíckrát za",
          timeit.timeit(stmt=mystatement, setup=mysetup, number=run_count), "sekund")

    # Merge sort
    mysetup = "from merge_sort import merge_sort"
    mystatement = "merge_sort({})".format(list_of_numbers)
    print("Merge sort na", list_size, "čísel proběhl tisíckrát za",
          timeit.timeit(stmt=mystatement, setup=mysetup, number=run_count), "sekund")


if __name__ == '__main__':
    test_sorting_algorithms(100, 1000)
