text = input("Введите целые числа через пробел: ")
parts = text.split()

numbers = []
for part in parts:
    numbers.append(int(part))

result = []
for number in numbers:
    if number < 0:
        result.append(abs(number))
    else:
        result.append(number)

print("Исходный список:", numbers)
print("Новый список:", result)
