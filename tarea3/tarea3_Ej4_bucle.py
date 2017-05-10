'''
Salvador Zepeda Pérez
'''

for a in range(0, 2):
	print("*")
	for b in range(0, 2):
		if a==0:
			print(">>")
		for c in range(0, 2):
			if a+b==0:
				print("***")
			for d in range(0, 3):
				if a+b+c==0:
					print(">>>>>>>>")