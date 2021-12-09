def count_bassin_size(height_map, x, y):
	count = 0

	if height_map[y][x] != 9:
		count += 1
		height_map[y][x] = 9
		if y != 0 and height_map[y - 1][x] != 9:
			count += count_bassin_size(height_map, x, y - 1)
		if y != (len(height_map) - 1) and height_map[y + 1][x] != 9:
			count += count_bassin_size(height_map, x, y + 1)
		if x != 0 and height_map[y][x - 1] != 9:
			count += count_bassin_size(height_map, x - 1, y)
		if x != (len(height_map[0]) - 1) and height_map[y][x + 1] != 9:
			count += count_bassin_size(height_map, x + 1, y)
	return count

def main():
	f = open('../input', 'r')
	lines = f.readlines()
	f.close()
	height_map = []
	for line in lines:
		line = line[:-1]
		height_map.append(list(map(int, list(line))))
	low_points = []
	lowest_cave = [0, 0, 0]
	for y in range(0, len(height_map)):
		for x in range(0, len(height_map[0])):
			if (y == 0 or height_map[y - 1][x] > height_map[y][x]) and \
(y == (len(height_map) - 1) or height_map[y + 1][x] > height_map[y][x]) and \
(x == 0 or height_map[y][x - 1] > height_map[y][x]) and \
(x == (len(height_map[0]) - 1) or height_map[y][x + 1] > height_map[y][x]):
				low_points.append(height_map[y][x])
	for y in range(0, len(height_map)):
		for x in range(0, len(height_map[0])):
			if (y == 0 or height_map[y - 1][x] > height_map[y][x]) and \
(y == (len(height_map) - 1) or height_map[y + 1][x] > height_map[y][x]) and \
(x == 0 or height_map[y][x - 1] > height_map[y][x]) and \
(x == (len(height_map[0]) - 1) or height_map[y][x + 1] > height_map[y][x]):
				count = count_bassin_size(height_map, x, y)
				if count > 0:
					if min(lowest_cave) < count:
						lowest = min(lowest_cave)
						n = 0
						for n in range(0, 3):
							if lowest_cave[n] == lowest:
								lowest_cave[n] = count
								break
	print("--- Part One ---")
	print("Sum of risk: ", sum(low_points) + len(low_points))
	print("--- Part Two ---")
	print("Result: ", lowest_cave[0] * lowest_cave[1] * lowest_cave[2])


if __name__ == "__main__":
	main()
