import pandas as pd
df = pd.read_csv("data/smaples_2.csv")
df["organism"].value_counts()
df[(df["gc_content"].mean()) | (df["leght"].mean())]