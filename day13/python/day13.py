def main():
	f = open('../input', 'r')
	lines = f.readlines()
	f.close()
	coord_max = [0, 0]
	coordinates = []
	fold_instr = []
	for line in lines:
		line = line[:-1]
		if ',' in line:
			line = list(map(int, line.split(",")))
			if coord_max[0] < line[0]:
				coord_max[0] = line[0]
			if coord_max[1] < line[1]:
				coord_max[1] = line[1]
			coordinates.append(line)
		elif line != '':
			line = line.replace("fold along ", "")
			line = line.split("=")
			line[1] = int(line[1])
			if line[0] == "x" and coord_max[0] < line[1] * 2:
				coord_max[0] = line[1] * 2
			if line[0] == "y" and coord_max[1] < line[1] * 2:
				coord_max[1] = line[1] * 2
			fold_instr.append(line)
	coord_max[0] = (int(coord_max[0] / 100) + 1) * 100
	coord_max[1] = (int(coord_max[1] / 100) + 1) * 100
	paper = [['.' for col in range(coord_max[0])] for row in range(coord_max[1])]
	for coord in coordinates:
		paper[coord[1]][coord[0]] = "#"
	for instr in fold_instr:
		count = 0
		if instr[0] == "x":
			for y in range(0, coord_max[1]):
				for x in range(instr[1] + 1, coord_max[0]):
					if paper[y][x] == "#":
						paper[y][instr[1] - (x - instr[1])] = "#"
					paper[y][x] = "X"
		elif instr[0] == "y":
			for y in range(instr[1] + 1, coord_max[1]):
				for x in range(0, coord_max[0]):
					if paper[y][x] == "#":
						paper[instr[1] - (y - instr[1])][x] = "#"
					paper[y][x] = "X"
		for col in paper:
			for dot in col:
				if dot == "#":
					count += 1
		print("hole:", count)
	for y in range(0, coord_max[1]):
		impr = 0
		for x in range(0, coord_max[0]):
			if paper[y][x] == "#":
				impr = 1
				print("#", end='')
			if paper[y][x] == ".":
				impr = 1
				print(".", end='')
		if impr == 1:
			print()

if __name__ == "__main__":
	main()
