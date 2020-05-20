import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
Df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00246/3D_spatial_network.txt')
D = D.iloc[:,:3].iloc[:,1:][:500].values
plt.scatter(D[:,0], D[:,1])

wcss = []
for i in range(1, 11):
  kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=500, n_init=10, random_state=0)
  kmeans.fit(D)
  wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=7, init='k-means++', max_iter=500, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(D)
plt.scatter(D[:,0], D[:,1])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
s=500, c='red')
plt.show()

import numpy as np
from sklearn import cluster
from osgeo import gdal, gdal_array
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
gdal.UseExceptions()
gdal.AllRegister()
img=mpimg.imread('5f2491592df6eb86f395147f0852d6aa.jpg')
imgplot = plt.imshow(img)
plt.show()
img_ds = gdal.Open('5f2491592df6eb86f395147f0852d6aa.jpg', gdal.GA_ReadOnly)

band = img_ds.GetRasterBand(2)
img = band.ReadAsArray()
print (img.shape)
X = img.reshape((-1,1))
print (X.shape)
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X)
X_cluster = k_means.labels_
X_cluster = X_cluster.reshape(img.shape)
print (len(X_cluster))

plt.figure(figsize=(10,20))
plt.imshow(X_cluster, cmap="PiYG")
plt.show()