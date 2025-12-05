import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------
# Generate realistic synthetic data
# -------------------------------
np.random.seed(42)

categories = [
    "Electronics", "Home & Kitchen", "Beauty", "Sports",
    "Clothing", "Toys", "Books", "Grocery"
]

# Satisfaction scores between 1 and 5
scores = np.random.normal(
    loc=[4.2, 4.0, 3.8, 4.1, 3.7, 4.3, 4.5, 4.0],
    scale=0.15,
    size=(8,)
)

data = pd.DataFrame({
    "Category": categories,
    "Avg_Satisfaction": np.clip(scores, 1, 5)
})

# -------------------------------
# Seaborn styling
# -------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -------------------------------
# Create EXACT 512x512 figure
# 8 inches × 64 dpi = 512 px
# -------------------------------
plt.figure(figsize=(8, 8), dpi=64)

sns.barplot(
    data=data,
    x="Category",
    y="Avg_Satisfaction",
    palette="viridis"
)

plt.title("Average Customer Satisfaction by Product Category", fontsize=18)
plt.xlabel("Product Category")
plt.ylabel("Average Satisfaction Score (1–5)")
plt.xticks(rotation=30, ha="right")

# ❗ IMPORTANT: Do NOT use bbox_inches='tight'
plt.savefig("chart.png", dpi=64)
plt.close()
