#example of input
sample_input = (55, 6, 777, 70.0, '7', 'A')

output_tuples = []  # To store the resulting tuples
current_tuple = ()  # To temporarily store items in a tuple

for item in sample_input:
    try:
        if isinstance(item, (int, float)):
            # If the item is an integer or float, add it to the current tuple
            current_tuple += (item,)
        else:
            if current_tuple:
                # If the current tuple is not empty, add it to the result and reset
                output_tuples.append(current_tuple)
                current_tuple = ()
            # Add the non-numeric item to the current tuple
            current_tuple += (item,)
    except TypeError:
        # Handle any TypeErrors that might occur (e.g., if isinstance fails)
        pass

if current_tuple:
    # After processing all items, add the last current tuple to the result
    output_tuples.append(current_tuple)

for output_tuple in output_tuples:
    print(output_tuple)