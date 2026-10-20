text = input("Введите целые числа через пробел: ")
parts = text.split()

if len(parts) == 0:
    print("Нет данных")
else:
    numbers = []
    for part in parts:
        numbers.append(int(part))

    maximum = max(numbers)
    positions = []
    for index, value in enumerate(numbers):
        if value == maximum:
            positions.append(index)

    print("Позиции:", positions)
