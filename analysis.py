"""FUTURE_DS_01 - Business Sales Performance Analytics
Recomputes every KPI in the report from Superstore_Cleaned.xlsx
Run: python analysis.py
"""
import pandas as pd
df = pd.read_excel("Superstore_Cleaned.xlsx", sheet_name="Sample - Superstore")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Year"] = df["Order Date"].dt.year
print(f"Rows: {len(df)} | Orders: {df['Order ID'].nunique()} | Customers: {df['Customer ID'].nunique()}")
print(f"Total Sales: ${df['Sales'].sum():,.2f} | Total Profit: ${df['Profit'].sum():,.2f} | Margin: {df['Profit'].sum()/df['Sales'].sum()*100:.2f}%")
print("\nBy Year:"); print(df.groupby("Year").agg(Sales=("Sales","sum"), Profit=("Profit","sum")))
print("\nBy Category:"); print(df.groupby("Category").agg(Sales=("Sales","sum"), Profit=("Profit","sum")))
print("\nBy Region:"); print(df.groupby("Region").agg(Sales=("Sales","sum"), Profit=("Profit","sum")))
print("\nTop 10 Products by Sales:"); print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))
