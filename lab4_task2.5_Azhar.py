try:
    from itertools import combinations

    # Исходное надмножество A
    A = {1, 2, 3, 4, 5, 6}

    # Размер n комбинаций
    n = 3

    # Размер m списка комбинаций
    m = 5

    # Генерируем комбинации размера n из множества A
    comb = list(combinations(A, n))

    # Создаем список m уникальных комбинаций
    result = []

    for i in range(m):
        result.append(comb[i % len(comb)])  # Используем остаток от деления, чтобы обеспечить уникальность

    # Выводим результат
    print(result)

except Exception as e:
    print("Произошла ошибка:", e)