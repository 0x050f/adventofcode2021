def find_all_paths_part1(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return [path]
	paths = []
	for node in graph[start]:
		if node not in path or node.isupper():
			newpaths = find_all_paths_part1(graph, node, end, path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths

def find_all_paths_part2(graph, start, end, path=[], both = 0):
	path = path + [start]
	if start == end:
		return [path]
	paths = []
	for node in graph[start]:
#		print(path)
		if (node.isupper() or (node != "start" and (path.count(node) == 0 or (both == 0 and path.count(node) == 1)))):
			if node.islower() and path.count(node) == 1:
				newpaths = find_all_paths_part2(graph, node, end, path, 1)
			else:
				newpaths = find_all_paths_part2(graph, node, end, path, both)
			for newpath in newpaths:
				paths.append(newpath)
	return paths

def main():
	f = open('../input', 'r')
	lines = f.readlines()
	f.close()
	small_caves = []
	graph = {}
	for line in lines:
		line = line[:-1]
		line = line.split("-")
		if line[0].islower() and line[0] not in small_caves:
			small_caves.append(line[0])
		elif line[1].islower() and line[1] not in small_caves:
			small_caves.append(line[1])
		if line[0] not in graph:
			graph[line[0]] = []
		graph[line[0]].append(line[1])
		if line[1] not in graph:
			graph[line[1]] = []
		graph[line[1]].append(line[0])
	paths = find_all_paths_part1(graph, "start", "end")
	print("--- Part One ---")
	print("Nb:", len(paths))
	paths = find_all_paths_part2(graph, "start", "end")
	print("--- Part Two ---")
	print("Nb:", len(paths))

if __name__ == "__main__":
	main()
