import pandas as pd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data/processed/orders_features.csv",parse_dates=["order_date"])
monthly=df.groupby(df.order_date.dt.to_period("M")).agg(sales=("sales","sum"),profit=("profit","sum"),orders=("order_id","nunique")).reset_index()
monthly["month"]=monthly.order_date.astype(str)
monthly.drop(columns="order_date").to_csv(ROOT/"outputs/reports/monthly_kpis.csv",index=False)
print("Top categories by sales:")
print(df.groupby("category").sales.sum().sort_values(ascending=False))
