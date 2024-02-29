from PaymentService import *
from os import system, name
from abc import ABC, abstractmethod

class Establishes(ABC):

    @abstractmethod
    def Display_Order(self):
        pass

    @abstractmethod
    def Toppings(self):
        pass

    @abstractmethod
    def mainBody(self):
        pass

class Establish1(Establishes):

    Order_Choice = []
    Order_Cost = []
    Order_Toppings = []
    Order_Toppings_Cost = []

    def Display_Order(self):

        system('cls')

        Items_Total = 0
        Toppings_Total = 0
        Item_Number = 0
        Topping_Number = 0

        print("\nItems in cart:")

        for x in self.Order_Choice:

            Topping_Number = 0
            print("\n---------------------------------------------------------------")
            print("ITEM: ", (Item_Number + 1), "\b.", x, "  Cost:", self.Order_Cost[(Item_Number)])
            Items_Total = Items_Total + self.Order_Cost[Item_Number]

            NumToppings = len(self.Order_Toppings[Item_Number])
            print("\n         ", "There are", NumToppings, "toppings for this item:\n")

            for y in self.Order_Toppings[Item_Number]:
                print("         ", (Topping_Number + 1), "\b.", y, "  Cost:",
                      self.Order_Toppings_Cost[Item_Number][Topping_Number])
                Toppings_Total = Toppings_Total + self.Order_Toppings_Cost[Item_Number][Topping_Number]
                Topping_Number = Topping_Number + 1

            Item_Number = Item_Number + 1

        Total_Cost = Items_Total + Toppings_Total

        print("\n---------------------------------------------------------------")
        print("\nRunning Item Total:", "$", Items_Total)
        print("Running Toppings Total:", "$", Toppings_Total)
        print("Total Cost:", "$", Total_Cost)

        print("\n 1. Pay by Credit Card \n"
              "2. Pay by Debit Card \n"
              "3. Pay by PayPal \n")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            cardNumber = input("Enter card number: ")
            expiracyDate = input("Enter expiracy date: ")
            cvv = input("Enter cvv: ")
            creditCard = CreditCard(cardNumber, expiracyDate, cvv)
            payment = PaymentContext(creditCard)
            payment.perform_payment(Total_Cost)

        elif choice == 2:
            cardNumber = input("Enter card number: ")
            expiracyDate = input("Enter expiracy date: ")
            cvv = input("Enter cvv: ")
            debitCard = DebitCard(cardNumber, expiracyDate, cvv)
            payment = PaymentContext(debitCard)
            payment.perform_payment(Total_Cost)

        else:
            email = input("Enter email: ")
            password = input("Enter password: ")
            paypal = PayPal(email, password)
            payment = PaymentContext(paypal)
            payment.perform_payment(Total_Cost)

        ContinueIT = input("\nENTER anything to continue:")
        ContinueIT = " "

    def Toppings(self):

        Toppings_Complete = "FALSE"
        Current_Toppings_Selection = []
        Current_Toppings_Cost = []

        while Toppings_Complete != "TRUE":

            print("\n--------------Toppings Menu---------------")
            print("|                                        |")
            print("|       (E)xtra Cheese         ($1)      |")
            print("|       (X)tra Sauce           ($0)      |")
            print("|       (B)lasphemous Pinapple ($5)      |")
            print("|       (T)omatoes             ($1)      |")
            print("|       (O)lives               ($1)      |")
            print("|       (G)reen Peppers        ($1)      |")
            print("|       (J)alapeños            ($1)      |")
            print("|       (P)epperoni            ($2)      |")
            print("|       (S)ausage              ($2)      |")
            print("|       (H)am                  ($2)      |")
            print("|       (C)hicken              ($2)      |")
            print("|       (A)nchovies            ($2)      |")
            print("|       (Q)uit [Finished Toppings]       |")
            print("|                                        |")
            print("------------------------------------------", "\n")

            CHOICE = input("Your choice: ")
            CHOICE = CHOICE.upper()

            if CHOICE == 'E':
                Current_Toppings_Selection.append("Extra Cheese")
                Current_Toppings_Cost.append(1)
                print("Extra Cheese.")

            elif CHOICE == 'X':
                Current_Toppings_Selection.append("EXTRA Sauce")
                Current_Toppings_Cost.append(0)
                print("EXTRA Sauce")

            elif CHOICE == 'B':
                Current_Toppings_Selection.append("Blasphemous Pinapple")
                Current_Toppings_Cost.append(5)
                print("Blasphemous Pinapple.")

            elif CHOICE == 'T':
                Current_Toppings_Selection.append("Tomatoes")
                Current_Toppings_Cost.append(1)
                print("Tomatoes.")

            elif CHOICE == 'O':
                Current_Toppings_Selection.append("Olives")
                Current_Toppings_Cost.append(1)
                print("Olives.")

            elif CHOICE == 'G':
                Current_Toppings_Selection.append("Green Peppers")
                Current_Toppings_Cost.append(1)
                print("Green Peppers")

            elif CHOICE == 'J':
                Current_Toppings_Selection.append("Jalapeños")
                Current_Toppings_Cost.append(1)
                print("Jalapeños.")

            elif CHOICE == 'P':
                Current_Toppings_Selection.append("Pepperoni")
                Current_Toppings_Cost.append(2)
                print("Pepperoni.")

            elif CHOICE == 'S':
                Current_Toppings_Selection.append("Sausage")
                Current_Toppings_Cost.append(2)
                print("Sausage.")

            elif CHOICE == 'H':
                Current_Toppings_Selection.append("Ham")
                Current_Toppings_Cost.append(2)
                print("Ham")

            elif CHOICE == 'C':
                Current_Toppings_Selection.append("Chicken")
                Current_Toppings_Cost.append(2)
                print("Chicken.")

            elif CHOICE == 'A':
                Current_Toppings_Selection.append("Anchovies")
                Current_Toppings_Cost.append(2)
                print("Anchovies")

            elif CHOICE == 'Q':
                print("Toppings complete.")

                if len(Current_Toppings_Selection) < 1:
                    print("No toppings selected for this item.")
                    Current_Toppings_Selection.append("No toppings selected for this item.")
                    Current_Toppings_Cost.append(0)

                Toppings_Complete = "TRUE"

            else:
                print("That choice was invalid. Please choose again.")

        self.Order_Toppings.append(Current_Toppings_Selection)
        self.Order_Toppings_Cost.append(Current_Toppings_Cost)

    def mainBody(self):

        system('cls')

        Order_Complete = "FALSE"

        print("\nWelcome to Carly's Calzones!", "\n")

        while Order_Complete != "TRUE":

            print("\n----------Product Menu------------")
            print("|                                   |")
            print("|       (S)mall Pizza               |")
            print("|       (M)edium Pizza              |")
            print("|       (L)arge Pizza               |")
            print("|       (C)olzones                  |")
            print("|       (B)read Sticks              |")
            print("|       (Q)uit (complete order)     |")
            print("|                                   |")
            print("-------------------------------------", "\n")

            CHOICE = input("Your choice: ")
            CHOICE = CHOICE.upper()

            if CHOICE == 'S':
                self.Order_Choice.append("SMALL Pizza")
                self.Order_Cost.append(15)
                print("SMALL Pizza.")
                self.Toppings()

            elif CHOICE == 'M':
                self.Order_Choice.append("MEDIUM Pizza")
                self.Order_Cost.append(20)
                print("MEDIUM Pizza.")
                self.Toppings()

            elif CHOICE == 'L':
                self.Order_Choice.append("LARGE Pizza")
                self.Order_Cost.append(25)
                print("LARGE Pizza.")
                self.Toppings()

            elif CHOICE == 'B':
                self.Order_Choice.append("Breadsticks")
                self.Order_Cost.append(5)
                print("Breadsticks.")
                self.Toppings()

            elif CHOICE == 'C':
                self.Order_Choice.append("Calzone")
                self.Order_Cost.append(10)
                print("Calzone")
                self.Toppings()

            elif CHOICE == 'Q':
                self.Display_Order()
                print("\nOrder is complete. Exiting program.\n")
                Order_Complete = "TRUE"

            else:
                print("That choice was invalid. Please choose again.")

        print("\nThank you for choosing Carly's Calzones!\n")

