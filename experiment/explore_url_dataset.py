import pandas as pd

DATASET_PATH = 'data/malicious_phish.csv'

df = pd.read_csv(DATASET_PATH)

print("dataset loaaded")
print("rows" , len(df))
print("columns", list(df.columns))


print("\n calss distribution")
print(df["type"].value_counts())


df["is_mal"] = (df["type"]!="benign").astype(int)
print("\nbinary class distibution")
print(df["is_mal"].value_counts())


