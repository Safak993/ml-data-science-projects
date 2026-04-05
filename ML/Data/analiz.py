import pandas as pd
df_raw = pd.read_parquet("Syn-training.parquet")
print(df_raw["Label"].value_counts())
print(df_raw.groupby("Label")[['Total Fwd Packets', 'Flow Packets/s', 'Flow Duration', 'Packet Length Mean']].mean())