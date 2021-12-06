def main():
	f = open('../input', 'r')
	line = f.readline()
	f.close()
	line = line[:-1]
	numbers = line.split(",")
	numbers = list(map(int, numbers))
	cpy = numbers.copy()
	# Dumb list resolution (impossible to 256)
	n_days = 0
	while n_days < 80:
		cpy_numbers = numbers.copy()
		i = 0
		while i < len(cpy_numbers):
			if cpy_numbers[i] == 0:
				numbers[i] = 7
				numbers.append(8)
			numbers[i] -= 1
			i += 1
		n_days += 1
	print("Lanternfish after 80 days:", len(numbers))
	numbers = cpy
	nb_start = len(numbers)
	count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for nb in numbers:
		count[nb] += 1
	# uwu
	n_days = 0
	while n_days < 256:
		new_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
		i = 0
		while i < len(count):
			if i == 0:
				new_count[6] += count[0]
				new_count[8] += count[0]
			else:
				new_count[i - 1] += count[i]
			i += 1
		count = new_count
		n_days += 1
	print("Lanternfish after 256 days:", sum(count))

if __name__ == "__main__":
	main()
