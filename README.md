# 📊 E-Commerce Sales Insights Dashboard

A full-stack data engineering and analytics solution that transforms raw e-commerce transaction data into actionable business KPIs. This project features a containerized database, optimized SQL views, and a live interactive dashboard.

## 🚀 Key Features
* **Automated Data Pipeline:** Processes sales, marketing spend, and customer data.
* **Business KPIs:** Real-time tracking of Net Revenue, AOV (Average Order Value), and Gross Margin.
* **Marketing Analytics:** Calculation of ROAS (Return on Ad Spend) and CAC (Customer Acquisition Cost) by channel.
* **Retention Tracking:** 30-day customer retention cohort analysis.

## 🛠️ Technical Stack
* **Database:** PostgreSQL (Containerized via **Docker**)
* **Data Modeling:** Complex Joins, CTEs, Views, and Performance Indexing.
* **Frontend:** Python (**Streamlit**) & Pandas.
* **Tools:** DBeaver for database management.

## 📸 Dashboard Preview
![Sales Dashboard](<screenshot.png.png>)

## 📁 Repository Structure
* `dashboard.py`: The Python application for the interactive UI.
* `1_database_setup_and_data.sql`: The full database schema, seeding data, and analytics views.
* `requirements.txt`: Python dependencies required to run the project.
* `screenshot.png`: Visual representation of the final dashboard.

## ⚙️ How to Run Locally
1. **Database:** Ensure Docker is running and your PostgreSQL container (`ecsales`) is active.
2. **Setup:** Run the SQL script in `1_database_setup_and_data.sql` using a tool like DBeaver.
3. **Environment:** Install dependencies using `pip install -r requirements.txt`.
4. **Launch:** Run the dashboard using `python -m streamlit run dashboard.py`.
