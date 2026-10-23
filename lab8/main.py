from collections_lab import word_counts, print_word_counts, common_topics, all_topics, totals_by_category, titles_in_category


def main():
    # 1. Частоты слов
    text = input("Введите текст: ")
    counts = word_counts(text)
    print_word_counts(counts)

    # 2. Учебные интересы
    first = input("Темы первого студента (через пробел): ").split()
    second = input("Темы второго студента (через пробел): ").split()
    print("Общие:", common_topics(first, second))
    print("Все:", all_topics(first, second))

    # 3. Запись и пара
    record = {"title": "Python", "hours": 4}
    print("Запись:", record)
    record["hours"] = 6
    record["completed"] = False
    print("Изменённая запись:", record)
    pair = (record["title"], record["hours"])
    name, count = pair
    print(f"Пара: {name}, {count}")

    # 4. Вариант 10: печатные заказы
    print()
    print("--- Печатные заказы ---")
    orders = [
        {"title": "Каталог", "category": "основное", "amount": 4},
        {"title": "Буклет", "category": "дополнительное", "amount": 2},
        {"title": "Прейскурант", "category": "основное", "amount": 3},
    ]
    totals = totals_by_category(orders)
    print("Сводка по категориям:")
    for cat in sorted(totals):
        print(f"  {cat}: {totals[cat]}")
    category = input("Введите категорию для поиска: ")
    print("Заказы:", titles_in_category(orders, category))


if __name__ == "__main__":
    main()
