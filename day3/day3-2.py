def main():
	file = open('input.txt', 'r')
	data = file.readlines()

	length = len(data[0]) - 1

	oxygen = [None] * len(data)
	co2 = [None] * len(data)

	for i in range(len(data)):
		oxygen[i] = data[i]
		co2[i] = data[i]

	while(len(oxygen) > 1):
		for i in range(length):
			zeros = 0
			ones = 0
			for j in range(len(oxygen)):
				if(oxygen[j][i] == '0'):
					zeros += 1
				else:
					ones += 1
			if(zeros > ones):
				oxygen = [x for x in oxygen if x[i] == '0']
			else:
				oxygen = [x for x in oxygen if x[i] == '1']
			
	while(len(co2) > 1):
		for i in range(length):
			zeros = 0
			ones = 0
			for j in range(len(co2)):
				if(co2[j][i] == '0'):
					zeros += 1
				else:
					ones += 1
			if(zeros > ones):
				co2 = [x for x in co2 if x[i] == '1']
			else:
				co2 = [x for x in co2 if x[i] == '0']

			if(len(co2) == 1):
				break

	print(oxygen)
	print(co2)
	
	print(1981*3371)

	#011110111101  1981
	#110100101011  3371

main()