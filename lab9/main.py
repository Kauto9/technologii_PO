from table import row_sums, column_sums, diagonal_pattern, transform


def main():
    # Ввод матрицы
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)

    print("Исходная матрица:", matrix)
    print("Суммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

    # Диагональный узор
    size = int(input("Введите размер узора: "))
    pattern = diagonal_pattern(size)
    for line in pattern:
        print(*line)

    # Вариант 10: преобразование
    print("Исходная:", matrix)
    result = transform(matrix)
    print("Преобразованная:", result)


if __name__ == "__main__":
    main()
