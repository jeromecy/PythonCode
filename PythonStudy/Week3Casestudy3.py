# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 22:28:04 2017

@author: zcao
"""

import pandas as pd
import numpy as np
import random
#data = # Enter your code here!
data = pd.read_csv("https://s3.amazonaws.com/demo-datasets/wine.csv")

numeric_data = data.drop("color",1)
numeric_data = (numeric_data - numeric_data.mean()) / np.std(numeric_data)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit(numeric_data).transform(numeric_data)


import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_pdf import PdfPages
observation_colormap = ListedColormap(['red', 'blue'])
x = principal_components[:,0] # Enter your code here!
y = principal_components[:,1]# Enter your code here!

plt.title("Principal Components of Wine")
plt.scatter(x, y, alpha = 0.2,
    c = data['high_quality'], cmap = observation_colormap, edgecolors = 'none')
plt.xlim(-8, 8); plt.ylim(-8, 8)
plt.xlabel("Principal Component 1"); plt.ylabel("Principal Component 2")
plt.show()


def accuracy(predictions, outcomes):
    # Enter your code here!
    return np.mean(predictions == outcomes)

x = np.array([1,2,3])
y = np.array([1,2,4])
print(accuracy(x,y))


print(accuracy(0,data["high_quality"]))



from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(numeric_data, data['high_quality'])
# Enter your code here!

library_predictions = knn.predict(numeric_data)
print(accuracy (library_predictions,data["high_quality"]))



n_rows = data.shape[0]


random.seed(123)

selection = random.sample(range(n_rows), 10)


predictors = np.array(numeric_data)
training_indices = [i for i in range(len(predictors)) if i not in selection]
outcomes = np.array(data["high_quality"])

my_predictions = np.array([knn_predict(predictors[i], predictors[training_indices,:], outcomes, k=5)  for i in selection])
percentage =accuracy(my_predictions,data.high_quality[selection]) 

print(percentage)

def knn_predict(p,points,outcomes,k=5):
    # find k nearest neighbors
    ind = find_nearest_neighbors(p,points,k)
    return majority_vote(outcomes[ind])

def find_nearest_neighbors(p,points,k=5):
    """Find the k nearest neighbors of point p """
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p,points[i])
    ind = np.argsort(distances)
    return ind[:k]


def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] +=1
        else:
            vote_counts[vote] = 1
    
    winners=[]
    max_counts = max(vote_counts.values())

    for vote, count in vote_counts.items():
        if count == max_counts:
            winners.append(vote)
    
    return random.choice(winners)

def distance(p1,p2):
    """Find the distrance between p1 and p2."""
    return np.sqrt(np.sum(np.power(p2-p1,2)))
