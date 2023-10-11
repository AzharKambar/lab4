try:
    # Определяем два набора
    set_A = {1, 2, 3, 4, 5}
    set_B = {5, 7, 8, 9, 2, 10}

    # Находим разницу между наборами A и B
    difference = set_A - set_B

    # Выводим результат
    print(difference)

except Exception as e:
    print("Произошла ошибка:", e)