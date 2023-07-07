from abc import ABC, abstractmethod


class Product(ABC):
	"""
	Interface for product types
	"""

	@abstractmethod
	def operation(self):
		pass

class FrozenProduct(Product):
	"""
	Concrete implimentation of the interface Product
	"""

	def operation(self):
		print("This is a frozen product")

class NonFrozenProduct(Product):
	"""
	Concrete implimentation of the interface Product
	"""

	def operation(self):
		print("This is a non-frozen product")
