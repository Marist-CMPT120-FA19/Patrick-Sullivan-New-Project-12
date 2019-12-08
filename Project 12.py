account = []

def Balance():
    print("\nChecking: $" + account[2])
    print("Savings: $" + account[3])

def deposit(depAmount):
    Option = input("\nAre you sure you would like to deposit?"
                   "\nIndicate (c) or (s) for the account that you would like to deposit into: ")

    if Option == "c":
        Balance_1 = int(account[2])
        Balance_2 = Balance_1 + depCAmount
        account[2] = str(Balance_2)
        print(depCAmount + "dollars was deposited into your Checking account.")
    elif Option == "s":
        Balance_1 = int(account[3])
        Balance_2 = Balance_1 + depSAmount
        account[3] = str(Balance_2)
        print(depSAmount + "dollars was deposited into your Savings account.")
    else:
        print("Which account would you like to make a deposit?")
        deposit(depAmount)


def withdraw(wAmount):
    Option = input("Are you sure you would like to make a withdrawl?"
                   "\nIndicate (c) or (s) which account you would like to withdraw from: ")

    if Option == "c":
        Balance_1 = int(account[2])
        if Balance_1 >= wCAmount:
            Balance_2 = Balance_1 - wCAmount
            account[2] = str(Balance_2)
            print(wCAmount + "dollars was withdrawn from your Checking account.") 
        else:
            print("Insufficient Funds")
    elif Option == "s":
        Balance_1 = int(account[3])
        if Balance_1 >= wSAmount:
            Balance_2 = Balance_1 - wSAmount
            account[3] = str(Balance_2)
            print(wSAmount, "dollars was withdrawn from your Checking account.")
        else:
            print("Insufficient Funds")
    else:
        print("Indicate the account that you would like withdraw from.")
        withdraw(withdrawAmount)


def transfer(tAmount):
    Option = input("\nAre you sure you would like to make a transfer?"
                   "\nIndicate (c) to transfer from Checking to Savings or (s) to transfer from Savings to Checking.")

    if Option == "c":
        Balance_1 = int(account[2])
        if Balance_1 >= transferCSAmount:
            Balance_2 = Balance_1 - tCSAmount
            account[2] = str(Balance_2)
            Balance_savings = int(account[3]) + tCSAmount
            account[3] = str(Balance_savings)
            print(tCSAmount + "dollars was transferred from your Checking to Savings account.")
        else:
            print("Insufficient funds.")
    elif Option == "s":
        Balance_1 = int(account[3])
        if Balance_1 >= tSCAmount:
            Balance_2 = Balance_1 - tSCAmount
            account[3] = str(Balance_2)
            Balance_checking = int(account[2]) + tSCAmount
            account[2] = str(cBalance)
            print(tSCAmount + "dollars was transferred from your Savings to Checking account.")
        else:
            print("Insufficient funds.")

def ATM():
    Option = "0"
    while(Option != "8"):
        print("\n   ATM Home Page")
        print("1. Balance Inquiry")
        print("2. Deposit to Checking")
        print("3. Deposit to Savings")
        print("4. Withdraw from Checking")
        print("5. withdraw from Savings")
        print("6. Transfer from Checking to Savings")
        print("7. Transfer from Savings to Checking")
        print("8. Exit System")
        Option = input("\nPlease choose which option you would like to have done today: ")

        if Option == "1":
            Balance()
        elif Option == "2":
            try:
                depCAmount = int(input("Please enter the amount that you would like to deposit into Checking: "))
                deposit(depCAmount)
            except ValueError:
                print(depCAmount, "dollars was deposited into your Checking account.")
        elif Option == "3":
            try:
                depSAmount = int(input("Please enter the amount that you would like to deposit into Savings: "))
                deposit(depSAmount)
            except ValueError:
                print(depSAmount, "dollars was deposited into your Savings account.")
        elif Option == "4":
            try:
                wCAmount = int(input("Please enter the amount that you would like to withdraw from Savings: "))
                withdraw(wCAmount)
            except ValueError:
                print(wCAmount, "dollars was withdrawn from your Checking account.")
        elif Option == "5":
            try:
                wSAmount = int(input("Please enter the amount that you would like to withdraw from Checking: "))
                withdraw(wSAmount)
            except ValueError:
                print(wSAmount, "dollars was withdrawn from your Savings account.")
        elif Option == "6":
            try:
                tCSAmount = int(input("Please enter the amount that you would like to tranfer from Checking to Savings: "))
                transfer(tCSAmount)
            except ValueError:
                print(tCSAmount, "dollars was transferred from your Checking to Savings account.")
        elif Option == "7":
            try:
                tSCAmount = int(input("Enter Transfer Amount from Savings to Checking: "))
                transfer(tSCAmount)
            except ValueError:
                print(tSCAmount, "dollars was transferred from your Savings to your Checking account.")
        elif Option == "8":
            print("Thank you! Have a great day.")
        else:
            print("Please indicate which option you would like to do today.")
    
def main():
    Filename = "account.txt"
    File = open("account.txt", 'r')
    Data = File.read()
    Information = Data.split('\n')
    File.close()

    for info in Information:
        if ':' in info:
            info_ = info.split(": ")
            info_data = info_[1]
            account.append(info_data)

    print("Please enter your User ID and associated PIN number below.")
    ID = input("    User ID: ")
    PIN = input("    PIN: ")

    if ID == account[0] and PIN == account[1]:
        print("\nWelcome to our ATM service! ")

        ATM()

        separateAcct = "ID: " + account[0] + "\n"
        separateAcct = separateAcct + "Pin: " + account[1] + "\n"
        separateAcct = separateAcct + "\n"
        separateAcct = separateAcct + "Checking: " + account[2] + "\n"
        separateAcct = separateAcct + "Savings: " + account[3]

        output = open(Filename, 'w')
        output.write(separateAcct)
        output.close()
    else:
        print("Your User ID or PIN are not correct, please retry.")

main()
