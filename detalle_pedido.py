class Detalle_Pedido:

	def __init__(self, cant, pizza, subtotal=0):
		self.cant=cant
		self.pizza=pizza
		self.subtotal=subtotal


	def calcular_subtotal(self):
		"""metodo para calcular el subtotal del detalle en base a la cantidad y el precio de la piza
		1 - calcular la multiplicacion entre el precio de la pizza(self.pizza.calcular_precio() y cant) y asignarlo a self.subtotal"""
		pass	
