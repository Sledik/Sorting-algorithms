from insertion_sort import insertion_sort


def is_sorted(array):
	if len(array) <= 1:
		return True

	for i in range(len(array) - 2):
		if array[i] > array[i + 1]:
			return False

	return True


def pre_sort(array):

	small_items = []

	# Projdi všechny položky pole array
	for i in range(len(array) - 1):

		if len(small_items) == 0:
			small_items.append(array[i])
			array.pop(i)
		elif array[i - len(small_items)] <= small_items[-1]:
			small_items.append(array[i - len(small_items)])
			array.pop(i - len(small_items) + 1)

	if len(array) > 1:
		final_arr = small_items[::-1] + pre_sort(array)
	else:
		final_arr = small_items[::-1] + array
	# Vrať seřazené pole
	return final_arr


def multiselect_sort(array):

	array = pre_sort(array)
	insertion_sort(array)

	return array
