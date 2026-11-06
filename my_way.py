from my_stats import average

gc_values = []
with open("data/samples.csv") as f:
    next(f)  # skip the header line
    for line in f:
        parts = line.strip().split(",")
        gc_values.append(float(parts[1]))

print(average(gc_values))   # 44.74