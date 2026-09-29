# Power BI dashboard build
**Page:** Executive Overview (16:9)

## Load data
Get Data → Text/CSV → `data/processed/orders_features.csv` (run scripts first).
Set `order_date` to Date; sales/cost/profit to Decimal Number; profit_margin to Decimal Number.

## Layout
- Top: title “Indian E-Commerce | Sales & Profit” and date range slicer.
- KPI row: Total Sales, Total Profit, Total Orders, Average Order Value.
- Middle left: Line chart — order_date (Month) vs Total Sales.
- Middle right: Clustered bar — category vs Total Sales and Total Profit.
- Bottom left: Bar chart — state vs Total Sales (sort descending).
- Bottom right: Donut — channel vs Total Sales.
- Slicers: year, state, category, channel.

Import `theme.json` via View → Themes → Browse for themes.
Create measures from `measures.dax` (Modeling → New measure). Use currency format INR for sales/profit/AOV and percentage for margin.
