attempts = 0
value = int(input("Введите целое число: "))

while value <= 0:
    attempts += 1
    value = int(input("Введите положительное целое число: "))

print("Квадрат:", value * value)
print("Отклонено:", attempts)
