# -*- coding: utf-8 -*-
"""Untitled47.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1laLFqIvFUYdXl9_OqeV0KHqk0YTELqdL
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import random

centroid = [(-5,-5), (5,5)]
clust_std = [1,1]
X,y = make_blobs(n_samples=100, cluster_std=clust_std, centers=centroid, n_features=2, random_state=2)

plt.scatter(X[:, 0], X[:, 1])
plt.show()

import random
import numpy as np

class KMeans:
    def __init__(self,n_clusters=2,max_iter=100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None

    def fit_predict(self,X):

        random_index = random.sample(range(0,X.shape[0]),self.n_clusters) #select the random points for centroid
        self.centroids = X[random_index]

        for i in range(self.max_iter):
            # assign clusters
            cluster_group = self.assign_clusters(X)
            old_centroids = self.centroids
            # move centroids
            self.centroids = self.move_centroids(X,cluster_group)
            # check finish
            if (old_centroids == self.centroids).all():
                break

        return cluster_group

    def assign_clusters(self,X):
        cluster_group = []
        distances = []

        for row in X:
            for centroid in self.centroids:
                distances.append(np.sqrt(np.dot(row-centroid,row-centroid))) # check the distance between the data with all the centorid
            min_distance = min(distances) # select min distance to make the clus
            index_pos = distances.index(min_distance) # selct the cluster
            cluster_group.append(index_pos)
            distances.clear()

        return np.array(cluster_group)

    def move_centroids(self,X,cluster_group):
        new_centroids = []

        cluster_type = np.unique(cluster_group)

        for type in cluster_type:
            new_centroids.append(X[cluster_group == type].mean(axis=0)) # move the centroids to the cluster by mean values of the cluster

        return np.array(new_centroids)

km = KMeans(n_clusters = 2, max_iter=100)
ymean = km.fit_predict(X)

plt.scatter(X[ymean == 0, 0], X[ymean == 0, 1], color = 'red')
plt.scatter(X[ymean == 1, 0], X[ymean == 1, 1], color = 'blue')
plt.show()
