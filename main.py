from food_establishment import *

print("Welcome to DelFood! \n")

while True:

    print("1. Carly's Calzones \n"
          "2. Berbos \n"
          "3. Quit \n")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        establishment = Establish1()
        establishmentContext = EstablishmentContext(establishment)
        establishmentContext.performEstablishment()

    elif ch == 2:
        establishment = Establish2()
        establishmentContext = EstablishmentContext(establishment)
        establishmentContext.performEstablishment()

    elif ch == 3:
        print("Succes!")
        break

    else:
        print("Error")