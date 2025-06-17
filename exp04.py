import pandas as pd


df = pd.read_csv('temperature.csv')


df = df[df['AvgTemperature'] != -99]


df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']], errors='coerce')


df = df.dropna(subset=['Date'])



df['Month'] = df['Date'].dt.month_name()

grouped = df.groupby(['City', 'Month'])['AvgTemperature'].sum().reset_index()

pivot_table = grouped.pivot(index='City', columns='Month', values='AvgTemperature').fillna(0)

pivot_table['Total'] = pivot_table.sum(axis=1)

print("Month-wise Temperature Summary:")
print(pivot_table)

max_city = pivot_table['Total'].idxmax()
max_temp = pivot_table['Total'].max()

print(f"\nCity with highest total temperature: {max_city} ({max_temp:.2f}°F)")



