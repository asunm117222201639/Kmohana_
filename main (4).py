'''Implement a class called Bankaccountholder that represents a bank account holder. The class should have private attributes for account number, name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. wirte a program to create an instance of the Bank account class and test the deposit and withdrawal functionality.'''


class BankAccountHolder:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      #self.__account_balance = self.__account_balance + amount
      print("Deposited ₹{}. New balance: ₹{}".format(amount,
                                                     self.__account_balance))

    else:
      print("Invalid deposit amount. Please deposit a positive amount.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      #self.__account_balance = self.__account_balance - amount
      print("withdraw ₹{}. New balance: ₹{}".format(amount,
                                                    self.__account_balance))

    else:
      print("Invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (Account #{}): ₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


# create an instance of the BankAccountHolder class
account = BankAccountHolder(account_number="123456789",
                            account_holder_name="Hari Prabu",
                            initial_balance=5000.0)

# Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()
