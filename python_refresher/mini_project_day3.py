import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Day 3: Mini Project
# =========================

# 1️⃣ Load CSV
df = pd.read_csv("practice.csv")
print("CSV Loaded:")
print(df)

# 2️⃣ Filter high sales (>300)
high_sales = df[df["Sales"] > 300]
print("\nHigh Sales (>300):")
print(high_sales)

# 3️⃣ Summarize / group data
summary = df.groupby("Name")["Sales"].agg(['sum','mean','count'])
print("\nSales Summary by Name:")
print(summary)

# 4️⃣ Add Bonus Column (10% of Sales)
df["Bonus"] = df["Sales"] * 0.10
print("\nData with Bonus Column:")
print(df)

# 5️⃣ Visualization
total_by_name = df.groupby("Name")["Sales"].sum()

plt.figure(figsize=(8,5))
total_by_name.plot(kind='bar', color='skyblue')
plt.title("Total Sales by Name")
plt.xlabel("Name")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("day3_total_sales_chart.png")
plt.show()

# Optional: highlight high sales
colors = ['red' if val > 300 else 'green' for val in total_by_name]
total_by_name.plot(kind='bar', color=colors)
plt.title("Total Sales by Name (High Sales in Red)")
plt.xlabel("Name")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("day3_total_sales_highlight.png")
plt.show()

# 6️⃣ Export processed data
df.to_csv("day3_processed_data.csv", index=False)
print("\nProcessed data saved as 'day3_processed_data.csv'")

# 7️⃣ Write Insights (for practice, normally in INSIGHTS.md)
print("\nINSIGHTS:")
for name, row in summary.iterrows():
    print(f"{name} had total sales of {row['sum']} across {row['count']} entries, averaging {row['mean']:.2f}.")
    if row['mean'] > 300:
        print("  → This is a high performer!")
    else:
        print("  → This is a normal performer.")
