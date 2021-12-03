def main():
	file = open('input.txt', 'r')
	data = file.readlines()


	gamma_rate = ''
	epsilon_rate = ''

	length = len(data[0]) -1

	for i in range(length):
		zeros = 0
		ones = 0
		for j in range(len(data)):
			if(data[j][i] == '0' ):
				zeros += 1
			else:
				ones += 1
		if(zeros > ones):
			gamma_rate += '0'
			epsilon_rate += '1'
		else:
			gamma_rate += '1'
			epsilon_rate += '0'

			
	print(gamma_rate)
	print('**********************************')
	print(epsilon_rate)
	print('**********************************')
	print(844 * 3251)


main()