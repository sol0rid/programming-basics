sequences = {}
name = None

with open("data/sequences.fasta") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            name = line[1:]          # drop the '>'
            sequences[name] = ""
        else:
            sequences[name] += line  # sequences can span many lines!

print(len(sequences), "sequences loaded")

print(sequences)