
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
import io

np.random.seed(42)

# -----------------------------
# Synthetic Data
# -----------------------------
segments = ['Budget', 'Regular', 'Premium', 'VIP']
data = []

for segment in segments:
    if segment == 'Budget':
        amounts = np.random.normal(50, 15, 150)
    elif segment == 'Regular':
        amounts = np.random.normal(150, 30, 200)
    elif segment == 'Premium':
        amounts = np.random.normal(300, 50, 120)
    else:  # VIP
        amounts = np.random.normal(500, 100, 80)
    amounts = np.clip(amounts, 0, None)
    data.extend([[segment, amt] for amt in amounts])

df = pd.DataFrame(data, columns=['Customer Segment', 'Purchase Amount'])

# -----------------------------
# Seaborn Style
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -----------------------------
# Create a larger figure for layout
# -----------------------------
fig, ax = plt.subplots(figsize=(8, 8))  # layout space
sns.boxplot(x='Customer Segment', y='Purchase Amount', data=df, palette='Set2', ax=ax)

ax.set_title("Purchase Amount Distribution by Customer Segment", fontsize=16, weight='bold')
ax.set_xlabel("Customer Segment", fontsize=12)
ax.set_ylabel("Purchase Amount ($)", fontsize=12)

plt.tight_layout()  # prevent clipping

# -----------------------------
# Render to PIL image at 512x512 pixels
# -----------------------------
buf = io.BytesIO()
fig.savefig(buf, format='png', dpi=200)  # high dpi to preserve layout
buf.seek(0)
img = Image.open(buf)
img = img.resize((512, 512), Image.LANCZOS)
img.save('chart.png')

plt.close(fig)
print("Chart saved as chart.png (exactly 512x512 pixels, text fully visible)")
