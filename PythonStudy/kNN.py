# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 16:30:49 2017

@author: zcao
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def distance(p1,p2):
    """Find the distrance between p1 and p2."""
    return np.sqrt(np.sum(np.power(p2-p1,2)))

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


import scipy.stats as ss 
def majority_vote_short(votes):
    """Returen the most common element in votes."""
    mode, count = ss.mstats.mode(votes)    
    return mode


votes = [1,2,3,4,5,3,1,2,3,1,3,2,2]
winner  = majority_vote(votes)
p1 = np.array([1,1])
p2 = np.array([4,4])

distance(p1,p2)



#compute the distance between point p to every other point
#sort distance and retur k points that are nearest to point p


points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])

p = np.array([2.5,2])




plt.plot(points[:,0],points[:,1],"ro")
plt.plot(p[0],p[1],"bo")
plt.axis([0.5,3.5,0.5,3.5])

def find_nearest_neighbors(p,points,k=5):
    """Find the k nearest neighbors of point p """
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p,points[i])
    ind = np.argsort(distances)
    return ind[:k]

ind = find_nearest_neighbors(p,points,3)
print(points[ind])


def knn_predic(p,points,outcomes,k=5):
    # find k nearest neighbors
    ind = find_nearest_neighbors(p,points,k)
    return majority_vote(outcomes[ind])
    # predict the class of p based on majority vote

outcomes = np.array([0,0,0,0,1,1,1,1,1])



def generate_synth_data(n=50):
    """ Synthetic data """
    points = np.concatenate((ss.norm(0,1).rvs((n,2)),ss.norm(1,1).rvs((n,2))),axis = 0)
    outcomes = np.concatenate((np.repeat(0,n),np.repeat(1,n)))
    return (points,outcomes)





points,outcomes = generate_synth_data(10)
n=10
plt.figure()
plt.plot(points[:n,0],points[:n,1],"ro")
plt.plot(points[n:,0],points[n:,1],"bo")


















