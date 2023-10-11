def count_elements_in_tuple(input_tuple):
    # Создаем пустой словарь для подсчета вхождений элементов
    element_count = {}

    try:
        # Итерируемся по элементам в кортеже
        for item in input_tuple:
            # Пробуем преобразовать элемент в строку (если это не строка)
            try:
                item_str = str(item)
            except Exception as e:
                item_str = str(item)

            # Если элемент уже есть в словаре, увеличиваем счетчик на 1, иначе добавляем его в словарь
            if item_str in element_count:
                element_count[item_str] += 1
            else:
                element_count[item_str] = 1

        # Создаем новый кортеж, содержащий пары элементов и их количество вхождений
        result_tuple = tuple((key, value) for key, value in element_count.items())

        return result_tuple
    except Exception as e:
        return f"Ошибка: {str(e)}"


# Примеры ввода
input_tuple_1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
input_tuple_2 = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)
input_tuple_3 = ((1, 2, 3), (['A', 'B']), (1, 2, 3), (['A']))

# Вызываем функцию для каждого примера ввода
output_1 = count_elements_in_tuple(input_tuple_1)
output_2 = count_elements_in_tuple(input_tuple_2)
output_3 = count_elements_in_tuple(input_tuple_3)

# Выводим результат
print("Пример вывода 1:")
print("Элементы и их вхождения:")
print(output_1)

print("Пример вывода 2:")
print("Элементы и их вхождения:")
print(output_2)

print("Пример вывода 3:")
print("Элементы и их вхождения:")
print(output_3)