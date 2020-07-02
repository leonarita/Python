import pickle
import os
import pathlib


class Account:
    accNo = 0
    name = ''
    deposit = 0
    type = ''

    def createAccount(self):
        self.accNo = int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Enter the type of account [C/S] : ")
        self.deposit = int(input("Enter the initial amount(>=500 for saving and >=1000 for current) : "))
        print()

    def showAccount(self):
        print("Account Number: ", self.accNo, "\nAccount Holder Name: ", self.name,
              "\nType of Account: ", self.type, "\nBalance: ", self.deposit)

    def modifyAccount(self):
        print("Account Number: ", self.accNo)
        self.name = input("Modify account holder name : ")
        self.type = input("Modify type of account [C/S] : ")
        self.deposit = int(input("Modify balance : "))

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmout(self, amount):
        self.deposit -= amount

    def reporter(self):
        print(self.accNo, " ", self.name, " ", self.type, " ", self.deposit)

    def getAccountNo(self):
        return self.accNo

    def getAccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit


def intro():
    print("\n\n\t\t\t\t" + ('*' * 20))
    print("\t\t\t\tBANK MANAGMENT SYSTEM")
    print("\t\t\t\t" + ('*' * 20))

    print("\t\t\t\tBrought to you by: ")
    print("\t\t\t\tPress any button to continue! ")
    input()


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)


'''
def writeAccountsFile(account):
    file = pathlib.Path('accounts.data')
    if file.exists():
        infile = open('accounts.data', 'ab')
        pickle.dump(account, infile)
        infile.close()
'''

def displayAll():
    file = pathlib.Path('accounts.data')
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.accNo, " ", item.name, " ", item.type, " ", item.deposit)
        infile.close()
    else:
        print("No records to display")


def displaySp(num):
    file = pathlib.Path('accounts.data')
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.accNo == num:
                print("Your account balance is: ", item.deposit)
                found = True
        if not found:
            print("No existing record with this number")
    else:
        print('No records to search')


def depositAndWithdraw(num1, num2):
    file = pathlib.Path('accounts.data')
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.accNo == num1:
                if num2 == 1:
                    amount = int(input("Enter the amount to deposit: "))
                    item.deposit += amount
                    print("Your account is updated!")
                elif num2 == 2:
                    amount = int(input("Enter the amount to withdraw: "))
                    if amount <= item.deposit:
                        item.deposit -= amount
                        print("Your account is updated!")
                    else:
                        print("You cannot withdraw larger amount")
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(mylist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
    else:
        print('No records to search')


def deleteAccount(num):
    file = pathlib.Path('accounts.data')
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        newlist = []
        for item in oldlist:
            if item.accNo != num:
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def modifyAccount(num):
    file = pathlib.Path('accounts.data')
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.accNo != num:
                item.name = input("Enter the account holder name : ")
                item.type = input("Enter the account type : ")
                item.deposit = int(input("Enter the amount : "))
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def main():
    ch = ''
    num = 0
    intro()

    while ch != 8:
        # os.system("cls")
        print("\tMAIN MENU")
        print("\t1- New Account")
        print("\t2- Deposit Amount")
        print("\t3- Withdraw Amount")
        print("\t4- Balance Enquiry")
        print("\t5- All Account Holder List")
        print("\t6- Close An Account")
        print("\t7- Modify An Account")
        print("\t8- Exit")
        ch = input("\n\nSelect your option (1 - 8) : ")
        # os.system("cls")
        print('\n\n')

        if ch == '8':
            print('\tThanks for using bank managemnt system')
            break
        elif ch == '1':
            writeAccount()
        elif ch == '2':
            num = int(input('\tEnter the account no : '))
            depositAndWithdraw(num, 1)
        elif ch == '3':
            num = int(input('\tEnter the account no : '))
            depositAndWithdraw(num, 2)
        elif ch == '4':
            num = int(input('\tEnter the account no : '))
            displaySp(num)
        elif ch == '5':
            num = int(input('\tEnter the account no : '))
            displayAll()
        elif ch == '6':
            num = int(input('\tEnter the account no : '))
            deleteAccount(num)
        elif ch == '7':
            num = int(input('\tEnter the account no : '))
            modifyAccount(num)


if __name__ == '__main__':
    main()