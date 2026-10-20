text = input("Введите целые числа через пробел: ")
parts = text.split()

if len(parts) == 0:
    print("Нет данных")
else:
    numbers = []
    for part in parts:
        numbers.append(int(part))

    count = len(numbers)
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]

    for number in numbers:
        total += number
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number

    average = total / count

    print("Количество:", count)
    print("Сумма:", total)
    print("Минимум:", minimum)
    print("Максимум:", maximum)
    print("Среднее: {:.2f}".format(average))
