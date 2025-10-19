def recaman(n):
    sequence = [0]
    for i in range(1, n):
        candidate = sequence[-1] - i
        if candidate >= 0 and candidate not in sequence:
            sequence.append(candidate)
        else:
            sequence.append(sequence[-1] + i)
    return sequence

# Example usage
seq = recaman(50)

# Save to file
with open("recaman_seq_iter.txt", "w") as f:
    for num in seq:
        f.write(f"{num}\n")

print(seq)