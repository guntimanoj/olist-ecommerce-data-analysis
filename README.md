# Olist E-commerce Analytics: Sales and Delivery Performance

**Live dashboard:** https://guntimanoj-olist.streamlit.app

<img width="1920" height="1080" alt="Screenshot_20261112-175441" src="https://github.com/user-attachments/assets/0d7880a1-1c43-4fb1-ae4c-e16416458611" />


Analysis of about 99,000 orders from Olist, a Brazilian online marketplace (Sept 2016 to Oct 2018), using Python, pandas, SQL (SQLite) and Streamlit.

## Aim
Answer three business questions:
1. How did sales develop over time?
2. Which states have the most late deliveries?
3. How are late deliveries related to customer review scores?

## Key results
- **8.1%** of 96,470 delivered orders arrived after the estimated date. Average delivery time is 12.1 days.
- Late rates are highest in **AL (23.9%)**, MA (19.7%), PI (16.0%) and CE (15.3%), and lowest in **SP (5.9%)**.
- Late orders average **2.57 stars** against **4.29 stars** for on-time orders (gap 1.72 stars). This is an association, not proof of cause.
- **SP** has 41,746 orders (about 42% of all orders), far ahead of RJ (12,852) and MG (11,635).
- Monthly revenue (delivered orders, excluding freight) grew through 2017, peaked in **November 2017 (987,765)** and stayed roughly flat in 2018.

## Recommendations
1. **Prioritise RJ and BA for delivery improvements.** RJ (13.5% late, 12,350 delivered orders) and BA (14.0%, 3,256) combine high volume with above-average late rates, so improvements there affect the most customers.
2. **Review carrier coverage and delivery estimates in the north-east (AL, MA, PI, CE).** Late rates there are 15% to 24%, up to about 3 times the national average.
3. **Track the late rate and the average review score together as monthly KPIs,** and use SP (5.9% late) as the benchmark.

## What is in the notebook
`notebooks/01_data_exploration.ipynb` has these sections:
1. **Setup and loading data**
2. **Data cleaning:** dates, missing values, duplicates, validation
3. **Sales and product analysis:** revenue, top products, orders by state, a map of customer locations
4. **Delivery analysis:** late rate by state, delivery vs estimated date by month, review scores
5. **SQL:** SQLite tables and queries, validated against pandas
6. **Key findings**
7. **Export:** summary tables for the dashboard

## Data
Public dataset: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/olistbr/brazilian-ecommerce) on Kaggle. The raw CSV files are not stored in this repository because of their size. To reproduce the analysis, download them from Kaggle and upload them to the notebook.

## Cleaning log
- 99,441 orders, no duplicate rows or order IDs.
- Date columns converted to datetime. 2,965 orders have no delivery date (mostly cancelled, unavailable or still in transit); only 8 delivered orders have none. Delivery analysis uses delivered orders with a delivery date (96,470).
- 646 delivered orders have no review and are left out of score averages. Where an order had several reviews, the latest is used.
- 610 products have no category and are labelled "unknown"; 2 products are missing measurements.
- Fixed duplicate category columns (`_x` and `_y`) after merging the translation table.
- Added columns: delivery days, late flag (delivered after estimated date).
- SQLite tables were checked against the pandas data (row counts 99,441 / 112,650 / 99,441), and SQL monthly revenue matches pandas.

## Definitions and limits
- **Late** = delivered after the estimated delivery date. Estimated dates are generous (orders arrive about 12 to 14 days early on average), so the average gap can hide late orders. The late rate is therefore measured order by order.
- **Revenue** = sum of item prices for delivered orders, excluding freight.
- States with fewer than 100 orders are excluded from late-rate rankings. Several small states have fewer than 500 orders, so their rates are less reliable.
- Months near the start and end of the data have few orders and should not be read as trends.
- Review score differences show association, not causation.

## Repository
- `notebooks/01_data_exploration.ipynb`: cleaning, analysis, SQL and findings
- `app.py` and `requirements.txt`: Streamlit dashboard
- `kpis.csv`, `monthly_revenue.csv`, `late_by_states.csv`: summary tables used by the dashboard

## Run the dashboard locally
`pip install -r requirements.txt` then `streamlit run app.py`

## Dependencies
- pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite (built into Python)
- Streamlit

## Author
Gunti Manoj. GitHub: [github.com/guntimanoj](https://github.com/guntimanoj)
