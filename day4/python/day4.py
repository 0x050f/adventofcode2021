def get_boards(filename):
	boards = []
	i = -1
	lines = filename.readlines()
	for line in lines:
		if line == "\n":
			boards.append([])
			i += 1
			boards[i] = []
		else:
			line = line[:-1]
			numbers = line.split(" ")
			numbers = list(filter(None, numbers))
			numbers = list(map(int, numbers))
			boards[i].append(numbers)
	return boards

def has_winning_state(nb_pick, board):
	side_nb = 5
	marker = [[0 for col in range(side_nb)] for row in range(side_nb)]
	for nb in nb_pick:
		for i in range(side_nb):
			for j in range(side_nb):
				if board[i][j] == nb:
					marker[i][j] = 1
	for i in range(side_nb):
		count = 0
		for j in range(side_nb):
			if marker[i][j] == 1:
				count += 1
			if count == 5:
				return True
	for j in range(side_nb):
		count = 0
		for i in range(side_nb):
			if marker[i][j] == 1:
				count += 1
			if count == 5:
				return True
	return False

def find_winning_board(nb_pick, boards):

	result = []
	index_pick = 0
	tmp = []
	for nb in nb_pick:
		tmp.append(nb)
		cpy_boards = boards
		for board in cpy_boards:
			if has_winning_state(tmp, board):
				result.append({"index": index_pick, "board": board})
				boards.remove(board)
		boards = cpy_boards
		index_pick += 1
	return result

def get_score(nb_pick, board):
	total = 0
	for line in board:
		for nb in line:
			if nb not in nb_pick:
				total += nb
	return total * nb_pick[len(nb_pick) - 1]

def main():
	f = open ('../input', 'r')

	nb_pick = f.readline()
	nb_pick = nb_pick.split(",")
	nb_pick = list(map(int, nb_pick))
	boards = get_boards(f)
	result = find_winning_board(nb_pick, boards)
	print("--- Part One ---")
	print("Result:", get_score(nb_pick[:result[0]["index"] + 1], result[0]["board"]))
	print("--- Part Two ---")
	print("Result:", get_score(nb_pick[:result[len(result) - 1]["index"] + 1], result[len(result) - 1]["board"]))
	f.close()

if __name__ == "__main__":
	main()
