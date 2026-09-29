import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data/processed/orders_features.csv",parse_dates=["order_date"])
monthly=df.groupby(df.order_date.dt.to_period("M")).sales.sum()
plt.figure(figsize=(11,5)); monthly.plot(); plt.title("Monthly Sales Trend"); plt.xlabel("Month"); plt.ylabel("Sales (INR)")
plt.tight_layout(); plt.savefig(ROOT/"outputs/plots/monthly_sales.png",dpi=160)
