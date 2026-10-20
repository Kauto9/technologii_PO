first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

if first <= second and first <= third:
    print("Минимальное:", first)
elif second <= first and second <= third:
    print("Минимальное:", second)
else:
    print("Минимальное:", third)
