import streamlit as st
import pandas as pd
import psycopg2

# Set up the web page
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")
st.title("📊 E-Commerce Sales Insights")

# Connect to your local PostgreSQL Docker container
@st.cache_resource
def get_connection():
    return psycopg2.connect("host=localhost port=5432 dbname=ecsales user=postgres password=pass")

conn = get_connection()

# ---------------------------------------------------------
# 1. Revenue & ROAS by Channel/Day (Using your View)
# ---------------------------------------------------------
st.header("1. Revenue & ROAS by Channel/Day")
query_daily = "SELECT * FROM ec.v_channel_daily ORDER BY order_date, channel_name;"
df_daily = pd.read_sql(query_daily, conn)

col1, col2 = st.columns(2)
with col1:
    st.dataframe(df_daily, use_container_width=True)
with col2:
    # Create a visual chart for Revenue
    chart_data = df_daily.pivot(index='order_date', columns='channel_name', values='revenue')
    st.line_chart(chart_data)

st.divider()

# ---------------------------------------------------------
# 2. Top Products by Net Revenue
# ---------------------------------------------------------
st.header("2. Top Products (Net Revenue)")
query_top = """
SELECT p.product_name, c.category_name,
       SUM((oi.unit_price*oi.quantity) - COALESCE(oi.discount,0)) AS net_revenue,
       SUM(oi.quantity) AS units
FROM ec.orders o
JOIN ec.order_items oi ON oi.order_id=o.order_id
JOIN ec.products p ON p.product_id=oi.product_id
JOIN ec.categories c ON c.category_id=p.category_id
WHERE o.status='PAID'
GROUP BY 1,2
ORDER BY net_revenue DESC 
LIMIT 10;
"""
df_top = pd.read_sql(query_top, conn)

col3, col4 = st.columns(2)
with col3:
    st.dataframe(df_top, use_container_width=True)
with col4:
    # Create a visual bar chart
    st.bar_chart(df_top, x="product_name", y="net_revenue")

st.divider()

# ---------------------------------------------------------
# 3. Refund Impact
# ---------------------------------------------------------
st.header("3. Refund Impact (Lost Revenue)")
query_refunds = """
SELECT o.order_datetime::date AS order_date,
       SUM((oi.unit_price*oi.quantity) - COALESCE(oi.discount,0)) AS refunded_revenue
FROM ec.orders o
JOIN ec.order_items oi ON oi.order_id = o.order_id
WHERE o.status='REFUNDED'
GROUP BY 1
ORDER BY 1;
"""
df_refunds = pd.read_sql(query_refunds, conn)

if not df_refunds.empty:
    st.warning(f"Total Revenue Lost to Refunds: **${df_refunds['refunded_revenue'].sum():.2f}**")
    st.dataframe(df_refunds, use_container_width=True)
else:
    st.success("No refunds recorded yet!")