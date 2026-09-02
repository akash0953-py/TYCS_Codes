import pandas as pd

# Read CSV
df = pd.read_csv("Data Science/employee.csv")

print("\nOriginal Data")
print(df)

# Missing values
print("\nMissing Values")
print(df.isnull().sum())

# fillna
print("\nAfter fillna()")
filled_df = df.fillna("Not Assigned")
print(filled_df)

# dropna
print("\nAfter dropna()")
dropped_df = df.dropna()
print(dropped_df)

# Salary > 40000
print("\nEmployees with Salary > 40000")
print(df[df["Salary"] > 40000])

# Marketing employees
print("\nMarketing Employees")
print(df[df["Department"] == "Marketing"])

# Sort ascending
print("\nEmployee Names Ascending")
print(df.sort_values("Emp_Name"))

# Sort descending
print("\nEmployee Names Descending")
print(df.sort_values("Emp_Name", ascending=False))

# Tech employees
print("\nTech Employees")
print(df[df["Department"] == "Tech"])

# Average salary
print("\nAverage Salary Department-wise")
print(df.groupby("Department")["Salary"].mean())

# HR count
print("\nHR Employee Count")
print(df[df["Department"] == "HR"].shape[0])

# Highest and Lowest salary designation-wise
print("\nDesignation Wise Highest and Lowest Salary")
print(df.groupby("Designation")["Salary"].agg(["max", "min"]))