import pandas as pd

df = pd.read_csv("data/samples.csv")
print(df["gc_content"].mean())   # 44.74
print(df.describe())