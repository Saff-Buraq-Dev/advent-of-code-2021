def main():
	file = open('input.txt', 'r')
	tab = file.readlines()
	counter = 0
	for i in range(len(tab)-3):
		if int(tab[i+1])+int(tab[i+2])+int(tab[i+3]) > int(tab[i])+int(tab[i+1])+int(tab[i+2]):
			counter += 1
	
	print(counter)
	
main()