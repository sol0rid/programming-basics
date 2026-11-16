sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA", "ATGNNNCGC"]

# 1. Print each sequence with its length
print("--- Lengths ---")
for seq in sequences:
    print(f"{seq}: {len(seq)}")

# 2. Build a list of lengths, then print the average
lengths = []
for seq in sequences:
    lengths.append(len(seq))
average = sum(lengths) / len(lengths)
print(f"\nAverage length: {average:.2f}")

# 3. Count how many sequences start with ATG
atg_count = 0
for seq in sequences:
    if seq.startswith("ATG"):
        atg_count += 1
print(f"\nSequences starting with ATG: {atg_count}")

# 4. Print only the sequences longer than 5 bases
print("\n--- Longer than 5 bases ---")
for seq in sequences:
    if len(seq) > 5:
        print(seq)

# 5. GC content per sequence (nested loop)
print("\n--- GC content ---")
for seq in sequences:
    gc = 0
    for base in seq:          # inner loop: look at each base
        if base == "G" or base == "C":
            gc += 1
    gc_content = gc / len(seq) * 100
    print(f"{seq}: {gc_content:.2f}%")