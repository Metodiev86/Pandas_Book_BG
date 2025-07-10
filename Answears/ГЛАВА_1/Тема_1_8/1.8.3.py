#3.	Дефинирайте клас BankAccount (банкова сметка) с атрибут balance (баланс) и методи deposit(amount) (внос) и withdraw(amount) (теглене). Конструкторът трябва да инициализира баланса на 0. Направете няколко вноса и тегления и изведете текущия баланс.

class BankAccount:
	def __init__(self):
		self.balance = 0

	def deposit(self, amount: float):
		self.balance += amount

	def withdraw(self, amоunt):
		self.balance -= amоunt

my_BankAccount = BankAccount()

print(f"Първоначалния ми баланс е: ", my_BankAccount.balance)

my_BankAccount.deposit(20)
print("След първоначалния депозит, баланса ми е: ", my_BankAccount.balance)

my_BankAccount.deposit(50)
print("След още един депозит, баланса ми е: ", my_BankAccount.balance)

my_BankAccount.withdraw(30)
print("След тегленето, баланса ми е: ", my_BankAccount.balance)


