import pandas as pd

df = pd.read_csv("data/processed/revenue_final_dataset_v2.csv")

X = df.drop(columns=["Total_Amount"])

print(X.columns.tolist())
