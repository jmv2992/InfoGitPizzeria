import datetime

class Pedido:

	def __init__(self,id_pedido, cliente, fecha_hora, hora_est_ent, detalle_pedido=[], total=0):
		self.id_pedido=id_pedido
		self.cliente=cliente
		self.fecha_hora=fecha_hora
		self.hora_est_ent=hora_est_ent
		self.detalle_pedido=detalle_pedido
		self.total=total

	def calcular_precio_total(self):
		"""calcular el precio total del pedido"""
		suma=0
		for linea in detalle_pedido:
			suma+= linea.subtotal
		self.total=suma

	

	def agregar_detalle_pedido(self, lista_pizzas):
		"""metodo para agragar una linea del pedido
		1 - crear instancia de Detalle Pedido, preguntando cual es la pizza, que desea(listar las pizas que hay)
		2- llamar al metodo calcular precio de la piza
		2 - agregarlo a self.detalle_pedido
		"""
		eldetalle= Detalle_Pedido(10, lista_pizzas[0])
		eldetalle.calcular_subtotal()

		pass	
