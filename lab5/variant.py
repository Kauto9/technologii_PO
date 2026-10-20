text = input("Введите текст: ")

words = text.split()
matches = []

for word in words:
    cleaned = word.strip(".,!?;:").lower()
    if len(cleaned) == 0:
        continue
    if cleaned[0] == cleaned[-1]:
        matches.append(cleaned)

if len(matches) > 0:
    for match in matches:
        print(match)
    print("Количество:", len(matches))
else:
    print("Нет совпадений")
    print("Количество:", 0)
