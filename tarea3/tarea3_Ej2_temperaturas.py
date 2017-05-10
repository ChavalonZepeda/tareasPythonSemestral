'''
Salvador Zepeda Pérez
'''

while(True):
	celcius = 0
	farenheit = 0
	grados = input("Ingrese una temperatura: Ej: 23C, 34F, 123c o 45f: ")
	if grados == "":
		break
	elif "c" in grados or "C" in grados:
		grados = float(grados.replace("c", "").replace("C", "").strip())
		print("%d °C = %d °F" % (grados, (9*grados) /5 + 32))
	elif "f" in grados or "F" in grados:
		grados = float(grados.replace("f", "").replace("F", "").strip())
		print("%d °F = %d °C" % (grados, (5*grados -160) /9))
	input("Enter para continuar...")