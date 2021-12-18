import math
import ast

def count_nested_bracket(number, to):
	nested_bracket = 0
	for i in range(0, to):
		if number[i] == "[":
			nested_bracket += 1
		elif number[i] == "]":
			nested_bracket -= 1
	return nested_bracket

#                          i
#                          v
def explode(number, i): # [3,2]
	save_size = len(number)
	j = i - 2
	# check left
	while j > 0 and j < len(number) - 1 and not isinstance(number[j], int):
		j -= 1
	if isinstance(number[j], int):
		number[j] += number[i]
#               i
#               v
	i += 2 # [3,2]
	k = i + 2
	while k > 0 and k < len(number) - 1 and not isinstance(number[k], int):
		k += 1
	if isinstance(number[k], int):
		number[k] += number[i]
	i -= 3
	for n  in range(0, 4):
		number.pop(i)
	number[i] = 0
	print("after explode: ", end="")
	print_number(number)

def split(number, i):
	nb = number[i]
	number.insert(i, "]")
	to_insert = math.ceil(nb / 2)
	number.insert(i, to_insert)
	number.insert(i, ",")
	to_insert = math.floor(nb / 2)
	number.insert(i, to_insert)
	number.insert(i, "[")
	number.pop(i + 5)
	print("after split: ", end="")
	print_number(number)

def check_for_explode(number):
	nested_bracket = 0
	i = 0
	while i < len(number):
		if nested_bracket > 4 and isinstance(number[i], int) and  isinstance(number[i + 2], int): # explode
			explode(number, i)
			i = 0
			nested_bracket = 0
		if number[i] == "[":
			nested_bracket += 1
		elif number[i] == "]":
			nested_bracket -= 1
		i += 1

def reduce_number(number):
	check_for_explode(number)
	i = 0
	while i < len(number):
		if isinstance(number[i], int) and number[i] > 9:
			split(number, i)
			i = 0
			nested_bracket = 0
			check_for_explode(number)
		i += 1

def print_number(number):
	print(''.join(map(str, number)))

def calculate_magnitude(number):
	magnitude = 0
	left, right = number
	left = left if isinstance(left, int) else calculate_magnitude(left)
	right = right if isinstance(right, int) else calculate_magnitude(right)
	magnitude = 3 * left + 2 * right
	return magnitude

def main():
	f = open('../input', 'r')
	lines = f.readlines()
	f.close()
	array = []
	for line in lines:
		line = line[:-1]
		array.append(list(line))
	for j in range(0, len(array)):
		for i in range(0, len(array[j])):
			if array[j][i].isdigit():
				array[j][i] = int(array[j][i])
	number = array[0]
	for j in range(1, len(array)):
		print_number(number)
		number.insert(0, "[")
		number.append(",")
		number += array[j]
		number.append("]")
		print("after addition: ", end="")
		print_number(number)
		reduce_number(number)
	magnitude = calculate_magnitude(ast.literal_eval(''.join(map(str, number))))
	print("--- Part One ---")
	print("Magnitude:", magnitude)

if __name__ == "__main__":
	main()
