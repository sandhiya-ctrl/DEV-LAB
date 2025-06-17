import pandas as pd

# Load the dataset
df = pd.read_csv("corporate_work_hours_productivity.csv")
df.columns = df.columns.str.strip()

# Drop missing values
df = df.dropna(subset=['Department', 'Monthly_Hours_Worked'])
df['Monthly_Hours_Worked'] = pd.to_numeric(df['Monthly_Hours_Worked'], errors='coerce')
df = df.dropna(subset=['Monthly_Hours_Worked'])

# Group by department and sum working hours
dept_hours = df.groupby('Department')['Monthly_Hours_Worked'].sum().reset_index()

# Create pivot table (summary)
pivot_table = dept_hours.pivot_table(values='Monthly_Hours_Worked', index='Department')

# Highlight department with highest working hours
max_dept = pivot_table['Monthly_Hours_Worked'].idxmax()
max_hours = pivot_table['Monthly_Hours_Worked'].max()

# Print the pivot summary
print("\n📊 Department-wise Total Monthly Working Hours Summary:\n")
print(pivot_table)

# Print the top department
print(f"\n🏆 Highest Total Working Hours:\n{max_dept} → {max_hours:.2f} hours")
