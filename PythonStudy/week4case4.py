# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:34:26 2017

@author: zcao
"""

import pandas as pd
 
x = pd.Series([6,3,8,6], index=["q","w","e","r"])  ## series

age = {"tim":20,"jim":30}  ## dictionary

x = pd.Series(age)


data = {'name':['tim','jin'],'age':[20,31],'zip':['112','231']}

y = pd.DataFrame(data,columns = ["name","age","zip"])

#sorted(x.index)
x.reindex(sorted(x.index))

x1 = pd.Series([7,3,5,2], index=["e","q","r","t"])

x + x1



import numpy as np

whisky = pd.read_csv("whiskies.txt")

whisky["region"] = pd.read_csv("regions.txt")

whisky.head()

flavor = whisky.iloc[:,2:14]

corr_flavor = pd.DataFrame.corr(flavor)

print(corr_flavor)


import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
plt.pcolor(corr_flavor)
plt.colorbar()
plt.savefig("corr_flavor.pdf")


corr_whisky = pd.DataFrame.corr(flavor.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.savefig("corr_whisky.pdf")


from sklearn.cluster.bicluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters=6,random_state=0)

model.fit(corr_whisky)

model.rows_

np.sum(model.rows_,axis = 1)


whisky['Group'] = pd.Series(model.row_labels_, index = whisky.index)

whisky = whisky.ix[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)

correlation = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())

correlation = np.array(correlation)

plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlation)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlations.pdf")








