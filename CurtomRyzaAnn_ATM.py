Acc_ID = "55735"
Acc_Name = "Ryza Ann Curtom"
Acc_Pass = "0922"
Authentication = False
Balance = 1000.00
Attempts = 3

while Attempts > 0:
    input_ID = input("Enter the account ID: ")
    input_Pass = input("Enter the account password: ")

    if input_ID == Acc_ID and input_Pass == Acc_Pass:
        print("Access Granted! Welcome, ", Acc_Name)
        Authentication = True
        break
    else:
        Attempts -= 1
        print("Invalid Credentials! Attempts remaining: ", Attempts)

if Authentication:
    while True:
        print("")
        print("1 || Check Balance")
        print("2 || Deposit")
        print("3 || Withdraw")
        print("4 || Exit")

        choice = input("Enter your choice: ")
        print("")

        if choice == '1':
            print("Current Balance: $", Balance)

        elif choice == '2':
            d_amount = float(input("Enter the amount to deposit: "))
            if d_amount > 0:
                Balance += d_amount
                print("Successfully deposited $", d_amount)
            else:
                print("Transaction Failed: Invalid amount.")

        elif choice == '3':
            print("Current Balance: $", Balance)
            w_amount = float(input("Withdraw amount: "))
            if 0 < w_amount <= Balance:
                Balance -= w_amount
                print("Successfully withdrawn $", w_amount)
            else:
                print("Transaction Failed: Insufficient funds or Invalid amount")

        elif choice == '4':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid selection")
else:
    print("Invalid credentials: Account Locked")
    print("Please contact your bank for assistance.")
