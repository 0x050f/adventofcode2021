def part1():
	print("--- Part One ---")
	file = open('../input', 'r')
	prev_value = file.readline()
	value = file.readline()
	lines = file.readlines()
	value = int(value[:-1])
	prev_value = int(prev_value[:-1])
	count = 0
	for line in lines:
#		print(prev_value, " -> ", value)
		if prev_value < value:
			count += 1
		prev_value = value
		value = line
		value = int(value[:-1])
	if prev_value < value:
		count += 1
	file.close()
	print("Result: ", count, " 'increased'")

def part2():
	print("--- Part Two ---")
	file = open('../input', 'r')
	window1 = [int(file.readline()[:-1]), int(file.readline()[:-1]), int(file.readline()[:-1])]
	window2 = [window1[1], window1[2], int(file.readline()[:-1])]
	lines = file.readlines()
	count = 0
	for line in lines:
		if sum(window1) < sum(window2):
			count += 1
		window1 = [window2[0], window2[1], window2[2]]
		window2 = [window2[1], window2[2], int(line[:-1])]
	if sum(window1) < sum(window2):
		count += 1
	print("Result: ", count, " 'increased'")
	file.close()

def main():
	part1()
	part2()

if __name__ == "__main__":
	main()
