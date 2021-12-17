import copy

def print_field(array):
	for y in array:
		for x in y:
			print(x, end="")
		print("")

def main():
	f = open('../input', 'r')
	line = f.readline()
	f.close()
	line = line[:-1]
	width = 200
	height = 200
	line = line[line.find('x'):].split(",")
	x_pos = list(map(int, list(line[0].split("=")[1].split(".."))))
	y_pos = list(map(int, list(line[1].split("=")[1].split(".."))))
	# 200 x - 400 y (200; -200)
	maxxx_y = 0
	for x in range(0, width):
		for y in range(0, height):
			velocity = [x, y]
#			print(velocity)
			probe = [0, 0]
			maxx_y = 0
			max_y = 0
			while probe[0] < width and probe[1] > -height:
				probe[0] += velocity[0]
				probe[1] += velocity[1]
				if probe[1] > max_y:
					max_y = probe[1]
				if velocity[0] > 0:
					velocity[0] -= 1
				elif velocity[0] < 0:
					velocity[0] += 1
				velocity[1] -= 1
				if probe[1] < height and probe[0] >= x_pos[0] and probe[0] <= x_pos[1] and probe[1] >= y_pos[0] and probe[1] <= y_pos[1]:
					maxx_y = max_y
			if maxxx_y < maxx_y:
				maxxx_y = maxx_y
	print(maxxx_y)
#	print(x_pos)
#	print(y_pos)
#	print(array)

if __name__ == "__main__":
	main()
