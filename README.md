# FUTURE_DS_01 — Business Sales Performance Analytics

**Future Interns | Data Science & Analytics — Task 1 (2026)**
**Intern:** Piyush Saxena | **CIN:** FIT/NOV26/DS24476

## Business Problem
A retail business (Superstore) is growing in sales but not equally in profit. This project answers, from real transaction data:
- Which products generate the most revenue and profit?
- How do sales change over time?
- Which categories and regions are most profitable?
- Where should the business focus to grow faster?

## Dataset
- **File:** `Superstore_Cleaned.xlsx` — 9,994 rows, 21 columns
- **Period:** 3 Jan 2014 – 30 Dec 2017 | **Orders:** 5,009 | **Customers:** 793 | **Products:** 1,850
- **Fields:** Order Date, Ship Mode, Customer, Segment, Region / State / City, Category, Sub-Category, Product, Sales, Quantity, Discount, Profit
- No missing values were found. Dates were parsed and Year / Quarter / Discount Band were derived for analysis.

## Tools Used
Python (pandas, matplotlib, openpyxl), Microsoft Excel, ReportLab (PDF)

## Key Results
| KPI | Value |
|---|---|
| Total Sales | $2,297,201 |
| Total Profit | $286,397 |
| Profit Margin | 12.47% |
| Avg Order Value | $458.61 |

- **Growth:** Sales +51.4% from 2014 ($484,248) to 2017 ($733,215). November / Q4 is the peak every year.
- **Best Category:** Technology — $836,154 sales, 17.40% margin. Copiers: 37.20% margin.
- **Problem Category:** Furniture — $742,000 sales but only 2.49% margin. Tables lose -$17,725.
- **Best Region:** West — $725,458 sales, 14.94% margin. Texas loses -$25,729 despite $170,188 in sales.
- **Discount Finding:** Every discount band above 20% loses money in total. Discounts >50% lost -$76,559.

## Recommendations
1. Cap discounts at 20% (manager approval above it).
2. Reprice / fix / exit loss-making Tables and Bookcases.
3. Push Technology (Copiers, Phones, Accessories) in Q4 campaigns.
4. Fix Central / Texas pricing instead of adding more discounts.
5. Rank customers by profit, not just sales, and run a monthly profit dashboard.

## Files in this Repo
- `FUTURE_DS_01_Business_Sales_Performance_Analytics_Report.pdf` — Client-ready report with charts, insights & recommendations
- `FUTURE_DS_01_Superstore_Dashboard.xlsx` — Excel dashboard (Dashboard, Yearly_Trend, Category, Region, SubCategory, Top10_By_Sales, Bottom10_By_Profit, Discount_Analysis) with native charts
- `analysis.py` — Reproducible Python analysis that recomputes every number in the report
- `Superstore_Cleaned.xlsx` — Source dataset (as provided for the task)

## How to Run
```bash
pip install pandas openpyxl matplotlib
python analysis.py
```

## Insights Story
Growth alone is not health. This business makes all its money at 0–20% discount on Technology and Office Supplies, and loses it on heavily discounted Furniture in Central / Texas. The fastest growth lever is not a new customer — it is pricing discipline.
