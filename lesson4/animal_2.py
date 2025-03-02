"""
Допишите код под условия в цикле так, чтобы вывод был корректным
"""

class Animal:
    def __init__(self, name):
        self.name = name  # сохраняем имя животного

    # в проверочном коде этот метод не применяется
    def walk(self):
        print(f"{self.name} is walking")  # базовый метод ходьбы


class Dog(Animal):
    @staticmethod
    def bark():
        print('Bark!')  # метод лая для собаки


class Cat(Animal):
    @staticmethod
    def meow():
        print('Meow!')  # метод мяуканья для кошки


animals = [Dog('Dog1'), Dog('Dog2'), Cat('Cat1'), Dog('Dog3')]

for animal in animals:
    # Проверяем тип животного и вызываем соответствующий метод
    if isinstance(animal, Dog):  # если это собака
        animal.bark()
    elif isinstance(animal, Cat):  # если это кошка
        animal.meow()