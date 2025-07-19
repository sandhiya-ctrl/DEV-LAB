import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

wine_data = load_wine()
df = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
df['target'] = wine_data.target

print("First 5 rows:\n", df.head())
print("\nShape of dataset:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nSummary statistics:\n", df.describe())

plt.figure(figsize=(6, 4))
sns.countplot(x='target', data=df, palette='Set2')
plt.title('Wine Classes Distribution')
plt.xlabel('Class Label')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(14, 10))
sns.heatmap(df.corr(), annot=False, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

top_features = ['alcohol', 'malic_acid', 'color_intensity']
for feature in top_features:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='target', y=feature, data=df, palette='pastel')
    plt.title(f"{feature.capitalize()} vs Target Class")
    plt.show()
