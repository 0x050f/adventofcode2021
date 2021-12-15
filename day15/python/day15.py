import heapq

def find(array, scale):
	todo = []
	height, width = len(array), len(array[0])
	exit = (scale * height - 1, scale * width - 1)
	heapq.heappush(todo,(0,0,0))
	seen = set()
	seen.add((0,0))
	while todo:
		cost, r, c = heapq.heappop(todo)
		if (r, c) == exit:
			return cost
		for dr in range(-1, 2):
			for dc in range(-1, 2):
				if abs(dr + dc) == 1:
					nr, nc = r + dr, c + dc
					if (nr,nc) not in seen and 0 <= nr < scale * height and 0 <= nc < scale * width:
						x, y = nr // height, nc // width
						new_val = array[nr - x * height][nc - y * width] + x + y
						if new_val > 9:
							new_val -= 9
						seen.add((nr, nc))
						heapq.heappush(todo,(cost + new_val, nr, nc))

def main():
	f = open('../input', 'r')
	lines = f.readlines()
	f.close()
	array = []
	for line in lines:
		line = line[:-1]
		array.append(list(map(int, list(line))))
	print("--- Part One ---")
	print(find(array.copy(), 1))
	print("--- Part Two ---")
	print(find(array.copy(), 5))

if __name__ == "__main__":
	main()
