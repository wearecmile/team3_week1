from products_interface import FrozenProduct, NonFrozenProduct
from abc import ABC, abstractmethod


class DeliveryService():
    """
	    Delivery service which is extended by specific delivery method classes
	"""

    def __init__(self, frozen=False):
        self.frozen = frozen

    @abstractmethod
    def deliver_product(self):
        print("Product Delivered Successfully.")

	
    def factory_method(self):
        """
		Factory method returning object of the class based on the boolean flag
		"""
        if self.frozen:
            return FrozenDeliveryService()
        else:
            return NonFrozenDeliveryService()

    def delivery_operation(self):
		# calling factory to fetch the right class for delivery operation
        service = self.factory_method()

        service.deliver_product()


class FrozenDeliveryService(DeliveryService):
    
	def deliver_product(self):
		"""
		Instantiates FrozenProduct class object
		"""
		print("Client wants delivery of frozen product")
		FrozenProduct().operation()
		print("Delivering frozen product")
		


class NonFrozenDeliveryService(DeliveryService):

	def deliver_product(self):
		"""
		Instantiates NonFrozenProduct class object
		"""
		print("Client wants delivery of non frozen product")
		NonFrozenProduct().operation()
		print("Delivering non-frozen product")
