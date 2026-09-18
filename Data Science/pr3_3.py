# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# df=pd.read_csv('Data Science\data\iris-id.csv')
# print("ID column with label encodeing")
# le=LabelEncoder()
# df['ID']=le.fit_transform(df['species'])
# print(df)

# #Using one hot encoding for species column 

# dummy = pd.get_dummies(df,columns=['species'],drop_first=False,dummy_na=False)
# print(dummy[['species_setosa','species_versicolor','species_virginica']])


import pandas as pd
from sklearn.preprocessing import MinMaxScaler , StandardScaler

df = pd.read_csv("data")

mm = MinMaxScaler()
df[["a",'b']] = mm.fit_transform(df[['a','b']])