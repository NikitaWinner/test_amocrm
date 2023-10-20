from typing import List, Union


def find_pair_sum(arr: List[int], K: int) -> Union[List[int], List]:
    """
    Находит пару чисел в массиве, которые в сумме равны заданному числу K.

    :param arr: Исходный массив чисел.
    :param K: Число, которое мы пытаемся получить в сумме парой чисел из массива.
    :return: Список с двумя числами, сумма которых равна K, или пустой список, если такой пары нет.
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]  # Вычисляем сумму двух чисел в указанных позициях.
        if current_sum == K:  # Если сумма равна K, возвращаем пару чисел.
            return [arr[left], arr[right]]
        elif current_sum < K:  # Если сумма меньше K, увеличиваем левый индекс, чтобы увеличить сумму.
            left += 1
        else:  # Если сумма больше K, уменьшаем правый индекс, чтобы уменьшить сумму.
            right -= 1

    return []  # Если в массиве нет пары чисел с суммой K, возвращаем пустой список.


if __name__ == '__main__':
    arr = [-3, -1, 0, 1, 2, 4, 6]
    K = 3

    result = find_pair_sum(arr, K)
    print(result)
