a = int(input("Введите первое целое число a: "))
b = int(input("Введите второе целое число b: "))

if a < b:
    for num in range(a, b + 1):
        print(num)
elif a > b:
    for num in range(a, b - 1, -1):
        print(num)
else:
    print(a)
