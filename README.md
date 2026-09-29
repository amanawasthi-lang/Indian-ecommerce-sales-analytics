# Indian E-Commerce Sales Analytics
An original learning/portfolio implementation using a reproducible **synthetic sample dataset**. It demonstrates data cleaning, feature engineering, exploratory analysis, SQL analytics, and a Power BI-ready model.

## Stack
Python, Pandas, NumPy, MySQL, Matplotlib, Power BI, Jupyter.

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/data_cleaning.py
python scripts/feature_engineering.py
python scripts/analysis.py
python scripts/visualizations.py
```
Import `data/processed/orders_features.csv` into Power BI and follow `PowerBI/dashboard_build_guide.md`.

## Dataset
`data/raw/ecommerce_orders_sample.csv` is synthetic and generated for this project; it is not real company/customer data and should not be represented as market evidence.

## SQL
Run `sql/schema.sql`, import processed rows into `orders`, then execute query/view scripts. Adjust import path/tooling to your MySQL setup.

## Attribution
This is a customized independent learning project. If you consult or reuse material from other repositories, retain appropriate attribution and comply with their license. No affiliation with any retailer is implied.


## Interactive web frontend (Streamlit)
Run the Python pipeline, then launch:
```bash
streamlit run app.py
```
The app provides date/state/category/channel filters, KPI cards, monthly sales, category and state charts, channel mix, top products, and CSV export. It can fall back to the included synthetic raw sample if the processed feature file has not yet been generated.

### Deploy on Streamlit Community Cloud
1. Push this repository to GitHub.
2. Open https://share.streamlit.io/ and sign in with GitHub.
3. Choose **Create app**, select this repository and branch `main`.
4. Set the main file path to `app.py`, then deploy.
5. Add the deployed app URL to this README.
