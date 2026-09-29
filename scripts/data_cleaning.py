import pandas as pd
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
src = ROOT / "data/raw/ecommerce_orders_sample.csv"
out = ROOT / "data/processed/orders_clean.csv"
df = pd.read_csv(src)
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df = df.drop_duplicates(subset=["order_id"])
df = df.dropna(subset=["order_id","order_date","sales"])
for col in ["quantity","unit_price","discount_rate","sales","cost"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df[(df["quantity"] > 0) & (df["sales"] >= 0) & (df["cost"] >= 0)]
df.to_csv(out, index=False)
print(f"Saved {len(df)} cleaned rows to {out}")
