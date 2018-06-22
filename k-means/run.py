# clustering dataset
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import collections
import csv


GP_idade = open("GP_idade.csv", "w")
with open('Grupo de Pessoas.dat') as file:
    read_data = file.readlines()


for i in read_data:
    GP_idade.write(str(i).split("::")[0] + "," + str(i).split("::")[2] + "\n")

GP_idade.close()


try:
    iris = pd.read_csv("GP_idade.csv", low_memory=False, quoting=csv.QUOTE_NONE,
                       nrows=6040, error_bad_lines=False, sep=',', header=None,)
    print(len(iris))

except:
    raise


kmeans = KMeans(n_clusters=7, init='k-means++')
kmeans.fit(iris.iloc[:, 1:2].values, iris.iloc[:, 0:1].values)


dict_result = {}
dict_result = {i: iris.iloc[:, 0:2].values[np.where(kmeans.labels_ == i)]
               for i in range(kmeans.n_clusters)}

print(dict_result)
# print(kmeans.cluster_centers_)

for key, value in dict_result.items():

    result_file = open(str(key) + "_" + str(len(value)) + "_" + str(key), "w")
    result_file.write(str(value))


"""
# print(kmeans.cluster_centers_)
plt.scatter(X[:, 0], X[:, 0], c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[
            :, 0], s=300, c='red', label='Centroids')
plt.title('Grupo de Pessoas')
plt.xlabel('Total de Pessoas')
plt.ylabel('Idade')
plt.legend()

plt.show()
"""
