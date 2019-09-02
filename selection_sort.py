def selection_sort(array):

    # Projdi všechny položky pole array
    for i in range(0, len(array) - 1):

        # Projdi všechny neutříděné položky pole array a najdi nejmenší položku pole array
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # Prohoď nejmenší prvek pole array s prvním (neutříděným) prvkem
        array[min_index], array[i] = array[i], array[min_index]

    # Vrať seřazené pole
    return array
