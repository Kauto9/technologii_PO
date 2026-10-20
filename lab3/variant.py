progress = int(input("Введите прогресс загрузки (0–100): "))

if progress < 0 or progress > 100:
    print("Ошибка диапазона")
elif progress <= 4:
    print("Начало")
elif progress <= 94:
    print("Загрузка")
else:
    print("Завершение")
