#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


__author__ = "Marcos Magno de Carvalho"

# Report in: https://www.overleaf.com/16314443rzyxtdmvyksf#/62500778/

class Agente(object):
    """
        This class is responsible for defining the proprieties of the agente
        Attributes:
            acao          (int)   : A position value on the board.
            posicao_livre (list)  : An integer list of the free position in the board.
            jogada_humano (list)  : An list of humano moves.
            obj_JogaVelha (object): An object of the JogoVelha
            ganho         (list)  : A list of positions to win.
    """

    def __init__(self):
        """
            This method is the Agente class constructor.
        """
        self.acao = ''
        self.posicao_livre = []
        self.jogada_humano = []
        obj_JogoVelha = JogoVelha()
        self.ganho = obj_JogoVelha.get_formacao()

    def agente(self):
        """
            The behavior of the agent is given abstractly by the function of the agent:
                [f: P* -> A]
            where P * is a sequence of perceptions and A is an action.
        """

        self.atuador(self.percepcao()) # For each action, send a sequence of perceptions

    def set_sensor(self, posicao_livre, recv_jogada_humano):
        """
            This method is responsible for setting each action.
        """
        self.posicao_livre = posicao_livre # Free position on the board
        self.jogada_humano = recv_jogada_humano # Each move of the Humano

    def get_posicao_livre(self):
        """
            return:
                posicao_livre (list): All free positions on the board.
        """
        return self.posicao_livre

    def get_jogada_humano(self):
        """
            return:
                jogada_humano (list): All moves of the Humano.
        """
        return self.jogada_humano

    def atuador(self, acao):
        self.acao = acao # Setting agent action.

    def get_acao(self):
        """
            return:
                acao (int): A position value on the board.
        """
        return self.acao

    def percepcao(self):
        """
            this method implements the perceptual procedures, characterized by:
                Complete story of everything the agent perceives through the sensor.
                Interpret input based on attributes:
            Attributes:
                posicao_livre (list): An integer list of the free position in the board.
                jogada_humano (list): All moves of the Humano.o
                jogAgente     (list): An integer list of agent moves
                jogHumano     (list): An integer list of humano moves
                jogAcao       (int) : An integer representing an humano action
                jogoAleatorio (int) : An integer representing a random action of the agent
        """

        jogAgent = []

        for i in range(0, 8):
            jogHumano = [x for x in self.ganho[i]
                         if x in self.jogada_humano]  # VerificaJogadaHumano

            if len(jogHumano) > 1:
                # VerificaPosicaoRestante
                jogAcao = [y for y in self.ganho[i]
                           if y not in self.jogada_humano]
                self.jogada_humano.pop(1)
                return jogAcao[0]

        jogAgent = [h for h in self.posicao_livre if h in self.ganho[i]]
        if len(jogAgent) > 1:
            return jogAgent[0]

  
        jogoAleatorio = random.choice(self.posicao_livre)
        return jogoAleatorio


class JogoVelha(object):
    """
        This class implements the Jogo da Velha
            Attributes:
                lista_posicao_livre (list) : An integer list of the free position in the board.
                jogador:            (list) : A list of players
                ganho               (list) : A list of gain positions
    """

    def __init__(self):
        """
            This method is the JogoVelha class constructor.
        """        
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
    """
        This class implements the properties of the humano.
            Attributes:
                jogada_humano (list) : An list of humano moves.
    """

    def __init__(self):
        """
            This method is the Humano class constructor.
        """         
        self.jogada_humano = []

    def set_jogada_humano(self, jogada):
        self.jogada_humano.append(jogada)

    def get_jogada_humano(self):
        return self.jogada_humano


def main():
    """
        This methdo start the game.
            Attributes:
                obj_JogoVelha (object) : An object of the JogoVelha.
                obj_Agente    (object) : An object of the Agente.
                obj_Humano    (object) : an object of the Humano.
                jogador       (string) : An players.
                velha         (string) : A representation of the Jogo da Velha.
                posicao       (list)   : An integer list of the position.
                tabuleiro     (list)   : A representation of the board.
                jogadas       (int)    : A integer value of the moves
                jogando       (boolean): Status of the game.
    """
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
        posicao_livre = []


        for i in range(1, 10):

            if tabuleiro[posicao[i][0]][posicao[i][1]] == " ":
                posicao_livre.append(i)
                obj_JogoVelha.set_posicao_livre(posicao_livre)

        if jogador == "X":
            jogada = int(
                input("Escolha uma posicao do Tabuleiro (1-9) "))

            if jogada < 1 or jogada > 9:
                print("Posicao invalida")
                return


            obj_Humano.set_jogada_humano(jogada)  # Take the humano move.

        else:
            """
               The agent sensor checks the environment
                (posicao livre e a jogada do Humano)
            """
            obj_Agente.set_sensor(
                obj_JogoVelha.get_posicao_livre(), obj_Humano.get_jogada_humano())

            obj_Agente.agente()  # Ativa o agente
            jogada = obj_Agente.get_acao()  # Atua


        # Check the position of the board
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

        jogador = "X" if jogador == "O" else "O"  # Toggles player

        jogadas += 1 # Increment plays


if __name__ == '__main__':
    main()