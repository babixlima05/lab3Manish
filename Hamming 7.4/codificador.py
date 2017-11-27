import sys, math
import numpy as np

def mod2(x):
	return x%2

arq = open("transmitido.txt", "r")
saida = open("codificado.txt", "w")

qtd = arq.readline()
saida.write(qtd)
for i in range(int(qtd)):
	stringEntrada = arq.readline()
	stringEntrada = stringEntrada.rstrip("\n")

	vetorEntrada = []

	for l in stringEntrada:
		vetorEntrada.append(int(l))

	G = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1]]
	G = np.matrix(G)

	vetorEntrada = np.matrix(vetorEntrada).getT()

	M = G*vetorEntrada

	vecFunc = np.vectorize(mod2)
	result = vecFunc(M)
	result = str(result)
	stringSaida = ""
	
	for j in range(7):
		stringSaida = stringSaida + result[2 + 5*j]

	saida.write(stringSaida + "\n")
arq.close()
saida.close()