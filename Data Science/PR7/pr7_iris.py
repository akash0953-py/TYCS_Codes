import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Read dataset
df = pd.read_csv("C:/Users/user/Documents/TYCS26/Data Science/PR7/data/iris.csv")

# Display first 5 rows
print(df.head())

# 2. Select features for clustering
# We are using only petal length and petal width
X = df[['petal_length', 'petal_width']]

print("\nSelected Features:")
print(X.head())

# 3. Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Elbow Method
wcss = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# 5. Display Elbow Plot
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")
plt.show()

# 6. Apply K-Means with K = 3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

df['Cluster'] = kmeans.fit_predict(X_scaled)

# 7. Display clustered data
print("\nClustered Data:")
print(df.head(10))

# 8. Display cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# 9. Plot clusters
plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=df['Cluster'],
    cmap='viridis'
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker='X',
    s=200,
    label='Centroids'
)

plt.title("K-Means Clustering of Iris Dataset")
plt.xlabel("Petal Length (Scaled)")
plt.ylabel("Petal Width (Scaled)")
plt.legend()
plt.show()