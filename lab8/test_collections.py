from collections_lab import word_counts, common_topics, all_topics, totals_by_category, titles_in_category


def test_all():
    # word_counts
    assert word_counts("Python, python! SQL") == {"python": 2, "sql": 1}
    assert word_counts("!!!") == {}
    assert word_counts("") == {}

    # common_topics и all_topics
    assert common_topics(["python", "sql", "python"], ["sql", "git"]) == ["sql"]
    assert all_topics(["python", "sql", "python"], ["sql", "git"]) == ["git", "python", "sql"]
    assert common_topics([], ["python"]) == []
    assert all_topics([], ["python"]) == ["python"]

    # totals_by_category
    records = [
        {"title": "A", "category": "основное", "amount": 4},
        {"title": "B", "category": "дополнительное", "amount": 2},
        {"title": "C", "category": "основное", "amount": 3},
    ]
    assert totals_by_category(records) == {"основное": 7, "дополнительное": 2}
    assert totals_by_category([]) == {}

    # titles_in_category
    assert titles_in_category(records, "основное") == ["A", "C"]
    assert titles_in_category(records, "нет") == []

    # Вариант 10: печатные заказы
    orders = [
        {"title": "Каталог", "category": "основное", "amount": 4},
        {"title": "Буклет", "category": "дополнительное", "amount": 2},
        {"title": "Прейскурант", "category": "основное", "amount": 3},
    ]
    assert totals_by_category(orders) == {"основное": 7, "дополнительное": 2}
    assert titles_in_category(orders, "основное") == ["Каталог", "Прейскурант"]

    print("Базовые проверки пройдены")


if __name__ == "__main__":
    test_all()
