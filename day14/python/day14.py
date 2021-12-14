def main():
	f = open('../input', 'r')
	lines = f.readlines()
	f.close()
	template = []
	insertion = {}
	for line in lines:
		line = line[:-1]
		if "->" in line:
			line = line.split(" -> ")
			insertion[line[0]] = line[1]
		elif line != "":
			template = list(line)
	template_bis = template.copy()
	print("Template:", template)
	step = 0
	while step < 10:
		copy = template.copy()
		i = 1
		for x in range(0, len(copy) - 1):
			for key in insertion:
				if list(key)[0] == copy[x] and list(key)[1] == copy[x + 1]:
					template.insert(i, insertion[key])
					i += 1
			i += 1
		step += 1
		print("After step", step, "- size:", len(template))
	count_el = {}
	for el in template:
		if el not in count_el:
			count_el[el] = 1
		else:
			count_el[el] += 1
	min_el = 999999
	max_el = 0
	for el, nb in count_el.items():
		if nb < min_el:
			min_el = nb
		if nb > max_el:
			max_el = nb
	print("--- Part One ---")
	print("Result:", max_el - min_el)
	template = template_bis
	print("Template:", template)
	double = {}
	for x in range(0, len(template) - 1):
		if template[x] + template[x + 1] not in double:
			double[template[x] + template[x + 1]] = 1
		else:
			double[template[x] + template[x + 1]] += 1
	step = 0
	while step < 40:
		new = {}
		for key in double:
			if list(key)[0] + insertion[key] in new:
				new[list(key)[0] + insertion[key]] += double[key]
			else:
				new[list(key)[0] + insertion[key]] = double[key]
			if insertion[key] + list(key)[1] in new:
				new[insertion[key] + list(key)[1]] += double[key]
			else:
				new[insertion[key] + list(key)[1]] = double[key]
		double = new
		step += 1
	letters = {}
	for key in double:
		if list(key)[0] in letters:
			letters[list(key)[0]] += double[key]
		else:
			letters[list(key)[0]] = double[key]
		if list(key)[1] in letters:
			letters[list(key)[1]] += double[key]
		else:
			letters[list(key)[1]] = double[key]
	for letter in letters:
		letters[letter] /= 2
	min_el = 99999999999999999999999
	max_el = 0
	for letter in letters:
		if letters[letter] < min_el:
			min_el = letters[letter]
		if letters[letter] > max_el:
			max_el = letters[letter]
	print("--- Part Two ---")
	print("Result:", int(max_el - min_el))

if __name__ == "__main__":
	main()
