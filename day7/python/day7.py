def main():
	f = open('../input', 'r')
	line = f.readline()
	f.close()
	line = line[:-1]
	numbers = line.split(",")
	numbers = list(map(int, numbers))
	n_max = max(numbers)
	n_min = min(numbers)
	c_fuel = 0
	result = 0
	min_c_fuel = 999999999999999999999999
	for i in range(n_min, n_max):
		c_fuel = 0
		for nb in numbers:
			c_fuel += abs(nb - i)
		if c_fuel < min_c_fuel:
			result = i
			min_c_fuel = c_fuel
	print("--- Part One ---")
	print("Result: ", result)
	print("Fuel: ", min_c_fuel)
	c_fuel = 0
	result = 0
	min_c_fuel = 999999999999999999999999
	for i in range(n_min, n_max):
		c_fuel = 0
		for nb in numbers:
			n = abs(nb - i)
			c_fuel += int((n * (n + 1)) / 2)
		if c_fuel < min_c_fuel:
			result = i
			min_c_fuel = c_fuel
	print("--- Part Two ---")
	print("Result: ", result)
	print("Fuel: ", min_c_fuel)

if __name__ == "__main__":
	main()
