 # clustering dataset
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans



"""


with open('Grupo_de_Pessoas.dat') as file:
	read_data = file.readlines()
	#print(str(read_data).split("::"))
	#print(read_data)
file.close()

idade = []
for i in read_data:
	idade.append(str(i).split(",")[2])

#print(idade)

with open("GP_idade.dat", "w") as gp_file:
	count = 0
	for i in idade:
		count = count + 1
		print(i)
		gp_file.write(str(i)+"\n")



"""

iris = pd.read_csv("GP_idade.dat")
#print(iris.head())

X = iris.iloc[:, 0:1].values



kmeans = KMeans(n_clusters=7, init = 'random')
kmeans.fit(X)
#print(kmeans.cluster_centers_[:, 0])


plt.scatter(X[:, 0], X[:,0], s = 100, c = kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 0], s = 300, c = 'red',label = 'Centroids')
plt.title('Grupo de Pessoas')
plt.xlabel('Total de Pessoas')
plt.ylabel('Idade')
plt.legend()

plt.show()