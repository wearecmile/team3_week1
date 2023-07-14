from delivery_service import DeliveryService

frozen = input("Are you want frozen products? True or False?  ")

if frozen.lower() == "true":
    boolean_value = True
elif frozen.lower() == "false":
    boolean_value = False
else:
    raise ValueError("Invalid input. Please enter 'True' or 'False'.")



print("Client isn't aware of different types delivery services.")

print("Only information needed from client is `frozen` boolean flag.")
print("\n")

delivery = DeliveryService(frozen=boolean_value)
delivery.delivery_operation()
print("\n")
