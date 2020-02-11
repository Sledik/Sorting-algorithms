from insertion_sort import insertion_sort


# Předřadící funkce – použita v hlavní funkci
def pre_sort(array):

	# Pole pro ukládání nejmenších prvků
	small_items = []

	# Projdi všechny položky pole array
	for i in range(len(array)):

		# Pokud pole small_items neobsahuje nic, přesuň tam první prvek pole array
		if len(small_items) == 0:
			small_items.append(array[i])
			array.pop(i)
		# Pokud daný prvek pole array je menší (nebo roven) než poslední prvek pole small_items,
		# přesuň do small_items tento prvek
		elif array[i - len(small_items)] <= small_items[-1]:
			small_items.append(array[i - len(small_items)])
			array.pop(i - len(small_items) + 1)

	# Slož dohromady nejmenší čísla a neseřazený zbytek pole array, na který je rekurzivně zavolána
	# funkce pre_sort(array). To dělej dokud je pole k řazení dost velké
	if len(array) > 1:
		final_arr = small_items[::-1] + pre_sort(array)
	else:
		final_arr = small_items[::-1] + array

	# Vrať předřazené pole
	return final_arr


# Hlavní funkce
def multiselect_sort(array):

	# Předřaď pole array
	array = pre_sort(array)

	# Pokud pole obsahuje více než 7000 prvků, je vhodné ho předřadit vícekrát (podle odhadu)
	if len(array) >= 7000:
		array = pre_sort(array)

	# Použij Insertion sort, který je rychlý na předřazených polích
	insertion_sort(array)

	# Vrať seřazené pole
	return array
