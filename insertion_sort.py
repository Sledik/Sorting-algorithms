def insertion_sort(array):
	# Projdi celé pole array
	for number in array:
		# Ulož pozici tohoto daného prvku
		position = array.index(number)

		# Dokud pozice nemá index 0, hledej číslo menší než toto dané číslo
		while position > 0:
			# Pokud je prvek nalevo od tohoto čísla větší, procházej případně nadále většími čísly,
			# než narazíš na menší. Sem pak vlož prvek.
			if array[position - 1] > array[position]:
				array[position - 1], array[position] = array[position], array[position - 1]
				position -= 1
			else:
				break
