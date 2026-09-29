import pandas as pd
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
src = ROOT / "data/processed/orders_clean.csv"
out = ROOT / "data/processed/orders_features.csv"
df = pd.read_csv(src, parse_dates=["order_date"])
df["year"] = df.order_date.dt.year
df["month_num"] = df.order_date.dt.month
df["month"] = df.order_date.dt.strftime("%b")
df["quarter"] = "Q" + df.order_date.dt.quarter.astype(str)
df["weekday"] = df.order_date.dt.day_name()
df["profit"] = (df.sales - df.cost).round(2)
df["profit_margin"] = (df.profit / df.sales.replace(0, pd.NA)).fillna(0).round(4)
df["sales_per_unit"] = (df.sales / df.quantity).round(2)
df["discount_band"] = pd.cut(df.discount_rate, [-.001,.001,.10,.20], labels=["No discount","Low (0-10%)","High (10-20%)"])
df.to_csv(out,index=False)
print(f"Saved features: {out}")
