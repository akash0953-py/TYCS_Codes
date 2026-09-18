import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv('Data Science/data/wine.csv', header=None, usecols=(0,1,2), skiprows=1)
df.columns = ['Class', 'Alcohol_level', 'Malic_Acid']
print(df)

print('scaling using min max scaler')
mm = MinMaxScaler()
df[['Class', 'Alcohol_level', 'Malic_Acid']] = mm.fit_transform(
    df[['Class', 'Alcohol_level', 'Malic_Acid']]
)
print(df)

print('scaling using standard scaler')
ss = StandardScaler()
df[['Class', 'Alcohol_level', 'Malic_Acid']] = ss.fit_transform(
    df[['Class', 'Alcohol_level', 'Malic_Acid']]
)
print(df)
