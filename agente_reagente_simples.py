
def maquina_jogando():
	print "pensando....."
	return 1


def main():
	velha="""               Posicoes
	   |   |      7 | 8 | 9
	---+---+---  ---+---+---
	   |   |      4 | 5 | 6
	---+---+---  ---+---+---
	   |   |      1 | 2 | 3
	"""

	posicao = [
	       None,  
	      (5, 1), # 1
	      (5, 5), # 2
	      (5, 9), # 3
	      (3, 1), # 4
	      (3, 5), # 5
	      (3, 9), # 6
	      (1, 1), # 7
	      (1, 5), # 8
	      (1, 9), # 9
	    ]


	ganho = [
	          [ 1, 2, 3], # Linhas
	          [ 4, 5, 6],
	          [ 7, 8, 9],
	          [ 7, 4, 1], # Colunas
	          [ 8, 5, 2],
	          [ 9, 6, 3],
	          [ 7, 5, 3], # Diagonais
	          [ 1, 5, 9]
	        ]


	tabuleiro = []
	for linha in velha.splitlines():
	    tabuleiro.append(list(linha))



	jogador = "X" 
	jogando = True
	jogadas = 0 


	while True:
	    for t in tabuleiro:
	    	print("".join(t))
	    if not jogando: 
	        break
	    if jogadas == 9: 
	        print("Deu velha! Ninguem ganhou.")
	        break

	    if jogador == "X":
	    	jogada = int(input("Digite a posicao a jogar 1-9 (jogador %s):" % jogador))

	    elif jogador == "0":
	    	print "Maquina jogando...."
	    	maquina_jogando()	    	

	    if jogada<1 or jogada>9:
	        print("Posicao invalida")
	        continue
	    
	    if tabuleiro[posicao[jogada][0]][posicao[jogada][1]] != " ":
	        print("Posicao ocupada.");
	        continue        

	    tabuleiro[posicao[jogada][0]][posicao[jogada][1]] = jogador

	   
	    for i in range(1,10):
	    	if tabuleiro[posicao[i][0]][posicao[i][1]] == " ":
	        	print("Posicao livre.")
	        	print i




	    for p in ganho:
	        for x in p:
	            if tabuleiro[posicao[x][0]][posicao[x][1]] != jogador:
	                break
	        else:
	            print("O jogador %s ganhou (%s): "%(jogador, p))
	            jogando = False
	            break
	    
	    jogador = "X" if jogador == "O" else "O" # Alterna jogador

	    

	    jogadas +=1


if __name__ == '__main__':
		main()	