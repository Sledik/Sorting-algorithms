import random


def get_pivot(array, low_index, high_index):

    # Hledáme index prvku uprostřed
    middle_index = (high_index + low_index) // 2

    # Prvky ze kterých vybíráme pivota:
    low = array[low_index]
    mid = array[middle_index]
    high = array[high_index]

    pivot = high_index
    if low < mid:
        if mid < high:
            pivot = middle_index
    elif low < high:
        pivot = low_index

    return pivot


def partition(array, low_index, high_index):

    # Najdi pozici pivota pomocí funkce get_pivot a ulož do jiné proměnné jeho hodnotu
    pivot_index = get_pivot(array, low_index, high_index)
    pivot_value = array[pivot_index]

    # Přemisti pivota na začátek pole prohozením s prvním prvkem pole
    array[pivot_index], array[low_index] = array[low_index], array[pivot_index]

    # Ukládáme si pozici, která nám bude určovat, kam máme později zařadit pivota. Značí jakousi hranici
    # mezi většími a menšími čísly
    position = low_index

    # Projdi všechny prvky pole
    for i in range(low_index, high_index + 1):
        # Pokud je tento prvek menší než pivot, prohoď prvek na naší "pozici" s tímto prvkem
        if array[i] < pivot_value:
            # Posuň pozici dále
            position += 1
            array[position], array[i] = array[i], array[position]

    # Zařaď pivot na naši uloženou pozici
    array[low_index], array[position] = array[position], array[low_index]

    # Vrať pozici, která nám jakoby rozděluje pole na dvě nová
    return position


def quick_sort(array, low_index=0, high_index=None):

    if high_index is None:
        high_index = len(array) - 1

    # Pokud pole obsahuje alespoň 2 prvky, které musí být seřazeny, pokračuj v řazení
    if low_index < high_index:

        # Ulož pozici prvku, který rozděluje původní pole na 2 další
        split_index = partition(array, low_index, high_index)
        # Seřaď prvky (proveď funkci quick_sort) na 1. polovinu pole (končící rozdělujícím prvkem)
        quick_sort(array, low_index, split_index - 1)
        # Seřaď prvky na 2. polovinu původního pole (za rozdělujícím prvkem)
        quick_sort(array, split_index + 1, high_index)
