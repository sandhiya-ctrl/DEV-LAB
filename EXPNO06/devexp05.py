import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.datasets import get_rdataset
dataset = get_rdataset('AirPassengers', package='datasets').data

dataset.rename(columns={'value': 'Passengers'}, inplace=True)

dataset['Month'] = pd.date_range(start='1949-01-01', periods=len(dataset), freq='MS')
dataset.set_index('Month', inplace=True)

dataset = dataset[['Passengers']]

print(dataset.head())

plt.figure(figsize=(10, 5))
plt.plot(dataset, label='Air Passengers', color='purple')
plt.title('Monthly Air Passengers')
plt.xlabel('Date')
plt.ylabel('Number of Passengers')
plt.legend()
plt.grid(True)
plt.show()

dataset['MA_6'] = dataset['Passengers'].rolling(window=6).mean()
dataset['MA_12'] = dataset['Passengers'].rolling(window=12).mean()

plt.figure(figsize=(10, 5))
plt.plot(dataset['Passengers'], label='Original', alpha=0.5)
plt.plot(dataset['MA_6'], label='6-month MA', color='green')
plt.plot(dataset['MA_12'], label='12-month MA', color='red')
plt.title('Moving Averages')
plt.xlabel('Date')
plt.ylabel('Passengers')
plt.legend()
plt.grid(True)
plt.show()

decompose_result = seasonal_decompose(dataset['Passengers'], model='multiplicative')
decompose_result.plot()
plt.tight_layout()
plt.show()

# Heatmap Visualization
dataset['Year'] = dataset.index.year
dataset['Month_Num'] = dataset.index.month

heatmap_data = dataset.pivot_table(values='Passengers', index='Month_Num', columns='Year')

plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt='.0f', cmap='coolwarm')
plt.title('Monthly Passenger Heatmap')
plt.xlabel('Year')
plt.ylabel('Month')
plt.show()
