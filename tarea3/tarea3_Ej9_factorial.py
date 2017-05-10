'''
Salvador Zepeda Pérez
'''

while(True):
	n = int(input("Factorial de: "))
	factorial = 1
	for i in range(1, n + 1):
		factorial = factorial * i
	print("Factorial de %d es %d" %(n, factorial))