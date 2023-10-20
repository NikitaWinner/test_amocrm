from collections import deque


def count_islands(field: list[list[str]]) -> int:
    """
    Подсчитывает количество островов в двумерном массиве.

    :param field: Двумерный массив с элементами '1' (суша) и '0' (вода).
    :return: Количество островов.
    """
    if not field:
        return 0

    def bfs(row: int, col: int):
        """
        Поиск в ширину (Breadth-First Search) для обхода суши.

        :param row: Начальная строка.
        :param col: Начальный столбец.
        """
        queue = deque()  # Создаем очередь для обхода в ширину
        queue.append((row, col))  # Добавляем начальную клетку в очередь
        field[row][col] = '0'  # Помечаем начальную клетку как посещенную

        while queue:  # Цикл, выполняется, пока очередь не пуста
            r, c = queue.popleft()  # Извлекаем следующую клетку для проверки

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # Проверяем соседние клетки
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(field) and 0 <= nc < len(field[0]) and field[nr][nc] == '1':
                    # Если соседняя клетка - суша и не выходит за границы массива
                    queue.append((nr, nc))  # Добавляем ее в очередь для обхода
                    field[nr][nc] = '0'  # Помечаем как посещенную

    num_islands = 0  # Переменная для подсчета количества островов

    for row in range(len(field)):  # Итерируемся по строкам массива
        for col in range(len(field[0])):  # Итерируемся по столбцам массива
            if field[row][col] == '1':  # Если обнаружена суша
                num_islands += 1  # Увеличиваем счетчик островов
                bfs(row, col)  # Запускаем обход суши с текущей клетки

    return num_islands


field = [
    ['1', '1', '0', '0', '1'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['1', '0', '0', '1', '1'],
    ['1', '1', '0', '0', '0'],
]

if __name__ == '__main':
    result = count_islands(field)
    print(f"Количество островов: {result}")
