def main():
	file = open('input.txt', 'r')
	data = file.readlines();


	for i in range(len(data)):
		data[i]= data[i].split()

	horizontal = 0
	depth = 0

	for a in data:
		if(a[0] == "forward"):
			horizontal += float(a[1])
		elif(a[0] == "up"):
			depth -= float(a[1])
		elif(a[0] == "down"):
			depth += float(a[1])

	print(horizontal * depth)

main() 