"""Simplify the avocado dataset for illustration purposes.

The orginal dataset (avocado.csv) comes from:
    https://www.kaggle.com/neuromusic/avocado-prices

"""
import pandas as pd

# Simplify the dataset to keep only the price volums, region and type
# Non-weighted average of the price to keep it simple
df = pd.read_csv("avocado.csv", index_col=0).groupby(by=["region", "type"]).agg({"AveragePrice": "mean", "Total Volume": "sum"})
df = df.reset_index(drop=False)
df = df[df.region != "TotalUS"]
df.to_csv("avocado_simplified.csv")