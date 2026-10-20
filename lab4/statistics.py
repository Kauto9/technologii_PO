n = int(input("Введите количество чисел n (n >= 1): "))

first = True
total = 0
positive = 0
maximum = 0

for _ in range(n):
    value = int(input("Введите целое число: "))
    total += value
    if value > 0:
        positive += 1
    if first:
        maximum = value
        first = False
    elif value > maximum:
        maximum = value

print("Сумма:", total)
print("Положительных:", positive)
print("Максимум:", maximum)
