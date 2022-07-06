"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number**2 for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number <= 1:
        return False
    for i in range (2, int(number**0.5)+1):
        if number % i ==0:
            return False
    return True


def filter_numbers(numbers, number_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if number_type == ODD:
        return list(filter(lambda n: n % 2 != 0, numbers))
    if number_type == EVEN:
        return list(filter(lambda n: n % 2 == 0, numbers))
    if number_type == PRIME:
        return list(filter(is_prime, numbers))
