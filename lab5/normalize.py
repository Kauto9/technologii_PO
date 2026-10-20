text = input("Введите текст: ")

original_length = len(text)
normalized = " ".join(text.split())
normalized_length = len(normalized)
words = normalized.split()
word_count = len(words)

print("Исходная длина:", original_length)
print("Нормализованная длина:", normalized_length)
print("Нормализованный текст:", normalized)
print("Количество слов:", word_count)
