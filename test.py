import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('house')

mm = MinMaxScaler()
x = mm.fit_transform(df[['age','income']])

km = KMeans(n_clusters=3,random_state=0)
df['clusters'] = km.fit_predict(x)

plt.scatter(x[:,0],x[:,1],c=df['clusters'])
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],marker='*',s=150)
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()

sse=[]
for k in range(1,10):
    km = KMeans(n_clusters=k,random_state=0)
    km.fit(x)
    sse.append(km.inertia_)

plt.plot(range(1,10),sse,marker="o")
plt.xlabel("K")
plt.ylabel("Sse")
plt.show()