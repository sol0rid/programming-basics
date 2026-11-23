
import requests #to contact the api
import pandas as pd #to create a csv table

genes = ["BRCA1", "BRCA2", "TP53", "EGFR", "MYC", "KRAS", "CFTR", "HBB"]
rows = []                                   

for symbol in genes:                        
    url = f"https://rest.ensembl.org/lookup/symbol/homo_sapiens/{symbol}"
    response = requests.get(url, headers={"Content-Type": "application/json"})
    response.raise_for_status()             

    data = response.json()                  

    rows.append({
        "gene": symbol,
        "chromosome": data["seq_region_name"],
        "length": data["end"] - data["start"] + 1,
        "strand": data["strand"],
    })

df = pd.DataFrame(rows)                     
df.to_csv("results/genes.csv", index=False)

print(df)