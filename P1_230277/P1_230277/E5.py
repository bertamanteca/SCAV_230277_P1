def run_length_encoding(sequence):
    compressed = []
    count = 1

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            count += 1
        else:
            compressed.append([sequence[i - 1], count])
            count = 1

    compressed.append([sequence[-1], count])
    return compressed

# Example
print('Sequence: ')
sequence = input()
result = run_length_encoding(sequence)
print(result)

