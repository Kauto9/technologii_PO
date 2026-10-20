text = input("Введите текст: ")

cleaned = text.replace(" ", "")
cleaned_lower = cleaned.lower()

if len(cleaned_lower) == 0:
    print("Нет текста")
elif cleaned_lower == cleaned_lower[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")
