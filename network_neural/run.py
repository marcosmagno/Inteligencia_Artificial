# Imports
import random
import numpy as np


"""
Rede Neural:
Baseado no livro: deeplearningbook
Link: http://deeplearningbook.com.br/construindo-uma-rede-neural-com-linguagem-python/
Git: https://github.com/dsacademybr/DeepLearningBook
"""

__author__ = "Marcos Magno de Carvalho"


class Network(object):
    """docstring for Network"""

    def __init__(self, sizes):
        """
                sizes ( list ) 	: numero de neuronio nas respectivas camadas (Ex: [2,3,1])
                bias  (lista de matriz)		:
                weights (int)	Pesos

        """
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

        """
			a' = theta (wa + b) vetorizar a função theta
			Onde:
				a é o vetor de ativações da segunda camada de neurônio.
				a' = multiplicação de a pela matriz de peso w + vetor de bias
		"""

    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a
