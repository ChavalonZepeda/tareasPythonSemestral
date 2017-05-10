'''
Salvador Zepeda Pérez
'''

numerosString = input("Escriba los números separados por coma: ")
numerosConjunto = numerosString.replace("(", "").replace(")", "").split(",")
pares = 0
nones = 0
for n in numerosConjunto:
	if n.strip().isdigit():
		if int(n) % 2 == 0:
			pares = pares +1	
		else:
			nones = nones +1
print("%d Pares" % pares)
print("%d Nones" % nones)			
