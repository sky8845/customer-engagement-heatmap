import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

data = pd.DataFrame({
    "Visit_Frequency": np.random.normal(5, 2, 300),
    "Purchase_Frequency": np.random.normal(3, 1, 300),
    "Avg_Order_Value": np.random.normal(75, 20, 300),
    "Email_Click_Rate": np.random.normal(0.25, 0.08, 300),
    "App_Engagement_Score": np.random.normal(60, 15, 300),
    "Customer_Lifetime_Value": np.random.normal(500, 150, 300)
})

corr_matrix = data.corr()

sns.set_style("whitegrid")
sns.set_context("talk")

# Force exact pixel dimensions for the saved image
DESIRED_PX = 512
# Choose a dpi; figsize (in inches) * dpi = pixels
DPI = 64
figsize = (DESIRED_PX / DPI, DESIRED_PX / DPI)

plt.figure(figsize=figsize, dpi=DPI)
ax = sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    square=True,
    cbar_kws={"shrink": 0.7}
)

plt.title("Customer Engagement Correlation Matrix", fontsize=16)

# Save without `bbox_inches='tight'` (which can change output size)
plt.savefig("chart.png", dpi=DPI, bbox_inches=None, pad_inches=0)
plt.close()
