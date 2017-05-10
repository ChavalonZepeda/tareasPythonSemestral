'''
Salvador Zepeda Pérez
'''

import random
numeroAleatorio = random.randint(1, 10)
numeroConjetura = -1
while numeroConjetura != numeroAleatorio:
	numeroConjetura = int(input("Adivina un numero de 1 al 10: "))
print("bien adivinado!!!")