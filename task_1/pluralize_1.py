from random import randint


def pluralize_string(count: int) -> str:
    """
    Возвращает строку вида 'N процент(а/ов)' с учётом склонения по-указанному number.

    :param count: Число для склонения.
    :return: Строка с числом и правильным склонением слова 'процент'.
    """

    number_100 = count % 100
    number_10 = number_100 % 10
    result_string = f'{count} процент'

    if 5 <= number_100 <= 20:
        result_string += 'ов'
    elif 1 < number_10 < 5:
        result_string += 'а'
    elif number_10 == 1:
        result_string = result_string
    else:
        result_string += 'ов'

    return result_string


if __name__ == '__main__':
    for _ in range(100):
        res = pluralize_string(randint(1, 10 ** 6))
        print(res)
