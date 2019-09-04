def merge(array1, array2):

	# Připrav pole, do kterého budeme ukládat prvky ve správném pořadí
	merged_array = []
	# Pomocné indexy i a j. Index i pro array1 a index j pro array 2
	i = j = 0

	# Dokud není index pole moc velký:
	while i < len(array1) and j < len(array2):
		# Porovnej prvky obou polí na daných indexech a ulož do připraveného pole to menší z nich
		if array1[i] < array2[j]:
			merged_array.append(array1[i])
			# Posuň index pro array1
			i += 1
		else:
			merged_array.append(array2[j])
			# Posuň index pro array2
			j += 1

	# Pokud už v jednom z polí nezbývají další prvky, ulož do připraveného pole zbytek pole, které má ještě prvky
	if i >= len(array1):
		merged_array.extend(array2[j:])
	else:
		merged_array.extend(array1[i:])

	return merged_array


def merge_sort(array):

	# Pokud pole obsahuje jen jeden nebo méně prvků, které musí být seřazeny, vrať samotné pole
	if len(array) <= 1:
		return array
	else:
		# Prováděj rekurzivně funkci merge_sort na menší a menší části pole
		first_part = merge_sort(array[:len(array) // 2])
		second_part = merge_sort(array[len(array) // 2:])

		return merge(first_part, second_part)
