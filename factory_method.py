from delivery_service import DeliveryService


print("Client isn't aware of different types delivery services.")

print("Only information needed from client is `frozen` boolean flag.")
print("\n")

print("Case 1: `frozen` boolean flag set to True")
delivery = DeliveryService(frozen=True)
delivery.delivery_operation()
print("\n")

print("Case 2: `frozen` boolean flag set to False")
delivery =DeliveryService(frozen=False)
delivery.delivery_operation()
