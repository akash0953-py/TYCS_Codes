# K - Mean Clustering

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

df = pd.read_csv("Data Science/PR7/data/income.csv")
mm = MinMaxScaler()
# print(df.head)

df['Age'] = mm.fit_transform(df[['Age']])
df['Income($)'] = mm.fit_transform(df[['Income($)']])
# print(df.head)

km = KMeans(n_clusters=3)
X = df[['Age','Income($)']]
Predict_y = km.fit_predict(X)

df['Cluster'] = Predict_y
print(df)

centroids = km.cluster_centers_
print(centroids)

df1 = df[df['Cluster'] == 0]
df2 = df[df['Cluster'] == 1]
df3 = df[df['Cluster'] == 2]

plt.scatter(df1['Age'],df1['Income($)'],color = 'red')
plt.scatter(df2['Age'],df2['Income($)'],color = 'blue')
plt.scatter(df3['Age'],df3['Income($)'],color = 'green')
plt.scatter(centroids[:,0],centroids[:,1],color = 'black',marker='*')
plt.legend(df['Income($)'])
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("K Mean Clustering")
plt.show()

sse = []
rng = range(1,10)
for k in rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['Age','Income($)']])
    sse.append(km.inertia_)

plt.xlabel('Age')
plt.ylabel('Income')
plt.title("Elbow Method")
plt.plot(rng,sse)    
plt.show()