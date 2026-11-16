import pandas as pd
df = pd.read_csv("data/smaples_2.csv")
print(df)
print(df.shape)
print(df["organism"])
print(df["length"].mean())
print(df[df["organism"] == "Escherichia coli"])
print(df[(df["gc_content"] > 42) & (df["length"] > 1000)])
print(df.sort_values("gc_content", ascending=False).head(3))
df["length_kb"] = df["length"] / 1000
print(df["length_kb"])
print(df["organism"].value_counts()) # counts how many times each unique value appears in a column