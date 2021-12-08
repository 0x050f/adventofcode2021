def count_common(str1, str2):
	str1 = list(str1)
	str2 = list(str2)
	count = 0
	for char1 in str1:
		for char2 in str2:
			if char1 == char2:
				count += 1
	return count

def main():
	f = open('../input', 'r')
	lines = f.readlines()
	f.close()
	digits = []
	for line in lines:
		line = line[:-1]
		line = line.split("|")
		ten_digits = line[0]
		four_digits = line[1]
		digits.append({"signal_pattern": list(filter(None, ten_digits.split(" "))), "output_values": list(filter(None, four_digits.split(" ")))})
	print("--- Part One ---")
	count_digits = 0
	for digit in digits:
		for d in digit["output_values"]:
			if len(d) < 5 or len(d) == 7:
				count_digits += 1
	print("Number of 1, 4, 7, 8:", count_digits)
	print("--- Part Two ---")
	i = 0
	output_values = []
	for digit in digits:
		output_values.append([])
		decoded_values = ["", "", "", "", "", "", "", "", "", ""]
		for d in digit["signal_pattern"]:
			if len(d) == 2:
				decoded_values[1] = d # 1
			if len(d) == 3:
				decoded_values[7] = d # 7
			if len(d) == 4:
				decoded_values[4] = d # 4
			if len(d) == 7:
				decoded_values[8] = d # 8
		for d in digit["signal_pattern"]:
			if len(d) == 5:#2, 3, 5
				if count_common(decoded_values[1], d) == 2:
					decoded_values[3] = d # 3
				elif count_common(decoded_values[4], d) == 3:
					decoded_values[5] = d # 5
				if count_common(decoded_values[4], d) == 2:
					decoded_values[2] = d # 2
		for d in digit["signal_pattern"]:
			if len(d) == 6:#0, 6, 9
				if count_common(decoded_values[4], d) == 4:
					decoded_values[9] = d # 9
				if count_common(decoded_values[1], d) == 1:
					decoded_values[6] = d # 6
				elif count_common(decoded_values[5], d) == 4:
					decoded_values[0] = d # 0
		for d in digit["output_values"]:
			n = 0
			for decode in decoded_values:
				if sorted(decode) == sorted(d):
					output_values[i].append(n)
				n += 1
		i += 1
	sum = 0
	for digits in output_values:
		n = digits[0] * 1000 + digits[1] * 100 + digits[2] * 10 + digits[3]
		sum += n
	print("Sum of all numbers:", sum)

if __name__ == "__main__":
	main()
