import pandas as pd

df = pd.read_csv("data/transactions.csv")


print(df.groupby("txn_type")["txn_amount"].sum())


failed_pct = (df[df["txn_status"] == "FAILED"].shape[0] / len(df)) * 100
print("Failed %:", failed_pct)


print(df[df["txn_type"] == "DEBIT"]
      .groupby("customer_id")["txn_amount"].sum())