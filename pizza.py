class Pizza:

	mediana=0.1
	grande=0.15
	piedra=0.05
	molde=0.03
	parrilla=0.03

	def __init__(self, nombre, ingredientes, tipo, tamanio, precio_base):
		self.nombre=nombre
		self.ingredientes=ingredientes
		self.tipo=tipo
		self.tamanio=tamanio
		self.precio_base=precio_base

	def calcular_precio(self):
		"""metodo para calcular el precio de la piza segun el tipo y el tamanio:
		1 - Preguntar que tipo y que tamanio desea
		2 - retornar el precio de la piza"""
		pass

