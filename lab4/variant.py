n = int(input("Введите количество чисел n (n >= 0): "))

count = 0
total = 0

for _ in range(n):
    value = int(input("Введите целое число: "))
    if value >= 10:
        count += 1
        total += value

print("Количество:", count)
print("Сумма:", total)
