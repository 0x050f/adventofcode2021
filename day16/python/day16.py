import math

char_to_binary = {
	"0": "0000",
	"1": "0001",
	"2": "0010",
	"3": "0011",
	"4": "0100",
	"5": "0101",
	"6": "0110",
	"7": "0111",
	"8": "1000",
	"9": "1001",
	"A": "1010",
	"B": "1011",
	"C": "1100",
	"D": "1101",
	"E": "1110",
	"F": "1111"
}

def decrypt_packet(array, index, recursive):
	version = 0
	padding = ""
	result = 0
	for n in range(0, recursive):
		padding += " "
	i = index
	if (len(array) - i > 6):
		binary = array[i] + array[i + 1] + array[i + 2]
		decimal = int(binary, 2)
#		print(padding + "Version:", decimal)
		version += decimal
		i += 3
		binary = array[i] + array[i + 1] + array[i + 2]
		decimal = int(binary, 2)
#		print(padding + "Type:", decimal)
		i += 3
		type_id = decimal
		if type_id == 4:
			binary = ""
			while array[i] != "0":
				i += 1
				for n in range(0, 4):
					binary += array[i + n]
				i += 4
			i += 1
			for n in range(0, 4):
				binary += array[i + n]
			i += 4
			decimal = int(binary, 2)
#			print(padding + "Value: " + str(decimal))
			result = decimal
		else:
			binary = array[i]
			decimal = int(binary, 2)
#			print(padding + "length type ID:", decimal)
			i += 1
			binary = ""
			packets_result = []
			if decimal == 0:
				for n in range(0, 15):
					binary += array[i + n]
				decimal = int(binary, 2)
#				print(padding + "total length in bits:", decimal)
#				print(padding + "{")
				i += 15
				n = i
				while i < n + decimal:
					i, v, r = decrypt_packet(array, i, recursive + 1);
					version += v
					packets_result.append(r)
			elif decimal == 1:
				for n in range(0, 11):
					binary += array[i + n]
				decimal = int(binary, 2)
#				print(padding + "number of sub-packets:", decimal)
#				print(padding + "{")
				i += 11
				for n in range(0, decimal):
					i, v, r = decrypt_packet(array, i, recursive + 1);
					version += v
					packets_result.append(r)
#			print(padding + "}")
			if type_id == 0:
				result = sum(packets_result)
			elif type_id == 1:
				result = math.prod(packets_result)
			elif type_id == 2:
				result = min(packets_result)
			elif type_id == 3:
				result = max(packets_result)
			elif type_id == 5:
				result = 1 if (packets_result[0] > packets_result[1]) else 0
			elif type_id == 6:
				result = 1 if (packets_result[0] < packets_result[1]) else 0
			elif type_id == 7:
				result = 1 if (packets_result[0] == packets_result[1]) else 0
	return i, version, result

def main():
	f = open('../input', 'r')
	line = f.readline();
	f.close()
	line = line[:-1]
	binary_line = ""
	for char in line:
		binary_line += char_to_binary[char];
	binary_line = list(binary_line)
	i, version, result = decrypt_packet(binary_line, 0, 0)
	print("--- Part One ---")
	print("Total version:", version)
	print("--- Part Two ---")
	print("Total result:", result)

if __name__ == "__main__":
	main()
