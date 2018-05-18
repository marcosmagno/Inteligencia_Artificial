#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time


class Agente(object):
    """docstring for Agente"""

    def __init__(self):
        self.acao = ''
        self.posicao_livre = []
        self.jogada_humano = []
        self.ganho = [
            [1, 2, 3],  # Linhas
            [4, 5, 6],
            [7, 8, 9],
            [7, 4, 1],  # Colunas
            [8, 5, 2],
            [9, 6, 3],
            [7, 5, 3],  # Diagonais
            [1, 5, 9]
        ]

    def agente(self):
        """
          O comportamento do agente é dado abstratamente pela função do agente:

                [f: P* -> A]

         onde é a P* é uma sequência de percepções e A é uma ação.


        """
        self.atuador(self.percepcao(
            self.get_posicao_livre(), self.get_jogada_humano()))

    def set_sensor(self, posicao_livre, recv_jogada_humano):
        self.posicao_livre = posicao_livre
        self.jogada_humano = recv_jogada_humano

    def get_posicao_livre(self):
        return self.posicao_livre

    def get_jogada_humano(self):
        return self.jogada_humano

    def atuador(self, acao):
        self.acao = acao

    def get_acao(self):
        return self.acao

    def percepcao(self, posicao_livre, jogada_humano):
        """
                Sequência de percepções: história completa de tudo
                que o agente percebeu.

        """


        for i in range(0,7):
        	print self.ganho[i]
        	lista_final = [x for x in jogada_humano if x in self.ganho[i]]

        	#lista_final = [x for x in jogada_humano if x in self.ganho[0]]

        print "LISTA FINAL", lista_final

        if len(jogada_humano) > 1:
            print "marcar a proxima", self.ganho[i]
            print "jogada humaaaaaaaaaa", jogada_humano
            marcar = [y for y in self.ganho[i] if y not in jogada_humano]
            print "marcaaaar essa", marcar[0]
            return marcar[0]
        else:
            posicao_livre = posicao_livre
            print "posicao livre", posicao_livre
            print "jogada humado000000", jogada_humano
            i = random.randrange(3, 12, 3)
            j = random.randrange(2, 11, 3)
            k = random.randrange(1, 10, 3)
            l = random.randrange(7, 10, 1)
            m = random.randrange(4, 8, 1)
            o = random.randrange(1, 4, 1)
            seq = [i, j, k, l, m, o]
            tamanho = len(posicao_livre)
            return posicao_livre[tamanho - 1]

        #vertical_jogo = random.choice(seq)
        # print vertical_jogo

        # if vertical_jogo in posicao_livre:
        #	return vertical_jogo
        # else:
        #	return posicao_livre[tamanho - 1]
        #posicao_livre = percepcao
        # print "Lista", posicao_livre
        #i = len(posicao_livre)
        # print "tamanho", i
        # print "i-1", i - 1
        # print "posicao", posicao_livre[i - 1]

        # return vertical_jogo


class JogoVelha(object):
    """docstring for JogoVelha"""

    def __init__(self):
        self.lista_posicao_livre = []
        self.jogador = ["X", "O"]

    def set_posicao_livre(self, lista):
        self.lista_posicao_livre = lista

    def get_posicao_livre(self):
        return self.lista_posicao_livre


class Humano(object):
    """docstring for Jogado"""

    def __init__(self):
        self.jogada_humano = []

    def set_jogada_humano(self, jogada):
        self.jogada_humano.append(jogada)

    def get_jogada_humano(self):
        return self.jogada_humano


def main():
    obj_JogoVelha = JogoVelha()
    obj_Agente = Agente()
    obj_Humano = Humano()

    # Inicia o primeiro jogador de forma aleatória
    jogador = obj_JogoVelha.jogador[random.randint(0, 1)]

    velha = """               		Posicoes
	   |   |      7 | 8 | 9
	---+---+---  ---+---+---
	   |   |      4 | 5 | 6
	---+---+---  ---+---+---
	   |   |      1 | 2 | 3
	"""

    posicao = [
        None,
        (5, 1),  # 1
        (5, 5),  # 2
        (5, 9),  # 3
        (3, 1),  # 4
        (3, 5),  # 5
        (3, 9),  # 6
        (1, 1),  # 7
        (1, 5),  # 8
        (1, 9),  # 9
    ]

    ganho = [
            [1, 2, 3],  # Linhas
            [4, 5, 6],
            [7, 8, 9],
            [7, 4, 1],  # Colunas
            [8, 5, 2],
            [9, 6, 3],
            [7, 5, 3],  # Diagonais
            [1, 5, 9]
    ]

    tabuleiro = []
    for linha in velha.splitlines():
        tabuleiro.append(list(linha))

    jogando = True
    jogadas = 0
    posicao_livre = []

    while True:

        for t in tabuleiro:
            print("".join(t))
        if not jogando:
            break
        if jogadas == 9:
            print("Deu velha! Ninguem ganhou.")
            break

        for i in range(1, 10):
            if tabuleiro[posicao[i][0]][posicao[i][1]] == " ":
                posicao_livre.append(i)
                obj_JogoVelha.set_posicao_livre(posicao_livre)

        posicao_livre = []
        if jogador == "X":
            jogada = int(
                input("Digite a posicao a jogar (1-9) "))
            obj_Humano.set_jogada_humano(jogada)

        else:
            obj_Agente.set_sensor(
                obj_JogoVelha.get_posicao_livre(), obj_Humano.get_jogada_humano())
            obj_Agente.agente()
            jogada = obj_Agente.get_acao()

        if jogada < 1 or jogada > 9:
            print("Posicao invalida")

        if tabuleiro[posicao[jogada][0]][posicao[jogada][1]] != " ":
            print("Posicao ocupada.")

            continue

        tabuleiro[posicao[jogada][0]][posicao[jogada][1]] = jogador

        for p in ganho:
            for x in p:
                if tabuleiro[posicao[x][0]][posicao[x][1]] != jogador:
                    break
            else:
                print("O jogador %s ganhou (%s): " % (jogador, p))
                jogando = False
                break

        jogador = "X" if jogador == "O" else "O"  # Alterna jogador

        jogadas += 1


if __name__ == '__main__':
    main()
