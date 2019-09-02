import timeit
import random


def test_sorting_algorithms(list_size):
    # Pole obsahující daný počet (list_size) různých čísel od 1 do list_size
    list_of_numbers = random.sample(range(1, list_size + 1), list_size)

    # Selection sort
    mysetup = "from selection_sort import selection_sort"
    mystatement = "selection_sort({})".format(list_of_numbers)

    print("Selection sort na 100 čísel proběhl tisíckrát za",
          timeit.timeit(stmt=mystatement, setup=mysetup, number=1000), "sekund")

    # Bubble sort
    mysetup = "from bubble_sort import bubble_sort"
    mystatement = "bubble_sort({})".format(list_of_numbers)

    print("Bubble sort na 100 čísel proběhl tisíckrát za",
          timeit.timeit(stmt=mystatement, setup=mysetup, number=1000), "sekund")

    # Quick sort
    mysetup = "from quick_sort import quick_sort"
    mystatement = "quick_sort({}, {}, {})".format(list_of_numbers, 0, len(list_of_numbers) - 1)

    print("Quick sort na 100 čísel proběhl tisíckrát za",
          timeit.timeit(stmt=mystatement, setup=mysetup, number=1000), "sekund")


if __name__ == '__main__':
    test_sorting_algorithms(100)