import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('../data/appliance_usage.csv', index_col=0)

# Total energy per appliance
data['Total'] = data.sum(axis=1)

# Suggest energy-saving tips
tips = []
for appliance, total in data['Total'].items():
    if total > 1000:
        tips.append(f"Consider reducing usage of {appliance} to save energy.")

# Print tips
print("Energy-Saving Suggestions:")
for tip in tips:
    print("-", tip)

# Visualization
plt.figure(figsize=(10,6))
sns.heatmap(data.iloc[:,:24], annot=True, fmt="d", cmap="YlGnBu")
plt.title("Hourly Energy Consumption per Appliance (Watts)")
plt.xlabel("Hour")
plt.ylabel("Appliance")
plt.savefig('../data/energy_heatmap.png')
plt.show()
