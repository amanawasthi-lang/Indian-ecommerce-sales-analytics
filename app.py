import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Indian E-Commerce Analytics", page_icon="🛍️", layout="wide")
ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data/processed/orders_features.csv"

@st.cache_data
def load_data():
    if DATA.exists():
        df = pd.read_csv(DATA, parse_dates=["order_date"])
    else:
        raw = pd.read_csv(ROOT / "data/raw/ecommerce_orders_sample.csv", parse_dates=["order_date"])
        raw["profit"] = raw["sales"] - raw["cost"]
        raw["profit_margin"] = raw["profit"] / raw["sales"].replace(0, pd.NA)
        raw["year"] = raw.order_date.dt.year
        raw["month_num"] = raw.order_date.dt.month
        raw["month"] = raw.order_date.dt.strftime("%b")
        raw["quarter"] = "Q" + raw.order_date.dt.quarter.astype(str)
        raw["weekday"] = raw.order_date.dt.day_name()
        raw["sales_per_unit"] = raw.sales / raw.quantity
        df = raw
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df

df = load_data()
st.title("🛍️ Indian E-Commerce | Sales Analytics")
st.caption("Interactive portfolio dashboard · Demonstration data (synthetic)")
with st.sidebar:
    st.header("Filters")
    dates = st.date_input("Order date range", value=(df.order_date.min().date(), df.order_date.max().date()),
                          min_value=df.order_date.min().date(), max_value=df.order_date.max().date())
    states = st.multiselect("State", sorted(df.state.unique()), default=[])
    categories = st.multiselect("Category", sorted(df.category.unique()), default=[])
    channels = st.multiselect("Channel", sorted(df.channel.unique()), default=[])

filtered = df.copy()
if isinstance(dates, tuple) and len(dates)==2:
    filtered = filtered[filtered.order_date.dt.date.between(dates[0], dates[1])]
if states: filtered = filtered[filtered.state.isin(states)]
if categories: filtered = filtered[filtered.category.isin(categories)]
if channels: filtered = filtered[filtered.channel.isin(channels)]

sales = filtered.sales.sum()
profit = filtered.profit.sum()
orders = filtered.order_id.nunique()
margin = profit/sales if sales else 0
a,b,c,d = st.columns(4)
a.metric("Total Revenue", f"₹{sales:,.0f}")
b.metric("Total Profit", f"₹{profit:,.0f}")
c.metric("Orders", f"{orders:,}")
d.metric("Profit Margin", f"{margin:.1%}")
st.divider()

left,right = st.columns(2)
with left:
    st.subheader("Monthly sales trend")
    monthly = filtered.set_index("order_date").resample("MS").sales.sum().reset_index()
    fig = px.line(monthly, x="order_date", y="sales", markers=True, labels={"order_date":"Month","sales":"Sales (₹)"})
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Category performance")
    cat = filtered.groupby("category", as_index=False).agg(Sales=("sales","sum"), Profit=("profit","sum"))
    fig = px.bar(cat, x="category", y=["Sales","Profit"], barmode="group")
    st.plotly_chart(fig, use_container_width=True)

left,right = st.columns(2)
with left:
    st.subheader("Sales by state")
    region = filtered.groupby("state",as_index=False).sales.sum().sort_values("sales",ascending=False)
    st.plotly_chart(px.bar(region,x="sales",y="state",orientation="h",labels={"sales":"Sales (₹)","state":"State"}),use_container_width=True)
with right:
    st.subheader("Channel mix")
    channel = filtered.groupby("channel",as_index=False).sales.sum()
    st.plotly_chart(px.pie(channel,names="channel",values="sales",hole=.45),use_container_width=True)

st.subheader("Top products")
top = filtered.groupby("product",as_index=False).agg(Sales=("sales","sum"), Units=("quantity","sum"), Profit=("profit","sum")).sort_values("Sales",ascending=False).head(10)
st.dataframe(top, use_container_width=True, hide_index=True)
st.download_button("Download filtered data (CSV)", filtered.to_csv(index=False).encode("utf-8"), "filtered_ecommerce_orders.csv", "text/csv")
