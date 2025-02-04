"""
Напишите класс BankAccount, имеющий следующие свойства и методы:

- __init__(self, balance): конструктор, принимающий начальный баланс счета
- balance: свойство, которое возвращает текущий баланс счета
- deposit(self, amount): метод, который позволяет внести деньги на счет
- withdraw(self, amount): метод, который позволяет снять деньги со счета
- close(self): метод, который закрывает счет и возвращает оставшиеся на нем деньги

Для свойства balance используйте декоратор @property.
"""


class BankAccount:
    balance: float


    def __init__(self, balance: int):
        self._balance = balance  # Начальный баланс счета


    @property
    def balance(self) -> int:
        return self._balance  # Возвращает текущий баланс счета

    def deposit(self, amount: int) -> None:
        self._balance += amount  # Вносит деньги на счет


    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self._balance:
            self._balance -= amount  # Снимает деньги со счета


    def close(self) -> float:
        remaining_balance = self._balance  # Запоминаем оставшиеся деньги
        self._balance = 0  # Закрываем счет
        return remaining_balance  # Возвращаем оставшиеся деньги


# код для проверки
account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0