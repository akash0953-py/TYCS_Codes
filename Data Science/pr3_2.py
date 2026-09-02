import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


print('Original Column')
df = pd.read_csv('Data Science\data\iris-id.csv')
print(df)


print('scaling using min max scaler')
mm = MinMaxScaler()
df[['sepal_length', 'sepal_width', 'petal_length','petal_width']]= mm.fit_transform(
    df[['sepal_length', 'sepal_width', 'petal_length','petal_width']]
)
print(df)


print('scaling using standard scaler')
ss = StandardScaler()
df[['sepal_length', 'sepal_width', 'petal_length','petal_width']] = ss.fit_transform(
    df[['sepal_length', 'sepal_width', 'petal_length','petal_width']]
)
print(df)