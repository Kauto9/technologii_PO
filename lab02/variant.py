total = int(input("Введите общее количество бутылок: "))
capacity = int(input("Введите вместимость одного ящика: "))

full = total // capacity
remainder = total % capacity
boxes = (total + capacity - 1) // capacity

print(f"Полных ящиков: {full}")
print(f"Остаток: {remainder}")
print(f"Всего ящиков: {boxes}")
