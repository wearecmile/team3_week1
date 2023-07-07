from delivery_service import DeliveryService

frozen = input("Are you want frozen products? True or False?  ")

if frozen.lower() == "true":
    boolean_value = True
else:
    boolean_value = False


print("Client isn't aware of different types delivery services.")

print("Only information needed from client is `frozen` boolean flag.")
print("\n")

delivery = DeliveryService(frozen=boolean_value)
delivery.delivery_operation()
print("\n")
