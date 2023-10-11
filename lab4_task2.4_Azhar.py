try:
    # Определяем наборы A, B и C
    set_A = {1, 2, 3, 4, 7}
    set_B = {8, 7, 9, 4, 2, 0, 10}
    set_C = {4, 0, 1}

    # Проходим по элементам набора A
    for element in set_A:
        # Если элемент находится в наборе C, добавляем его в набор B
        if element in set_C:
            set_B.add(element)

    # Выводим обновленный набор C
    print("Обновлен set_C =", set_C)

except Exception as e:
    print("Произошла ошибка:", e)