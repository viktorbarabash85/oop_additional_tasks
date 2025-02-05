"""
Напишите класс Timer, который будет вычислять время выполнения блока кода.
Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""

import time


class Timer:
    start_time: float
    end_time: float

    def __enter__(self):
        """Запускает таймер"""

        self.start_time = time.perf_counter()
        # self.elapsed_time = None
        # print(f"Start time: {self.start_time:.4f} seconds")  # проверочный print начала времени
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Останавливает таймер и выводит время выполнения блока кода."""

        self.end_time = time.perf_counter()
        # print(f"End time: {self.end_time:.4f} seconds")  # проверочный print завершения времени
        self.elapsed_time = self.end_time - self.start_time
        # print(f"Elapsed time: {self.elapsed_time:.4f} seconds")  # проверочный print затраченного времени


with Timer() as timer:
    # Блок кода
    total = sum(range(1, 1000001))  # Пример: подсчет времени для вычисления суммы чисел от 1 до 1 миллиона.
    # time.sleep(2)  # Пример: подсчет времени выполнения кода с задержкой в 2 секунды

# Код для проверки затраченного времени
print("Execution time:", timer.elapsed_time)
