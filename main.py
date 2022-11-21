class Account:
    def __init__(self, number):
        self.number = number
        self.balance = 0


class User:
    def __init__(self, PIN):
        self.PIN = PIN
        self.account_list = {}

    def make_account(self, number):
        self.account_list[number] = Account(number)

    def see_balance(self, PIN, number):
        if self.PIN==PIN:
            print(self.account_list[number].balance)
        else:
            print('wrong PIN number')

    def deposit(self, PIN, number, money):
        if self.PIN == PIN:
            self.account_list[number].balance+=money
            print(f'account number : {number}, current balance : {self.account_list[number].balance}')
        else:
            print('wrong PIN number')

    def withdraw(self, PIN, number, money):
        if self.PIN == PIN:
            if self.account_list[number].balance < money:
                print(f'current balance is {self.account_list[number].balance}\n you cannot withdraw')
            else:
                self.account_list[number].balance -= money
                print(f'account number : {number}, current balance : {self.account_list[number].balance}')
        else:
            print('wrong PIN number')



if __name__ == '__main__':
    PIN = 1234
    u1 = User(PIN) # create user
    account_number=4321
    u1.make_account(account_number) # create account
    card_insert = False
    while not card_insert: # insert card
        number = input("insert card(press number 1): ")
        print(number)
        card_insert = number == '1'
        if card_insert:
            PIN = 1234

    account = False
    while not account: # check account
        account_number = int(input("insert account number: "))
        account = (account_number in u1.account_list)
    controller = True
    while controller: # select menu
        menu = input("insert number(0 out, 1 check balance, 2 deposit, 3 withdraw: ")
        if menu == '0':
            print('good bye')
            break
        elif menu == '1':
            u1.see_balance(PIN, account_number)
        elif menu == '2':
            money = int(input("insert money: "))
            u1.deposit(PIN, account_number, money)
        elif menu == '3':
            money = int(input("how much money do you withdraw: "))
            u1.withdraw(PIN, account_number, money)
        else:
            print('wrong number, press repeat')
