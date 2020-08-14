class Pizeria:

	def __init__(self, pedidos=[], pizzas=[], clientes=[]):
		self.pedidos=pedidos
		self.pizzas=pizzas
		self.clientes=clientes

	def cargar_pedido(self):
		"""metodo para cargar los pedidos"""
		micliente = cargar_cliente()
		mipedido = Pedido(1, micliente, datetime.datetime.now(), datetime.datetime.now())
		while True:
			mipedido.agregar_detalle_pedido(self.pizzas)

		mipedido.calcular_precio_total()



	def cargar_pizza(self):
		"""metodo para cargar las pizzas"""
		pass

	def pedidos_por_periodo(self, fecha_ini, fecha_fin):
		"""metodo para listar los pedidos de un periodo determinado"""	
		pass	

	def cargar_cliente(self):
		"""metodo para cargar cliente"""
		cliente = Cliente("Juan Perez","3624452365", "25 de mayo 1221")
		return cliente




	while True:
		pedido = cargar_pedido()



