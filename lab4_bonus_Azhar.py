def count_occurrences(input_tuple):
    element_count = {}  # Dictionary to store element counts
    for item in input_tuple:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1

    result_tuple = []
    for item, count in element_count.items():
        result_tuple.append((item, count))

    return tuple(result_tuple)


def find_popular_elements(input_tuple):
    element_count = count_occurrences(input_tuple)
    max_count = max(element_count, key=lambda x: x[1])[1]  # Find the maximum count
    min_count = min(element_count, key=lambda x: x[1])[1]  # Find the minimum count

    most_popular = [item[0] for item in element_count if item[1] == max_count]
    least_popular = [(item[0], item[1]) for item in element_count if item[1] == min_count]

    frequent_elements = [item for item in element_count if item[1] == max_count]

    return most_popular, least_popular, frequent_elements


def print_results(input_tuple, most_popular, least_popular, frequent_elements):
    print("Elements and their occurrences:")
    print(count_occurrences(input_tuple))

    if len(most_popular) == 1:
        print(f"The most popular element: {most_popular[0]} - {max_count} occurrences")
    else:
        print("The most popular element: no most popular element")

    if len(least_popular) == 1:
        print(f"The least popular element: {least_popular[0][0]} - {min_count} occurrence(s)")
    else:
        print("The least popular element: no least popular element")

    print("The frequent elements:", frequent_elements)


# Sample Input
input_data = (5, 55, 10, 1, 0, 1, 55, 77, 10, 5, 5, 55, 77)
element_count = count_occurrences(input_data)

most_popular, least_popular, frequent_elements = find_popular_elements(input_data)
print_results(input_data, most_popular, least_popular, frequent_elements)