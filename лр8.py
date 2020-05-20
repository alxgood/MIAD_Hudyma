from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph
from sklearn.cluster import KMeans
df = pd.read_csv('pima-indians-diabetes.csv', sep=",")
data = df[df['class'] == 1]
num_data = data[['mass', 'age']].to_numpy()
plt.scatter(num_data[:, 0], num_data[:, 1])
for x, y in zip(num_data[:, 0], num_data[:, 1]):
    plt.annotate(xy=(x, y), xytext=(-3, 3), textcoords='offset points', ha='right', va='bottom', s="")
plt.show()
linkage_data = linkage(num_data, 'single')
plt.figure(figsize=(7, 7))
dendrogram(linkage_data, distance_sort='descending', show_leaf_counts=True)
plt.show()
cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
cluster.fit_predict(num_data)
plt.scatter(num_data[:, 0], num_data[:, 1], c=cluster.labels_, cmap='rainbow')
plt.show()

data = df[['plas', 'pres']]
data2 = df['class']
data_train, data_test, data2_train, data2_test = train_test_split(data, data2, random_state=1)
data_classifier = KNeighborsClassifier(n_neighbors=5,weights = 'distance', metric='minkowski', p=2, algorithm='brute')
data_classifier.fit(data_train, data2_train)
data_pred = data_classifier.predict(data_test)
plt.scatter(data_test['plas'],data_test['pres'],c=y_pred,cmap='coolwarm',alpha=0.7)
plt.show()

data = df[df['class'] == 1]
num_data = data[['mass', 'age']].to_numpy()
linkage_data = linkage(num_data, 'complete')
dendrogram(linkage_data, distance_sort='descending', show_leaf_counts=True)
plt.show()

data = df[['age', 'mass']].to_numpy()
plt.figure(figsize=(10, 10))
data_clastering = AgglomerativeClustering(linkage="average", n_clusters=5)
data_clastering.fit(data)
plt.scatter(data[:, 0], data[:, 1], c=model.labels_, cmap=plt.cm.nipy_spectral)
plt.show()

data = df[['plas', 'pres']]
kmeans = KMeans(n_clusters=4)
kmeans.fit(data)
data_kmeans = kmeans.predict(data)
plt.scatter(data['plas'], data['pres'], c=data_kmeans, s=50, cmap='viridis')
data_cluster = kmeans.cluster_centers_
plt.scatter(data_cluster[:, 0], data_cluster[:, 1], c='black', s=200, alpha=0.5);
plt.show()