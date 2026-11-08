import pandas as pd
import streamlit as st

st.set_page_config(page_title="Olist E-commerce Analytics", layout="wide")


@st.cache_data
def load_data():
    kpis = pd.read_csv("kpis.csv").iloc[0]
    monthly = pd.read_csv("monthly_revenue.csv")
    states = pd.read_csv("late_by_states.csv")
    return kpis, monthly, states


kpis, monthly, states = load_data()

st.title("Olist E-commerce Analytics")
st.caption(
    "Brazilian e-commerce orders, Sept 2016 to Oct 2018. "
    "Built with Python, pandas, SQL and Streamlit."
)

# ---- Headline numbers ----
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Revenue", f"{kpis['total_revenue']:,.0f}")
c2.metric("Orders", f"{int(kpis['total_orders']):,}")
c3.metric("Avg order value", f"{kpis['avg_order_value']:,.2f}")
c4.metric("Late deliveries", f"{kpis['late_pct']}%")
c5.metric("Avg delivery days", f"{kpis['avg_delivery_days']}")

# ---- Review scores ----
st.subheader("Late deliveries and review scores")
s1, s2, s3 = st.columns(3)
s1.metric("Avg score, on-time orders", f"{kpis['score_on_time']:.2f}")
s2.metric("Avg score, late orders", f"{kpis['score_late']:.2f}")
s3.metric("Gap", f"{kpis['score_on_time'] - kpis['score_late']:.2f} stars")
st.caption("This is an association, not proof that lateness causes lower scores.")

# ---- Monthly revenue ----
st.subheader("Monthly revenue (delivered orders)")
months = monthly["month"].tolist()
start, end = st.select_slider(
    "Month range", options=months, value=(months[0], months[-1])
)
sel = monthly[(monthly["month"] >= start) & (monthly["month"] <= end)]
st.line_chart(sel.set_index("month")["revenue"])
st.caption(
    "The first months of 2016 have very few orders, so early points are not a trend."
)

# ---- Late rate by state ----
st.subheader("Late-delivery rate by state")
min_orders = st.slider("Minimum orders per state", 100, 5000, 100, step=100)
view = (
    states[states["orders"] >= min_orders]
    .sort_values("late_pct", ascending=False)
    .reset_index(drop=True)
)
st.bar_chart(view.set_index("customer_state")["late_pct"])
st.dataframe(view, use_container_width=True)

# ---- Definitions ----
with st.expander("Definitions and limits"):
    st.markdown(
        "- **Late** means delivered after the estimated delivery date, "
        "for delivered orders that have a delivery date.\n"
        "- **Monthly revenue** is the sum of item prices of delivered orders, "
        "excluding freight.\n"
        "- States with few orders have less reliable rates, so use the slider.\n"
        "- Review scores use the latest review per order; orders without a "
        "review are left out."
    )
