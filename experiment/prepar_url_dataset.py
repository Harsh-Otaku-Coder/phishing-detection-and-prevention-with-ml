import pandas as pd
from src.url_features import extract_features

input_file = "data/malicious_phish.csv"

def convert(label):
    if label == "benign":
        return 0
    else:
        return 1

df = pd.read_csv(input_file)

print("original dataset:")
print(df.head())

print("\n original shape:")
print(df.shape)

df["label"] = df["type"].apply(convert)

print("\n binary level distribution")
print(df["label"].value_counts())

sample = df.head(1000).copy()

feature = sample["url"].apply(extract_features)

feature_df = pd.DataFrame(feature.tolist())

result = pd.concat (
    [
        feature_df,
        sample["label"].reset_index(drop=True),
    ],
    axis=1,
)

print("\n Feature dataset")
print(result.head())

print("\nFeature shape")
print(result.shape)

print("\n missing value")
print(result.isnull().sum())


result.to_csv("data/url_features.csv", index= False)

print("\nSaved feature dataset:")
print("shape:", result.shape)



