def print_2darray(arr_2d):
	for i in arr_2d:
		for j in i:
			print(j, end=" ")
		print()

def flash_octopus(octopus, i, j):
	flashes = 0
	if octopus[i][j] >= 9:
		flashes += 1
		octopus[i][j] = 0
		if i != 0:
			flashes += flash_octopus(octopus, i - 1, j)
			if j != 0:
				flashes += flash_octopus(octopus, i - 1, j - 1)
			if j != len(octopus[i]) - 1:
				flashes += flash_octopus(octopus, i - 1, j + 1)
		if j != 0:
			flashes += flash_octopus(octopus, i, j - 1)
		if i != len(octopus) - 1:
			flashes += flash_octopus(octopus, i + 1, j)
			if j != 0:
				flashes += flash_octopus(octopus, i + 1, j - 1)
		if j != len(octopus[i]) - 1:
			flashes += flash_octopus(octopus, i, j + 1)
			if i != len(octopus) - 1:
				flashes += flash_octopus(octopus, i + 1, j + 1)
	elif octopus[i][j] != 0:
		octopus[i][j] += 1
	return flashes

def main():
	f = open('../input', 'r')
	lines = f.readlines()
	f.close()
	octopus = []
	for line in lines:
		line = line[:-1]
		octopus.append(list(map(int, list(line))))
	step = 0
	first = 0
	flashes = 0
	while first == 0:
		i = 0
		while i < len(octopus):
			j = 0
			while j < len(octopus[i]):
				octopus[i][j] += 1
				j += 1
			i += 1
		i = 0
		while i < len(octopus):
			j = 0
			while j < len(octopus[i]):
				if octopus[i][j] == 10 and step < 100:
					flashes += flash_octopus(octopus, i, j)
				elif octopus[i][j] == 10:
					flash_octopus(octopus, i, j)
				j += 1
			i += 1
		n = octopus[0][0]
		i = 0
		while i < len(octopus):
			j = 0
			while j < len(octopus[i]):
				if octopus[i][j] != n:
					break
				j += 1
			if j != len(octopus[i]) and octopus[i][j] != n:
				break
			i += 1
		if i == len(octopus):
			first = step
		step += 1
	print("--- Part One ---")
	print("Flashes:" , flashes)
	print("--- Part Two ---")
	print("Synchronisation:", step)

if __name__ == "__main__":
	main()
