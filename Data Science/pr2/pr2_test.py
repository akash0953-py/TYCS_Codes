import pandas as pd

df = pd.read_csv("data.csv")

# Check missing values
df.isnull().sum()

# Fill missing values
df = df.fillna('nan')

# Drop rows where Designation is missing
df = df.dropna(subset=["Designation"])

# Salary greater than 4000
df[df['Salary'] > 4000]

# Employees with Marketing designation
df[df['Designation'] == "Marketing"]

# Sort employee names
sorted(df['Emp_Name'])

# Sort departments in reverse order
sorted(df['Department'], reverse=True)

# Employees in Tech department
df[df['Department'] == 'Tech']

# Average salary by department
df.groupby('Department')['Salary'].mean()

# Count HR employees
df[df['Department'] == 'HR']['Emp_Name'].count()

# Maximum salary by designation
df.groupby('Designation')['Salary'].max()

# Minimum salary by designation
df.groupby('Designation')['Salary'].min()