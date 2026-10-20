total_seconds = int(input("Введите общее количество секунд: "))

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{hours} ч {minutes} мин {seconds} с")
