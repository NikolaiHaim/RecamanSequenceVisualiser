def recaman_recursive(n, seq=None):
    if seq is None:
        seq = [0]

    if len(seq) == n:
        return seq

    step = len(seq)
    candidate = seq[-1] - step
    if candidate >= 0 and candidate not in seq:
        seq.append(candidate)
    else:
        seq.append(seq[-1] + step)

    return recaman_recursive(n, seq)

# Example usage
seq = recaman_recursive(999)

# Save to file
with open("recaman_seq_recu.txt", "w") as f:
    for num in seq:
        f.write(f"{num}\n")

print(seq)
