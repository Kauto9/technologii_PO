from functions import sum_digits, average, normalize_text, select_numbers


def main():
    # sum_digits
    number = int(input("Целое число: "))
    print("Сумма цифр:", sum_digits(number))

    # average
    text = input("Целые числа через пробел: ")
    parts = text.split()
    numbers = []
    for part in parts:
        numbers.append(int(part))
    result = average(numbers)
    if result is None:
        print("Среднее: Нет данных")
    else:
        print("Среднее:", result)

    # normalize_text
    text_input = input("Введите текст: ")
    print("Нормализованный:", normalize_text(text_input))

    # select_numbers
    text2 = input("Целые числа для отбора: ")
    parts2 = text2.split()
    numbers2 = []
    for part in parts2:
        numbers2.append(int(part))
    threshold = int(input("Введите порог: "))
    selected = select_numbers(numbers2, threshold)
    print("Выбранные:", selected)


if __name__ == "__main__":
    main()
