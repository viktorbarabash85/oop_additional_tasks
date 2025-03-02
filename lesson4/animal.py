"""
Напишите класс Animal, представляющий животное, имеющий следующие методы:
- __init__(self, name): конструктор, принимающий имя животного;
- speak(self): метод, который выводит звук, издаваемый животным.

Напишите класс Dog, наследующийся от класса Animal, представляющий собаку, имеющий
следующие методы:
- speak(self): метод, который выводит звук, издаваемый собакой.

Напишите класс Cat, наследующийся от класса Animal, представляющий кошку,
имеющий следующие методы:
- speak(self): метод, который выводит звук, издаваемый кошкой.
"""


class Animal:
    def __init__(self, name):
        self.name = name  # сохраняем имя животного

    def speak(self):
        print("?")  # базовый метод издания звука

class Dog(Animal):
    def speak(self):
        print("Woof!")  # переопределяем метод для собаки

class Cat(Animal):
    def speak(self):
        print("Meow!")  # переопределяем метод для кошки


# код для проверки 
animal = Animal("Animal")
animal.speak()  # ?

dog = Dog("Dog")
dog.speak()  # Woof!

cat = Cat("Cat")
cat.speak()  # Meow!
