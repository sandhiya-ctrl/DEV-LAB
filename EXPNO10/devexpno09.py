import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
print("Dataset shape:", df.shape)
print("Column info:\n", df.info())
print("\nFirst 5 rows:\n", df.head())
print("\nMissing values:\n", df.isnull().sum())
print("\nSummary statistics:\n", df.describe(include='all'))

df = df.drop(columns=['deck', 'embark_town', 'alive'])
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

plt.figure(figsize=(6, 4))
sns.countplot(x='survived', data=df, palette='Set2')
plt.title("Survival Count (0 = Died, 1 = Survived)")
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x='sex', hue='survived', data=df, palette='Set1')
plt.title("Survival by Gender")
plt.show()

plt.figure(figsize=(6, 4))
sns.countplot(x='pclass', hue='survived', data=df, palette='Set3')
plt.title("Survival by Passenger Class")
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='age', kde=True, hue='survived', palette='coolwarm')
plt.title("Age Distribution by Survival")
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='Blues')
plt.title("Correlation Matrix")
plt.show()
