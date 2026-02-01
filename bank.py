# Определите класс `Account` имитирующий банковский счет.
# Класс должен включать атрибуты для хранения идентификатора владельца, баланса счета
# и методы для депозита (пополнения) и снятия средств, если на счету достаточно средств.


class Account():

    def __init__(self, id, balance=0):
        self.id=id
        self.balance=balance

    def deposit(self, money):
        if money > 0:
            self. balance += money
            print(f"Вы успешно пополнили счёт, сумма на счету - {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"недостаточно средств на счету")

        elif money <= self.balance:
            self.balance -= money
            print(f" Вы успешно сняли {money} рублей. Остаток на счёте: {self.balance}")

    def all_balance(self):
        print(f"текущий баланс - {self.balance}")


man = Account(f"12323132", 600)

man.all_balance()
man.deposit(23000)
man.withdraw(450)
man.withdraw(800)
man.withdraw(15150)









