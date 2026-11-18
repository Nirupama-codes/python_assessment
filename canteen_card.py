# Canteen Card System

balance = 500
pin = 4321
count = 0
login = False

# Enter PIN
while count < 3:
    user_pin = int(input("Enter PIN:"))
    if user_pin == pin:
        print("Login successful!")
        login = True
        break
    else:
        print("Wrong PIN")
        count+= 1

# Show menu after login
if login == True:

    while True:
        print("\n========== CANTEEN MENU ==========")
        print("1. Check Balance")
        print("2. Add Money")
        print("3. Buy Item")
        print("4. Exit")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            print("Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter recharge amount:"))

            if amount <= 0:
                print("Invalid Amount")
                continue
            balance = balance + amount
            print("Recharge Successful")

        elif choice == 3:
            amount = int(input("Enter purchase amount:"))

            if amount <= 0:
                print("Invalid Amount")
                continue
            elif amount > balance:
                print ("Insufficient Balance")
            else:
                balance = balance - amount
                print("Purchase Successful")

        elif choice == 4:
            print("Thank you for using the Canteen Card System!")
            break

        elif choice == 5:
            print("History Not Available") 
            pass
        else:
            print("Invalid Choice") 
    print("Final Balance:", balance)

else:
    print("Your Card is Blocked.")



    

            