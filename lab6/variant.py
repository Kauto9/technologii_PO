text = input("Введите целые числа через пробел: ")
parts = text.split()

if len(parts) == 0:
    numbers = []
else:
    numbers = []
    for part in parts:
        numbers.append(int(part))

filtered = []
for number in numbers:
    if number >= 10:
        filtered.append(number)

count = len(filtered)
total = sum(filtered)
sorted_copy = sorted(filtered)

print("Результат:", filtered)
print("Количество:", count)
print("Сумма:", total)
print("Отсортированная копия:", sorted_copy)
