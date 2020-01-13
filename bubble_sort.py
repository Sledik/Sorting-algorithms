def bubble_sort(array):

    # Tento for cyklus zajišťuje, že se nekontroluje největší prvek,
    # který je po dokončení jednoho cyklu seřazen na konci
    for i in range(len(array) - 1):

        # Projdi všechny prvky daného pole kromě již seřazených
        for j in range(len(array) - 1 - i):

            # Porovnej dva sousední elementy pole a pokud je první element větší než po něm následující element,
            # prohoď je.
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
