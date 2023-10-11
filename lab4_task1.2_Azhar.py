try:
    # Given tuple
    input_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
    # Convert the tuple to a string
    output_string = ''.join(input_tuple)
    # Print the resulting string
    print("The string is:", output_string)
except ValueError:
    print('Ввод неверный')