first_room = input("Введите номер аудитории 1 - ")
second_room = input("Введите номер аудитории 2 - ")
print(f"1 аудитория - {first_room} 2 аудитория - {second_room}")

temporary = first_room
first_room = second_room
second_room = temporary

print(f"Теперь 1 аудитория - {first_room} 2 аудитория - {second_room}")