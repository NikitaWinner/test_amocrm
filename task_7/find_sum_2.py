from typing import List, Union


def find_pair_sum(arr: List[int], K: int) -> Union[List[int], List]:
    """
    Находит пару чисел в массиве, которые в сумме равны заданному числу K, используя множество для оптимизации.

    :param arr: Исходный массив чисел.
    :param K: Число, которое мы пытаемся получить в сумме парой чисел из массива.
    :return: Список с двумя числами, сумма которых равна K, или пустой список, если такой пары нет.
    """
    num_set = set()  # Создаем множество для отслеживания чисел

    for num in arr:
        complement = K - num  # Находим, какое число дополнит текущее до K
        if complement in num_set:
            return [complement, num]  # Нашли пару чисел
        num_set.add(num)  # Добавляем текущее число в множество

    return []


arr = [-3, -1, 0, 1, 2, 4, 6]
K = 3

result = find_pair_sum(arr, K)
print(result)  # Результат: [1, 2]
