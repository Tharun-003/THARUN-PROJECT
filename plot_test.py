import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read your CSV file
df = pd.read_csv("data/covid_data.csv")

# Show first few rows (to check data loaded correctly)
print(df.head())
print(df.columns)


# Basic plot
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x=df.columns[0], y=df.columns[1])  # first column vs second column
plt.title("Basic Plot from My CSV")
plt.xticks(rotation=45)
plt.show()
