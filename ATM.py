import os
import math
import sys
import time

print("This is an ATM to manage your cash.")
print()
print("----- Instructions -----")
print()
print("you can exit after any transaction by typing QUIT.\n")
print("clear -> resets all data.")
print()

def addStartingBalance():
    print("Shall I add a starting balance?")
    addStart = str(input())
    addStart = addStart.lower()
    if addStart == "y" or addStart == "yes":
        file = open("Bank Data.txt", "w")
        print("How much money would you like to put in your new account?")
        file.write(str(input()))
    print("Should I reset the old log files?")
    erase = str(input())
    erase = erase.lower()
    if erase == "y" or erase == "yes":
        file = open("Transaction Log.txt", "w")
        file.write("START")
    prompt()

def prompt():
    print("Would you like to make a transaction?")
    transact = str(input())
    transact = transact.lower()
    startup(transact)

def startup(confirm):
    run = True
    while run:
        if confirm == "yes" or confirm == "y":
         transaction_option()
        elif confirm == "no" or confirm == "n" or confirm == "quit" or confirm == "q":
            print("Exiting...")
            sys.exit()
        elif confirm == "clear" or confirm == "c":
            addStartingBalance()
        else:
            print("Input invalid")
        prompt()

def transaction_option():
    print("\nWould you like to make a deposit or withdrawal?")
    change = str(input(""))
    change = change.lower()
    if change == "deposit" or change == "d":
        cls()
        deposit_money()
    elif change == "withdrawal" or change == "w":
        cls()
        withdrawMoney()
    elif change == "quit" or change == "exit":
        print("Exiting...")
        cls()
        sys.exit()
    else:
        print("Invalid input")

def checkBalance():
    file = open("Bank Data.txt", "r")
    print("Your current balance is: " +(file.read()))
    current = open("Bank Data.txt", "r").read()
    floatCurrent = float(current)
    file.close()

def deposit_money():
    checkBalance()
    depositAction()

def depositAction():
    try:
        file = open("Bank Data.txt", "r")
        current = open("Bank Data.txt", "r").read()
        floatCurrent = float(current)
        file.close()

        print("\n\nHow much cash would you like to deposit?")
        addedAmount = input()
        floatAddedAmount = float(addedAmount)
        file = open("Bank Data.txt", "w")
        newAmount = floatCurrent + floatAddedAmount
        newAmount = str(newAmount)
        file.write(newAmount)
        file.close()
        file = open("Bank Data.txt", "r")
        cls()
        print("New Amount is: ")
        print(file.read())
        print()
        print()
        file.close()
        transactionOccurred = "+"
        transactionLogs(floatCurrent, transactionOccurred, floatAddedAmount, newAmount)
    except ValueError:
        print("You provided an invalid input.")


def withdrawMoney():
    checkBalance()
    withdrawalAction()

def withdrawalAction():
    try:
        file = open("Bank Data.txt", "r")
        current = open("Bank Data.txt", "r").read()
        floatCurrent = float(current)
        file.close()

        print("\n\nHow much cash would you like to withdraw?")
        addedAmount = input()
        floatAddedAmount = float(addedAmount)
        file = open("Bank Data.txt", "w")
        newAmount = floatCurrent - floatAddedAmount
        newAmount = str(newAmount)
        file.write(newAmount)
        file.close()
        file = open("Bank Data.txt", "r")
        print("\n\nNew balance is: ")
        print(file.read())
        file.close()
        transactionOccurred = "-"
        transactionLogs(floatCurrent, transactionOccurred, floatAddedAmount, newAmount)
    except ValueError:
        print("You provided an invalid input.")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def transactionLogs(floatCurrent, transactionOccurred, floatAddedAmount,newAmount):
    LOG = open("Transaction Log.txt", "a")
    oldAmount = floatCurrent
    oldAmount = str(floatCurrent)
    transactionType = transactionOccurred
    transactionAmount = floatAddedAmount
    transactionAmount = str(transactionAmount)
    updatedAmount = newAmount
    updatedAmount = str(newAmount)

    LOG.write("\n\nOn " + (time.strftime("%d/%M/%Y"))+": ")
    LOG.write("\nYour balance was: " + oldAmount)
    LOG.write("\nThe transaction that Occurred was: " + transactionType + transactionAmount)
    LOG.write("\nYour new Balance is: " + updatedAmount)


def main():
    prompt()


main()
