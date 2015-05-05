import Gateway

gateway = Gateway.Gateway()

print("Doing Math")
print(gateway.getMathy() + gateway.getMathy())

print("")

print("Getting some Words")
print(gateway.getWordy())

print("")

print("Is it true?")
if(gateway.getTruthy() == True):
	print("Yes")
else:
	print("No")

print("")

print("What does the data class do?")
print(gateway.getFunctionality())