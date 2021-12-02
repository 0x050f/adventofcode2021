def part1():
	print("--- Part One ---")
	file = open('../input', 'r')
	depth = 0
	horizontal = 0
	lines = file.readlines()
	for line in lines:
		movement = line.split()[0]
		nb = int(line.split()[1])
		if movement == "forward":
			horizontal += nb
		elif movement == "up":
			depth -= nb
		elif movement == "down":
			depth += nb
	file.close()
	print("Depth: ", depth)
	print("Horizontal: ", horizontal)
	print("Result: ", depth * horizontal)

def part2():
	print("--- Part Two ---")
	file = open('../input', 'r')
	depth = 0
	horizontal = 0
	aim = 0
	lines = file.readlines()
	for line in lines:
		movement = line.split()[0]
		nb = int(line.split()[1])
		if movement == "forward":
			horizontal += nb
			depth += aim * nb
		elif movement == "up":
			aim -= nb
		elif movement == "down":
			aim += nb
	file.close()
	print("Depth: ", depth)
	print("Horizontal: ", horizontal)
	print("Result: ", depth * horizontal)


def main():
	part1()
	part2()

if __name__ == "__main__":
	main()
