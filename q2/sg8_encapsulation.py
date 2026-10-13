class BankAccount:
  def __init__(self, account_number, balance):
    self.__balance = 0
    self.balance = balance
    self.__account_number = account_number

  def set_account_number(self, account_number):
    self.__account_number = account_number

  @property
  def balance(self):
    return self.__balance

  @balance.setter
  def balance(self, account):
    if amount >= 0:
      self.__balance = amount
    else:
      print("Error. Balance cannot be negative.")

  @property
  def account_number(self):
    return self.__account_number

  @property
  def balance(self):
    return self.__balance

  @balance.setter
  def balance(self,amount):
    if amount >= 0:
      self.__balance = amount
    else:
      print("Error. Balance cannot be negative")


account = BankAccount("4277", 125000)
print("Account 1")
print("Account Number:", account.account_number)
print(f"Balance: {account.balance:,.2f} PHP")

account.set_account_number("4277")

account.balance = 825000

print(f"\nUpdate Balance to -1000")
account.balance = -1000

print("Account Number:", account.account_number)
print(f"Balance: {account.balance:.2f} PHP")
