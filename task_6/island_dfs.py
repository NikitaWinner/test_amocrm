def count_islands(field: list[list[str]]) -> int:
    """
    Подсчитывает количество островов в двумерном массиве.

    :param field: Двумерный массив с элементами '1' (суша) и '0' (вода).
    :return: Количество островов.
    """
    if not field:
        return 0

    def dfs(row: int, col: int):
        """
        Поиск в глубину (Depth-First Search) для обхода суши.

        :param row: Начальная строка.
        :param col: Начальный столбец.
        """
        # Проверка на выход за границы массива или наличие воды в текущей клетке
        if row < 0 or col < 0 or row >= len(field) or col >= len(field[0]) or field[row][col] == '0':
            return

        field[row][col] = '0'  # Помечаем текущую клетку как посещенную
        # Рекурсивно вызываем функцию dfs для соседних клеток
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    num_islands = 0  # Переменная для подсчета количества островов

    for row in range(len(field)):  # Итерируемся по строкам массива
        for col in range(len(field[0])):  # Итерируемся по столбцам массива
            if field[row][col] == '1':  # Если обнаружена суша
                num_islands += 1  # Увеличиваем счетчик островов
                dfs(row, col)  # Запускаем обход суши с текущей клетки

    return num_islands  # Возвращаем общее количество островов


field = [
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
    ['0', '1', '0', '1', '1'],
]

if __name__ == '__main__':
    result = count_islands(field)
    print(f"Количество островов: {result}")
