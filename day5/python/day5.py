def main():
	f = open ('../input', 'r')
	data = []
	lines = f.readlines()
	for line in lines:
		line = line[:-1]
		tmp = line.split(" -> ")
		t_from = tmp[0].split(",")
		t_from = list(map(int, t_from))
		t_to = tmp[1].split(",")
		t_to = list(map(int, t_to))
		data.append({"from": {"x": t_from[0], "y": t_from[1]}, "to": {"x": t_to[0], "y": t_to[1]}})
	marker = [[0 for col in range(1000)] for row in range(1000)]
	for el in data:
		if el["from"]["x"] == el["to"]["x"]:
			x = el["from"]["x"]
			y = el["from"]["y"]
			while True:
				marker[y][x] += 1
				if y == el["to"]["y"]:
					break
				if el["from"]["y"] < el["to"]["y"]:
					y += 1
				else:
					y -= 1
		elif el["from"]["y"] == el["to"]["y"]:
			y = el["from"]["y"]
			x = el["from"]["x"]
			while True:
				marker[y][x] += 1
				if x == el["to"]["x"]:
					break
				if el["from"]["x"] < el["to"]["x"]:
					x += 1
				else:
					x -= 1
		else:
			x = el["from"]["x"]
			y = el["from"]["y"]
			while True:
				marker[y][x] += 1
				if x == el["to"]["x"] or y == el["to"]["y"]:
					break
				if el["from"]["x"] < el["to"]["x"]:
					x += 1
				else:
					x -= 1
				if el["from"]["y"] < el["to"]["y"]:
					y += 1
				else:
					y -= 1
	count = 0
	for line in marker:
		for mark in line:
			if mark > 1:
				count += 1
	print("Count: ", count)
	f.close()

if __name__ == "__main__":
	main()
