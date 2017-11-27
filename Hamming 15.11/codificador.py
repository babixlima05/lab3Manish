import sys, math
import numpy as np

def mod2(x):
	return x%2

arq = open("transmitido.txt", "r")
saida = open("codificado.txt", "w")

qtd = arq.readline()
saida.write(qtd)

for i in range(int(qtd)):
	stringEntrada = arq.read()
	stringEntrada = stringEntrada.rstrip("\n")

	vetorEntrada = []

	for i in stringEntrada:
		vetorEntrada.append(int(i))

	vetorEntrada = np.matrix(vetorEntrada).getT()

	G = [[1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
	[1, 0, 1, 1, 0, 1, 1, 0, 0, 1 ,1],
	[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
	[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
	[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

	G = np.matrix(G)
	M = G*vetorEntrada

	vecFunc = np.vectorize(mod2)
	result = vecFunc(M)
	result = str(result)
	
	resultFinal = ""
	for i in range(15):
		resultFinal = resultFinal + result[2 + 5*i]

	saida.write(resultFinal + "\n")

arq.close()
saida.close()