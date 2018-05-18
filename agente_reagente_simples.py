#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time

__author__ = "Marcos Magno de Carvalho"


class Agente(object):
    """docstring for Agente"""

    def __init__(self):
        self.acao = ''
        self.posicao_livre = []
        self.jogada_humano = []
        obj_JogoVelha = JogoVelha()
        self.ganho = obj_JogoVelha.get_formacao()

    def agente(self):
        """
          O comportamento do agente é dado abstratamente pela função do agente:

            [f: P* -> A]

         onde é a P* é uma sequência de percepções e A é uma ação.


        """
        self.atuador(self.percepcao(self.get_posicao_livre()))

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

    def percepcao(self, posicao_livre):
        """
            Sequência de percepções: 
            história completa de tudo que o agente percebeu.

            Interpretar Entrada baseado em:
                posicao_livre : posicoes livres no tabuleiro
                jogada_humano : jogadas do ser Humano

        """

        for i in range(0, 8):
            jog = [x for x in self.ganho[i] if x in self.jogada_humano]
            if len(jog) > 1:
                jog_acao = [y for y in self.ganho[i]
                            if y not in self.jogada_humano]
                self.jogada_humano.pop(1)
                return jog_acao[0]

        posicao_livre = posicao_livre
        tamanho = len(posicao_livre)
        
        # Escolhe aleatoriamente uma das posicoes livre na primeira jogada
        vertical_jogo = random.choice(posicao_livre)
        return vertical_jogo


class JogoVelha(object):
    """docstring for JogoVelha"""

    def __init__(self):
        self.lista_posicao_livre = []
        self.jogador = ["X", "O"]

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

    def set_posicao_livre(self, lista):
        self.lista_posicao_livre = lista

    def get_posicao_livre(self):
        return self.lista_posicao_livre

    def get_formacao(self):
        return self.ganho


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
    ganho = obj_JogoVelha.get_formacao()

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
        (5, 1),
        (5, 5),
        (5, 9),
        (3, 1),
        (3, 5),
        (3, 9),
        (1, 1),
        (1, 5),
        (1, 9),
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
            print("Deu velha!")
            break

        for i in range(1, 10):
            if tabuleiro[posicao[i][0]][posicao[i][1]] == " ":
                posicao_livre.append(i)
                obj_JogoVelha.set_posicao_livre(posicao_livre)

        if jogador == "X":
            jogada = int(
                input("Escolha uma posicao do Tabuleiro (1-9) "))

            obj_Humano.set_jogada_humano(jogada)  # Pega a jogada do ser Humano

        else:
            """
                O sensor do agente verifica o ambiente 
                (posicao livre e a jogada do Humano)
            """
            obj_Agente.set_sensor(
                obj_JogoVelha.get_posicao_livre(), obj_Humano.get_jogada_humano())

            obj_Agente.agente()  # Ativa o agente
            jogada = obj_Agente.get_acao()  # Atua

        if jogada < 1 or jogada > 9:
            print("Posicao invalida")

        # Verifica a posicao do tabuleiro
        if tabuleiro[posicao[jogada][0]][posicao[jogada][1]] != " ":
            print("Posicao ocupada. Tente outra !")
            continue

        tabuleiro[posicao[jogada][0]][posicao[jogada][1]] = jogador

        for p in ganho:
            for x in p:
                if tabuleiro[posicao[x][0]][posicao[x][1]] != jogador:
                    break
            else:
                print("           O JOGADOR ( %s ) GANHOU: " % (jogador), " ")
                jogando = False
                break

        jogador = "X" if jogador == "O" else "O"  # Alterna jogador

        jogadas += 1


if __name__ == '__main__':
    main()
