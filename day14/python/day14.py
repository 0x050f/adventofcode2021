def main():
	f = open('../input', 'r')
	lines = f.readlines()
	f.close()
	template = []
	insertion = []
	for line in lines:
		line = line[:-1]
		if "->" in line:
			line = line.split(" -> ")
			line.append(line[1])
			one = list(line[0])[0]
			two = list(line[0])[1]
			line[0] = one
			line[1] = two
			insertion.append(line)
		elif line != "":
			template = list(line)
	template_bis = template.copy()
	print("Template:", template)
	step = 0
	while step < 10:
		copy = template.copy()
		i = 1
		for x in range(0, len(copy) - 1):
			for insert in insertion:
				if insert[0] == copy[x] and insert[1] == copy[x + 1]:
					template.insert(i, insert[2])
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
	#while step < 10:
	#	
	print(double)
#	print(insertion)

if __name__ == "__main__":
	main()
