def insertion_sort(array):
	# Projdi celé pole array
	for i in range(1, len(array)):

		# Dokud pozice i nemá index 0, hledej číslo menší než toto dané číslo
		while i > 0:
			# Pokud je prvek nalevo od tohoto čísla větší, procházej případně nadále většími čísly,
			# než narazíš na menší. Sem pak vlož prvek.
			if array[i - 1] > array[i]:
				array[i - 1], array[i] = array[i], array[i - 1]
				i -= 1
			else:
				break
