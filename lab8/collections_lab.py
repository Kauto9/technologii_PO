def word_counts(text):
    words = text.lower().split()
    counts = {}
    for word in words:
        cleaned = word.strip(".,!?;:")
        if cleaned == "":
            continue
        counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def print_word_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    return sorted(set(first) & set(second))


def all_topics(first, second):
    return sorted(set(first) | set(second))


def totals_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    result = []
    for record in records:
        if record["category"] == category:
            result.append(record["title"])
    return result
