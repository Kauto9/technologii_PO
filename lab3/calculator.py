a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, *, /): ")

if op == "+":
    print(f"Результат: {a + b:.2f}")
elif op == "-":
    print(f"Результат: {a - b:.2f}")
elif op == "*":
    print(f"Результат: {a * b:.2f}")
elif op == "/":
    if b == 0:
        print("Деление на ноль запрещено")
    else:
        print(f"Результат: {a / b:.2f}")
else:
    print("Неизвестная операция")
