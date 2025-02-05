"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в который будет производиться запись логов;

- __call__(self, message): магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл.
"""


class Logger:
    filename: str
    message: str

    def __init__(self, filename):
        """Конструктор, принимающий имя файла для записи логов."""
        self.filename = filename

    def __call__(self, message):
        """Магический метод для записи сообщения в файл."""
        with open(self.filename, 'a') as file:  # Открываем файл в режиме добавления
            file.write(message + '\n')  # Записываем сообщение с переносом строки


# код для проверки
logger = Logger("log.txt")
logger("This is a test message.")

