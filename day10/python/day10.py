def main():
	f = open('../input', 'r')
	lines = f.readlines()
	f.close()
	syntax_lines = []
	for line in lines:
		line = line[:-1]
		syntax_lines.append(list(line))
	score_syntax_error = 0
	scores = []
	n = 0
	for syntax_line in syntax_lines:
		pair = []
		i = 0
		while i < len(syntax_line):
			if syntax_line[i] == "(":
				pair.append(")")
			if syntax_line[i] == "[":
				pair.append("]")
			if syntax_line[i] == "{":
				pair.append("}")
			if syntax_line[i] == "<":
				pair.append(">")
			if syntax_line[i] == ")" or syntax_line[i] == "]" or syntax_line[i] == "}" or syntax_line[i] == ">":
				if pair[len(pair) - 1] != syntax_line[i]:
					break
				else:
					pair.pop()
			i += 1
		if i != len(syntax_line):
#			print("Expected", pair[len(pair) - 1], "got", syntax_line[i])
			if syntax_line[i] == ")":
				score_syntax_error += 3
			if syntax_line[i] == "]":
				score_syntax_error += 57
			if syntax_line[i] == "}":
				score_syntax_error += 1197
			if syntax_line[i] == ">":
				score_syntax_error += 25137
		else:
#			print(pair)
			scores.append(0)
			j = len(pair) - 1
			while j >= 0:
				scores[n] *= 5
				if pair[j] == ")":
					scores[n] += 1
				if pair[j] == "]":
					scores[n] += 2
				if pair[j] == "}":
					scores[n] += 3
				if pair[j] == ">":
					scores[n] += 4
				j -= 1
			n += 1
	scores = sorted(scores)
	print("--- Part One ---")
	print("Score:", score_syntax_error)
	print("--- Part Two ---")
	print("Score:", scores[int(len(scores) / 2)])

if __name__ == "__main__":
	main()
