# start bank management system using python

# 
 

from security import password
# import security file to password class
# 
import os
class BankAccount:
    def __init__(self):
        self.account = {}
    
    def create_account(self,account_number,name,type,balance):
        os.system('cls')
        if account_number in self.account:
            print('Account is already created ' + str(account_number))
        else:
            self.account[account_number] = {"account-number": account_number,"type": type, "name": name, "type": type, "balance": balance }
            print('Account created successfully :' + str(account_number))


    def deposit(self,account_number,amount):
        os.system('cls')
        if account_number in self.account:
            self.account[account_number] ['balance'] += amount
            print("Amount deposit from account "+str(account_number))
        else:
            print("account_number is not found in Account data!!!!!")


    def withdraw(self,account_number,amount):
        os.system('cls')
        if account_number in self.account:
            if self.account[account_number]['balance'] >= amount:
                self.account[account_number]['balance'] -= amount
                print("amount withdraw successfuly."+str(amount))
            else:
                print("amount is not equal to account balance"+str(amount))
        else:
            print("account not found in Account data!!!!!")
    

    def account_detail(self,account_number):
        os.system('cls')
        if account_number in self.account:
            print(f"Account number : " + str(account_number))
            print(f"Account holder : " + str(self.name))
            print(f"Account type : " + str(self.type))
            print(f"Account balance : " + str(self.amount))
        else:
            print("Account is not found in data:"+str(account_number),"--create account--")
    

    def close(self,account_number):
        os.system('cls')
        if account_number in self.account:
            del self.account[account_number]
            print("Account closed successfully")
        else:
            print("Account number is not found in data")
    

    def modify(self,account_number,name):
        os.system('cls')
        if account_number in self.account:
            self.account[account_number]['name'] = name
            print("Account holder name updated successfully")

        else:
            print("Account number is not found in data")
        
    def all_accounts(self):
        os.system('cls')
        print("All account holders")
        for account_number,details in self.account.items():
            print(f"\tAccount number: {account_number}, name: {details['name']},type: {details['type']},balance: {details['balance']}")


def main():

    secured = password()




    Bank = BankAccount()
    # BankAccount = Bank()
    filename = "Accounts.txt"

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                account_number,name,type,balance = line.strip().split(',')
                BankAccount.create(account_number,name,type,float(balance))
    

    while True:
        print("\n Menu")
        print("1. Create Account") # Create Account ok
        print("2. deposit amount") # deposit amount ok
        print("3. withdraw amount") # withdraw amount ok
        print("4. Account details") # Account details ok
        print("5. close account")   # Account close ok
        print("6. modify account")  # Account modify ok
        print("7. All accounts holder list") # All accounts holder list ok
        print("8. exit system") #ok
        # 

        choice = input("Enter your choice : ")
        os.system('cls')

        if choice == '1':
            
            account_number = input("Enter your account number : ")
            # master_pin = input("Enter your master pin : ")
            # if master_pin.lenth == 8:
            #     True
            # else:
            #     print('Invalid master pin')
            #     master_pin = input('Enter your master pin : ')

            name = input("Enter your name : ")
            type = input("Enter your  Account type : ")
            balance = float(input("Enter balance amount(Saving =< 6500 and Current =<95000 :"))
            #
            if type == 'C' or type == 'c':
                type = 'current'
            elif type == 'S' or type == 's':
                type ='savings'
            else:
                print('Invalid account type')
                type = input('Enter your account type(C|S):')
            Bank.create_account(account_number, name, type ,balance) 

        elif choice == '2':
            account_number = input("Enter your account number : ")
            amount = float(input("Enter amount to deposit : "))
            # code = input("Enter your master pin : ")
            # if code == master_pin and code.lengt == 8:
            #     Bank.deposit(account_number,code,amount)
            # else:
            #     print('Invalid master pin')
            #     master_pin = input('Enter your 6 Digit master pin : ')
            Bank.deposit(account_number,amount)

        elif choice == '3':
            account_number = input("Enter your account number : ")
            amount = float(input("Enter amount to withdraw : "))
            # code = input("Enter your master pin : ")
            # if code == master_pin and code.lengt == 8:
            #     Bank.withdraw(account_number,code,amount)
            # else:
            #     print('Invalid master pin')
            #     master_pin = input('Enter your 6 Digit master pin : ')
            Bank.withdraw(account_number, amount)
            # 

        elif choice == '4':
            account_number = input("Enter your account number : ")
            # code = input("Enter your master pin : ")
            # if code == master_pin and code.lengt == 8:
            #     Bank.account_detail(account_number,code)
            # else:
            #     print('Invalid master pin')
            #     code = input('Enter your 6 Digit master pin : ')
            # 
            Bank.account_detail(account_number)

        elif choice == '5':
            account_number = input("Enter your account number : ")
            # code = input("Enter your master pin : ")
            # if code == master_pin and code.lengt == 8:
            #     Bank.close(account_number,code)
            # else:
            #     print('Invalid master pin')
            #     code = input('Enter your 6 Digit master pin : ')
            # Bank.close(account_number)
            # 
            Bank.close(account_number)

        elif choice == '6':
            account_number = input("Enter your account number : ")
            name = input("Enter your name : ")
            # code = input("Enter your master pin : ")
            
            # if code == master_pin and code.lengt == 8:
            #     name = input("Enter your name : ")
            #     Bank.modify(account_number, name)
            # else:
            #     print('Invalid master pin')
            #     code = input('Enter your 6 Digit master pin : ')
            # 
            Bank.modify(account_number, name)

        elif choice == '7':
            passw = (input("Enter ADMIN Password : "))
            if passw == secured.password:
                Bank.all_accounts()
            else:
                print("Invalid password")
            # 
                
        elif choice == '8':
            with open(filename, 'w') as file:
                for account_number,details in Bank.account.items():
                    file.write(f"{account_number},{details['name']},{details['type']},{details['balance']}\n")
            print("Exiting system........")
            
            # 
        
        else:
            print("Invalid choice")
            os.system('cls')
            break

if __name__ == '__main__':
    main()




# this is my 2nd python project




# 