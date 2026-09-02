import pandas as pd
df=pd.read_csv('Data Science/data.csv')

# replace empty value with NAN
# df.dropna(inplace=True)
# print(df.head(10))

# replace empty value with 0
# df.fillna(inplace=True, value=0)
# print(df.head(10))


# data = df['Class']=='TYCS'
# print(data)
# data = df['Marks']>=59
# print(data)

sorted_names=sorted(df['Name'],reverse=True)
print(sorted_names)