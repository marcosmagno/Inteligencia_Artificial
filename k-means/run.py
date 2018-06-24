# clustering dataset
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import collections
import csv

# Set option to print all the values in list
np.set_printoptions(threshold=50000)

# Read file
with open('Grupo de Pessoas.dat') as file:
    read_data = file.readlines()

# Write values in file - I use this option to read with read_csv panda
with open("GP_idade.csv", "w") as GP_idade:
    for i in read_data:
        try:
            GP_idade.write(str(i).split("::")[0] + "," + str(i).split("::")[1] + "," + str(
                i).split("::")[2] + "," + str(i).split("::")[3] + "," + str(i).split("::")[4] + "\n")
        except IOError:
        	raise

try:
    iris = pd.read_csv("GP_idade.csv", low_memory=False, quoting=csv.QUOTE_NONE,
                       nrows=6040, error_bad_lines=False, sep=',', header=None,)
    print(len(iris))

except:
    raise

# Call KMeans
kmeans = KMeans(n_clusters=7, init='k-means++')
kmeans.fit(iris.iloc[:, 2:3].values, iris.iloc[:, 0:1].values)

# Get result
dict_result = {}
dict_result = {i: iris.iloc[:, 0:8].values[np.where(kmeans.labels_ == i)]
               for i in range(kmeans.n_clusters)}

print(dict_result)
print(len(dict_result))

for key, value in dict_result.items():
    result_file = open(str(key) + "_" + str(len(value)) + "_" + str(key), "w")
    result_file.write(str(value))


"""
plt.scatter(iris.iloc[:, 0:1], iris.iloc[:, 0:1], c = kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[
            :, 0], s=300, c='red', label='Centroids')
plt.title('Grupo de Pessoas')
plt.xlabel('Total de Pessoas')
plt.ylabel('Idade')
plt.legend()

plt.show()

"""
