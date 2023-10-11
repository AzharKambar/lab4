try:
    # Sample Input
    tuple_A = (1, 2, 3, 4, 5, 6, 7)
    tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)
    # Find the midpoint for both tuples
    midpoint_A = len(tuple_A) // 2
    midpoint_B = len(tuple_B) // 2
    # Concatenate the first half of A with the second half of B
    final_tuple = tuple_A[:midpoint_A] + tuple_B[midpoint_B:]
    # Print the concatenated tuple
    print(final_tuple)
except ValueError:
    print("Ввод неверный")