# -*- coding: utf-8 -*-

################################################
#	Agenda telefonica 
#	Salvador Zepeda Perez
#
################################################

contactos = []

print("Agenda telefonica:")

def listar():
	if len(contactos) > 0:
		i = 0
		for contacto in contactos:
			i = i + 1
			print("Contacto numero: ", i)
			print("Nombre: ", contacto.get("nombre"))
			print("Apellidos: ", contacto.get("apellidos"))
			print("Numero telefonico: ", contacto.get("numero"))
			print("Edad: ", contacto.get("edad"))
			print("Email: ", contacto.get("mail"))
	else:
		print("Lista de contactos vacia")
		raw_input("Enter para continuar...")
	init()
def eliminar():
	indice = int(raw_input("Escriba el numero del contacto que desea eliminar: "))
	indice = indice - 1
	if(indice) < len(contactos):
		del contactos[indice]
		print("Contacto numero %d borrado" % (indice + 1))
		raw_input("Enter para continuar...")
	else:
		print("El numero de contacto %d no existe" % (indice +1))
		raw_input("Enter para continuar...")
	init()
def agregar():
	indiceContacto = len(contactos) + 1
	print("Agregando el contacto numero %d" % (indiceContacto))
	nombre = raw_input("Escriba el nombre: ")
	apellidos = raw_input("Escriba los apellidos: ")
	numero = raw_input("Escriba el numero telefonico: ")
	edad = raw_input("Escriba la edad: ")
	mail = raw_input("Escriba el e-mail: ")
	nuevoContacto = {"nombre": nombre, "apellidos": apellidos, "numero": numero, "edad": edad, "mail": mail}
	contactos.append(nuevoContacto)
	print("Contacto numero %d agregado" % (indiceContacto))
	raw_input("Enter para continuar...")
	init()
def init():
	print("Acciones disponibles:")
	print("Listar (Ver todo los contactos disponibles)")
	print("Eliminar (Borrar de la lista algun contacto)")
	print("Agregar (Aregar algun contacto)")
	comando = raw_input("Que desea hacer? ")
	comandoValido = False
	if"listar" in comando.lower():
		comandoValido = True
		listar()
	if"eliminar" in comando.lower():
		comandoValido = True
		eliminar()
	if"agregar" in comando.lower():
		comandoValido = True
		agregar()
	if not comandoValido:
		print("Accion %s no reconocida" % (comando))
		raw_input("Enter para continuar...")
		init()


init()

