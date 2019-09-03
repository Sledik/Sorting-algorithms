def merge(array1, array2):

	merged_array = []
	i = j = 0

	while i < len(array1) and j < len(array2):
		if array1[i] < array2[j]:
			merged_array.append(array1[i])
			i += 1
		else:
			merged_array.append(array2[j])
			j += 1

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

		first_part = merge_sort(array[:len(array) // 2])
		second_part = merge_sort(array[len(array) // 2:])

		return merge(first_part, second_part)
