#прописываем функцию
def count_elements_occurrence(input_tuple):
    element_counts = {}

    for element in input_tuple:
        # Convert elements to a hashable form (e.g., tuples to strings)
        try:
            hashable_element = element if isinstance(element, str) else str(element)
        except TypeError:
            hashable_element = str(element)

        if hashable_element in element_counts:
            element_counts[hashable_element] += 1
        else:
            element_counts[hashable_element] = 1

    result_list = [(eval(k) if k.startswith('(') and k.endswith(')') else k, v) for k, v in element_counts.items()]

    result_tuple = tuple(result_list)

    return result_tuple

# Example usage:
input_tuple_1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
input_tuple_2 = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)
input_tuple_3 = ((1, 2, 3), (['A', 'B']), (1, 2, 3), (['A']))

result_1 = count_elements_occurrence(input_tuple_1)
result_2 = count_elements_occurrence(input_tuple_2)
result_3 = count_elements_occurrence(input_tuple_3)

print("Sample Output 1:")
print("Elements and their occurrences:")
print(result_1)

print("\nSample Output 2:")
print("Elements and their occurrences:")
print(result_2)

print("\nSample Output 3:")
print("Elements and their occurrences:")
print(result_3)