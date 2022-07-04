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
    if number_type==ODD:
        return [number for number in numbers if number%2!=0]
    if number_type==EVEN:
        return [number for number in numbers if number%2==0]
    if number_type==PRIME:
        list_of_numbers = []
        for number in numbers:
            for i in range (1, number):
                if number%i==0 or number==0:
                    continue
                else:
                    i+=1
                list_of_numbers.append(number)
        return list_of_numbers


