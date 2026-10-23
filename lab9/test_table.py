from table import row_sums, column_sums, diagonal_pattern, transform


def test_all():
    # row_sums
    assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
    assert row_sums([[7]]) == [7]
    assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
    assert row_sums([]) == []

    # column_sums
    assert column_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]
    assert column_sums([[7]]) == [7]
    assert column_sums([[1], [-1], [0]]) == [0]
    assert column_sums([]) == []

    # diagonal_pattern
    assert diagonal_pattern(1) == [[0]]
    assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

    # transform (вариант 10)
    assert transform([]) == []
    assert transform([[-2, 0, 3], [4, -5, 6]]) == [[-2, 0, 3], [4, 0, 0]]

    # Проверка независимости
    original = [[-2, 0, 3], [4, -5, 6]]
    result = transform(original)
    result[0][0] = 99
    assert original == [[-2, 0, 3], [4, -5, 6]]

    print("Базовые проверки пройдены")


if __name__ == "__main__":
    test_all()
