import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# -----------------------------
# Configuration
# -----------------------------
DATA_FILE = Path("SampleSuperstore.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")

# -----------------------------
# Load and inspect dataset
# -----------------------------
if not DATA_FILE.exists():
    raise FileNotFoundError(
        "SampleSuperstore.csv was not found. Place it in the same folder as this script."
    )

df = pd.read_csv(DATA_FILE, encoding="latin1")

print("First five rows:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nDataset information:")
df.info()

print("\nMissing values by column:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nStatistical summary:")
print(df.describe())

# -----------------------------
# Sales by category (total sales)
# -----------------------------
sales_by_category = (
    df.groupby("Category", as_index=False)["Sales"]
      .sum()
      .sort_values("Sales", ascending=False)
)

plt.figure(figsize=(8, 5))
ax = sns.barplot(data=sales_by_category, x="Category", y="Sales", color="steelblue")
ax.set_title("Total Sales by Category")
ax.set_xlabel("Category")
ax.set_ylabel("Total Sales")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_by_category.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# -----------------------------
# Profit by region (total profit)
# -----------------------------
profit_by_region = (
    df.groupby("Region", as_index=False)["Profit"]
      .sum()
      .sort_values("Profit", ascending=False)
)

plt.figure(figsize=(8, 5))
ax = sns.barplot(data=profit_by_region, x="Region", y="Profit", color="steelblue")
ax.set_title("Total Profit by Region")
ax.set_xlabel("Region")
ax.set_ylabel("Total Profit")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "profit_by_region.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# -----------------------------
# Sales vs. profit
# -----------------------------
plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=df,
    x="Sales",
    y="Profit",
    hue="Category",
    alpha=0.55,
    s=35
)
plt.title("Sales vs. Profit by Category")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_vs_profit.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# -----------------------------
# Correlation heatmap
# Exclude identifier/location code columns from correlation analysis.
# -----------------------------
numeric_for_corr = df[["Sales", "Quantity", "Discount", "Profit"]]
correlation = numeric_for_corr.corr()

plt.figure(figsize=(7, 5))
sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    linewidths=0.5
)
plt.title("Correlation Heatmap of Sales Variables")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

print(f"\nAnalysis completed. Charts saved in: {OUTPUT_DIR.resolve()}")
