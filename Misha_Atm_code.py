# ATM SIMULATION SYSTEM

pin = 9296
balance = 50000

print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("       WELCOME TO ATM")
print("................................")

user_pin = int(input("Enter your ATM PIN: "))

if user_pin == pin:

    while True:
        print("\n------ ATM MENU ------")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is Rs.", balance)

        elif choice == 2:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Enter a valid amount.")
            elif amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining balance: Rs.", balance)
            else:
                print("Insufficient balance!")

        elif choice == 3:
            amount = int(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Money deposited successfully!")
                print("Updated balance: Rs.", balance)
            else:
                print("Enter a valid amount.")

        elif choice == 4:
            old_pin = int(input("Enter old PIN: "))

            if old_pin == pin:
                new_pin = int(input("Enter new PIN: "))
                pin = new_pin
                print("PIN changed successfully!")
            else:
                print("Incorrect old PIN!")

        elif choice == 5:
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice. Try again.")

else:
    print("Incorrect PIN! Access Denied.")
