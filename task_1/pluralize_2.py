def pluralize_string(count: int) -> str:
    """
    Возвращает строку вида 'N процент(а/ов)' с учётом склонения по-указанному number.

    :param number: Число для склонения.
    :return: Строка с числом и правильным склонением слова 'процент'.
    """

    if count % 10 == 1 and count % 100 != 11:
        return f"{count} программист"
    elif count % 10 in (2, 3, 4) and count % 100 not in (12, 13, 14):
        return f"{count} программиста"
    else:
        return f"{count} программистов"


if __name__ == '__main__':
    for i in range(100, 200):
        res = pluralize_string(i)
        print(res)
