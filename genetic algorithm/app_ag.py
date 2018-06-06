#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import datetime
import time
import argparse


class GeneticAlgorithm(object):
    """Essa classe implementa um algoritmo genetico que tem a função montar
        uma determinada palavra ou frase passada por parâmetro.

        Diagrama do Algoritmo:
            1 - População Inicial - É criada de forma aleatória
            2 - Chama a função Fitnes
            4 - Seleciona um novo gene (Mutação)
            5 - Gera uma nova população
            6 - Verifica se chegou no objetivo final
                Caso sim, finaliza o programa
                caso não:
            7 repete o passo 1

    """

    def __init__(self, arg):
        self.arg = arg
        self.geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
        self.target = self.arg.texto
        self.startTime = datetime.datetime.now()

    def get_fitness(self, guess):
        """ 
            Esté metodo é responsável por implementar o FITNESS
                Soma 1 caso a palavra esperada seja igual a atual.
        """
        print("Função Fitnes : Cálculo de aptidão")
        time.sleep(3)
        return sum(1 for expected, actual in zip(self.target, guess)
                   if expected == actual)

    def display(self, guess):
        """ 
            Mostra na tela
        """
        timeDiff = datetime.datetime.now() - self.startTime
        fitness = self.get_fitness(guess)

        print("{0}\t\t{1}\t\t\t{2}".format(guess,fitness, str(timeDiff)))

    def generate_parent(self, length):
        """
            Gerando novos pais
        """
        genes = []
        while len(genes) < length:
            sampleSize = min(length - len(genes), len(self.geneSet))
            genes.extend(random.sample(self.geneSet, sampleSize))

        return ''.join(genes)

    def mutate(self, parent):
        """
            Mutação
        """

        index = random.randrange(0, len(parent))
        childGenes = list(parent)
        newGene, alternate = random.sample(self.geneSet, 2)

        childGenes[index] = alternate \
            if newGene == childGenes[index] \
            else newGene

        #print "Mutacao:", ''.join(childGenes)
        print(str("Mutação:     ") + str(''.join(childGenes)))
        time.sleep(3)
        time.sleep(0.5)

        return ''.join(childGenes)


def main():
    parser = argparse.ArgumentParser(
        description='Parse pra o AG')

    parser.add_argument('--texto', type=str, required=False,
                        default='MarcosMagno', help='Uma frase para o AG')

    geneticAlgorithm = GeneticAlgorithm(parser.parse_args())
    random.seed()

    target = parser.parse_args().texto
    print("Gerando Gene Paterno : Popução Inicial")
    bestParent = geneticAlgorithm.generate_parent(len(target))
    time.sleep(3)
    print(bestParent)
    bestFitness = geneticAlgorithm.get_fitness(bestParent)    
    print("\n\nMutação    valor de adequação         Tempo")
    geneticAlgorithm.display(bestParent)

    while True:
        child = geneticAlgorithm.mutate(bestParent)
        childFitness = geneticAlgorithm.get_fitness(child)
        if bestFitness >= childFitness:
            continue
        geneticAlgorithm.display(child)
        if childFitness >= len(bestParent):
            break
        bestFitness = childFitness
        bestParent = child


if __name__ == '__main__':
    main()
