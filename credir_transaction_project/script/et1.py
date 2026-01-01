import pandas as pd


df = pd.read_csv("data/transactions.csv")


print(df)


df['txn_date'] = pd.to_datetime(df['txn_date'])


df['txn_amount'] = df['txn_amount'].astype(float)


print("Null values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

print("ETL completed successfully")