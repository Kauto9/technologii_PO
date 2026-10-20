""""
first = "2"
second = "3"
print(first + second)
ошибка в том, что вводятся значения типа str, а операция для значений типа int
"""
first = 2
second = 3
print(first + second)

""""
age = input("Возраст: ")
print(age + 1)
проблема в том, что функция input по умолчанию считывается значения типа str, а операция для значений типа int
"""
age = int(input("Возраст: "))
print(age + 1)

""""
first = 4
second = 7
third = 10
average = first + second + third / 3
print(average)

алгебраическая ошибка, отсутствие скобок
"""
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print(average)