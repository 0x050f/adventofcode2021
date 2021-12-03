def part1():
	print("--- Part One ---")
	file = open('../input', 'r')
	bit_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	count = 0

	lines = file.readlines()
	for line in lines:
		binary = line[:-1]
		for i in range(0, 12):
			if binary[i] == '1':
				bit_count[i] += 1
		count += 1
	gamma = "000000000000"
	epsilon = "000000000000"
	for i in range(0, 12):
		if count - bit_count[i] >= count / 2:
			gamma_list = list(gamma)
			gamma_list[i] = "1"
			gamma = "".join(gamma_list)
		else:
			epsilon_list = list(epsilon)
			epsilon_list[i] = "1"
			epsilon = "".join(epsilon_list)
	print("Gamma: ", int(gamma,2))
	print("Epsilon: ", int(epsilon,2))
	print("Gamma * Epsilon = ", int(gamma,2) * int(epsilon,2))

	file.close()

def part2():
	print("--- Part Two ---")
	file = open('../input', 'r')
	bit_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	oxygen = []
	co2 = []

	lines = file.readlines()
	for line in lines:
		oxygen.append(line[:-1])
		co2.append(line[:-1])
	i = 0
	while len(oxygen) > 1:
		count = 0
		total = 0
		for binary in oxygen:
			binary_list = list(binary)
			if binary_list[i] == "1":
				count += 1
			total += 1
		if count >= total / 2:
			char = "1"
		else:
			char = "0"
		cpy_oxygen = oxygen.copy()
		for binary in oxygen:
			binary_list = list(binary)
			if binary_list[i] != char:
				cpy_oxygen.remove(binary)
		oxygen = cpy_oxygen
		i += 1
	i = 0
	while len(co2) > 1:
		count = 0
		total = 0
		for binary in co2:
			binary_list = list(binary)
			if binary_list[i] == "1":
				count += 1
			total += 1
		if count >= total / 2:
			char = "0"
		else:
			char = "1"
		cpy_co2 = co2.copy()
		for binary in co2:
			binary_list = list(binary)
			if binary_list[i] != char:
				cpy_co2.remove(binary)
		co2 = cpy_co2
		i += 1
	print("Oxygen: ", int(oxygen[0],2))
	print("C02: ", int(co2[0],2))
	print("Oxygen * C02 = ", int(oxygen[0],2) * int(co2[0],2))
	file.close()

def main():
	part1()
	part2()

if __name__ == "__main__":
	main()
