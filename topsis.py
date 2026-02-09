import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# STEP 1: Dataset (Conversational AI benchmarks)
# -------------------------------

data = {
    "Model": ["Claude Opus", "Gemini 2.5", "GPT-4.1", "LLaMA 3.3", "GPT-4o Turbo"],
    "Elo Score": [1496, 1486, 1287, 1000, 1100],   # Higher is better
    "Quality Index": [0.88, 0.83, 0.99, 0.74, 0.88],  # Higher is better
    "Latency (s)": [1.13, 0.51, 0.48, 0.59, 0.60],  # Lower is better
    "Context Score": [5, 4, 4, 3, 4],  # Higher is better
    "Cost ($)": [15, 2.8, 10, 3.5, 15]  # Lower is better
}

df = pd.DataFrame(data)

print("\nOriginal Decision Matrix:\n")
print(df)

# -------------------------------
# STEP 2: Prepare matrix for TOPSIS
# -------------------------------

matrix = df.iloc[:, 1:].values

# Weights (you can justify these in report)
weights = np.array([0.25, 0.25, 0.15, 0.20, 0.15])

# Impacts: 1 = benefit, -1 = cost
impacts = np.array([1, 1, -1, 1, -1])

# -------------------------------
# STEP 3: Normalize the matrix
# -------------------------------

norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

# -------------------------------
# STEP 4: Weighted normalized matrix
# -------------------------------

weighted_matrix = norm_matrix * weights

# -------------------------------
# STEP 5: Ideal best & worst solutions
# -------------------------------

ideal_best = np.where(
    impacts == 1,
    weighted_matrix.max(axis=0),
    weighted_matrix.min(axis=0)
)

ideal_worst = np.where(
    impacts == 1,
    weighted_matrix.min(axis=0),
    weighted_matrix.max(axis=0)
)

# -------------------------------
# STEP 6: Distance from ideal best & worst
# -------------------------------

dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

# -------------------------------
# STEP 7: TOPSIS score
# -------------------------------

topsis_score = dist_worst / (dist_best + dist_worst)

df["TOPSIS Score"] = topsis_score
df["Rank"] = df["TOPSIS Score"].rank(ascending=False)

# Sort by rank
df = df.sort_values("Rank")

print("\nFinal Ranking using TOPSIS:\n")
print(df)

# -------------------------------
# STEP 8: Bar Graph Visualization
# -------------------------------

plt.figure(figsize=(10, 6))
bars = plt.bar(df["Model"], df["TOPSIS Score"])

# Add score labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.title("TOPSIS Ranking of Conversational AI Models")
plt.xlabel("Model")
plt.ylabel("TOPSIS Score")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
