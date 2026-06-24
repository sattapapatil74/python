
# Account Information from assignment
accountInfo = {
    "Name": "Shubham Lohar",
    "Account Number": "9098787676676",
    "Available Balance": 20000,
    "PIN": 1234
}

print("-------- WELCOME TO ATM --------")

# 1. User Authentication
entered_pin = int(input("Enter PIN: "))

if entered_pin != accountInfo["PIN"]:
    print("Invalid PIN")
    exit()
else:
    print("Login Successful\n")

# 2. ATM Menu
while True:
    print("\n1. Check Balance")
    print("2. Withdraw Amount")
    print("3. Deposit Amount")
    print("4. Change PIN")
    print("5. Account Details")
    print("6. Exit")

    choice = int(input("\nSelect Option: "))

    # 3. Check Balance
    if choice == 1:
        print("Available Balance: ₹", accountInfo["Available Balance"])

    # 4. Withdraw Amount
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: ₹"))
        if amount > accountInfo["Available Balance"]:
            print("Insufficient Balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            accountInfo["Available Balance"] -= amount
            print(f"₹{amount} withdrawn successfully")
            print("Updated Balance: ₹", accountInfo["Available Balance"])

    # 5. Deposit Amount
    elif choice == 3:
        amount = int(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("Invalid amount")
        else:
            accountInfo["Available Balance"] += amount
            print(f"₹{amount} deposited successfully")
            print("Updated Balance: ₹", accountInfo["Available Balance"])

    # 6. Change PIN
    elif choice == 4:
        current_pin = int(input("Enter current PIN: "))
        if current_pin == accountInfo["PIN"]:
            new_pin = int(input("Enter new PIN: "))
            accountInfo["PIN"] = new_pin
            print("PIN changed successfully")
        else:
            print("Incorrect current PIN")

    # Account Details
    elif choice == 5:
        print("\n------ Account Details ------")
        print("Name:", accountInfo["Name"])
        print("Account Number:", accountInfo["Account Number"])
        print("Available Balance: ₹", accountInfo["Available Balance"])
        print("-----------------------------")

    # Exit
    elif choice == 6:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid Option. Please select 1-6")