class Establish2(Establishes):

    Order_Choice = []
    Order_Cost = []
    Order_Toppings = []
    Order_Toppings_Cost = []

    def Display_Order(self):

        system('cls')

        Items_Total = 0
        Toppings_Total = 0
        Item_Number = 0
        Topping_Number = 0

        print("\nItems in cart:")

        for x in self.Order_Choice:

            Topping_Number = 0
            print("\n---------------------------------------------------------------")
            print("ITEM: ", (Item_Number + 1), "\b.", x, "  Cost:", self.Order_Cost[(Item_Number)])
            Items_Total = Items_Total + self.Order_Cost[Item_Number]

            NumToppings = len(self.Order_Toppings[Item_Number])
            print("\n         ", "There are", NumToppings, "toppings for this item:\n")

            for y in self.Order_Toppings[Item_Number]:
                print("         ", (Topping_Number + 1), "\b.", y, "  Cost:",
                      self.Order_Toppings_Cost[Item_Number][Topping_Number])
                Toppings_Total = Toppings_Total + self.Order_Toppings_Cost[Item_Number][Topping_Number]
                Topping_Number = Topping_Number + 1

            Item_Number = Item_Number + 1

        Total_Cost = Items_Total + Toppings_Total

        print("\n---------------------------------------------------------------")
        print("\nRunning Item Total:", "$", Items_Total)
        print("Running Toppings Total:", "$", Toppings_Total)
        print("Total Cost:", "$", Total_Cost)

        print("\n1. Pay by Credit Card \n"
              "2. Pay by Debit Card \n"
              "3. Pay by PayPal \n")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            cardNumber = input("Enter card number: ")
            expiracyDate = input("Enter expiracy date: ")
            cvv = input("Enter cvv: ")
            creditCard = CreditCard(cardNumber, expiracyDate, cvv)
            payment = PaymentContext(creditCard)
            payment.perform_payment(Total_Cost)

        elif choice == 2:
            cardNumber = input("Enter card number: ")
            expiracyDate = input("Enter expiracy date: ")
            cvv = input("Enter cvv: ")
            debitCard = DebitCard(cardNumber, expiracyDate, cvv)
            payment = PaymentContext(debitCard)
            payment.perform_payment(Total_Cost)

        else:
            email = input("Enter email: ")
            password = input("Enter password: ")
            paypal = PayPal(email, password)
            payment = PaymentContext(paypal)
            payment.perform_payment(Total_Cost)

        ContinueIT = input("\nENTER anything to continue:")
        ContinueIT = " "

    def Toppings(self):

        Toppings_Complete = "FALSE"
        Current_Toppings_Selection = []
        Current_Toppings_Cost = []

        while Toppings_Complete != "TRUE":

            print("\n--------------Toppings Menu---------------")
            print("|                                        |")
            print("|       (E)xtra Cheese         ($1)      |")
            print("|       (X)tra Sauce           ($0)      |")
            print("|       (B)lasphemous Pinapple ($5)      |")
            print("|       (T)omatoes             ($1)      |")
            print("|       (O)lives               ($1)      |")
            print("|       (G)reen Peppers        ($1)      |")
            print("|       (J)alapeños            ($1)      |")
            print("|       (P)epperoni            ($2)      |")
            print("|       (S)ausage              ($2)      |")
            print("|       (H)am                  ($2)      |")
            print("|       (C)hicken              ($2)      |")
            print("|       (A)nchovies            ($2)      |")
            print("|       (Q)uit [Finished Toppings]       |")
            print("|                                        |")
            print("------------------------------------------", "\n")

            CHOICE = input("Your choice: ")
            CHOICE = CHOICE.upper()

            if CHOICE == 'E':
                Current_Toppings_Selection.append("Extra Cheese")
                Current_Toppings_Cost.append(1)
                print("Extra Cheese.")

            elif CHOICE == 'X':
                Current_Toppings_Selection.append("EXTRA Sauce")
                Current_Toppings_Cost.append(0)
                print("EXTRA Sauce")

            elif CHOICE == 'B':
                Current_Toppings_Selection.append("Blasphemous Pinapple")
                Current_Toppings_Cost.append(5)
                print("Blasphemous Pinapple.")

            elif CHOICE == 'T':
                Current_Toppings_Selection.append("Tomatoes")
                Current_Toppings_Cost.append(1)
                print("Tomatoes.")

            elif CHOICE == 'O':
                Current_Toppings_Selection.append("Olives")
                Current_Toppings_Cost.append(1)
                print("Olives.")

            elif CHOICE == 'G':
                Current_Toppings_Selection.append("Green Peppers")
                Current_Toppings_Cost.append(1)
                print("Green Peppers")

            elif CHOICE == 'J':
                Current_Toppings_Selection.append("Jalapeños")
                Current_Toppings_Cost.append(1)
                print("Jalapeños.")

            elif CHOICE == 'P':
                Current_Toppings_Selection.append("Pepperoni")
                Current_Toppings_Cost.append(2)
                print("Pepperoni.")

            elif CHOICE == 'S':
                Current_Toppings_Selection.append("Sausage")
                Current_Toppings_Cost.append(2)
                print("Sausage.")

            elif CHOICE == 'H':
                Current_Toppings_Selection.append("Ham")
                Current_Toppings_Cost.append(2)
                print("Ham")

            elif CHOICE == 'C':
                Current_Toppings_Selection.append("Chicken")
                Current_Toppings_Cost.append(2)
                print("Chicken.")

            elif CHOICE == 'A':
                Current_Toppings_Selection.append("Anchovies")
                Current_Toppings_Cost.append(2)
                print("Anchovies")

            elif CHOICE == 'Q':

                print("Toppings complete.")

                if len(Current_Toppings_Selection) < 1:
                    print("No toppings selected for this item.")
                    Current_Toppings_Selection.append("No toppings selected for this item.")
                    Current_Toppings_Cost.append(0)

                Toppings_Complete = "TRUE"

            else:
                print("That choice was invalid. Please choose again.")

        self.Order_Toppings.append(Current_Toppings_Selection)
        self.Order_Toppings_Cost.append(Current_Toppings_Cost)

    def mainBody(self):

        system('cls')

        Order_Complete = "FALSE"

        print("\nWelcome to Bembos", "\n")

        while Order_Complete != "TRUE":

            print("\n----------Product Menu------------")
            print("|                                   |")
            print("|       (S)mall Burger               |")
            print("|       (M)edium Burger              |")
            print("|       (L)arge Burger               |")
            print("|       (Q)uit (complete order)     |")
            print("|                                   |")
            print("-------------------------------------", "\n")

            CHOICE = input("Your choice: ")
            CHOICE = CHOICE.upper()

            if CHOICE == 'S':
                self.Order_Choice.append("SMALL Burger")
                self.Order_Cost.append(15)
                print("SMALL Pizza.")
                self.Toppings()

            elif CHOICE == 'M':
                self.Order_Choice.append("MEDIUM Burger")
                self.Order_Cost.append(20)
                print("MEDIUM Pizza.")
                self.Toppings()

            elif CHOICE == 'L':
                self.Order_Choice.append("LARGE Burger")
                self.Order_Cost.append(25)
                print("LARGE Pizza.")
                self.Toppings()

            elif CHOICE == 'Q':
                self.Display_Order()
                print("\nOrder is complete. Exiting program.\n")
                Order_Complete = "TRUE"

            else:
                print("That choice was invalid. Please choose again.")

        print("\nThank you for choosing Bembos!\n")

class EstablishmentContext:

    def __init__(self, establishment):
        self.establishment = establishment

    def performEstablishment(self):
        self.establishment.mainBody()
