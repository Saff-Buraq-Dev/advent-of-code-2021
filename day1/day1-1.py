def main():
	file = open('input1.txt', 'r')
	tab = file.readlines()
	counter = 0
	for i in range(len(tab)-1):
		if int(tab[i+1]) > int(tab[i]):
			counter += 1
	
	print(counter)

main()