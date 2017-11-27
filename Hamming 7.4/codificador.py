import sys, math
import numpy as np

def mod2(x):
	return x%2

arq = open("transmitido.txt", "r")
saida = open("codificado.txt", "w")


stringEntrada = arq.read()
stringEntrada = stringEntrada.rstrip("\n")

vetorEntrada = []

for i in stringEntrada:
	vetorEntrada.append(int(i))

G = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]
G = np.matrix(G)

vetorEntrada = np.matrix(vetorEntrada).getT()

M = G*vetorEntrada

vecFunc = np.vectorize(mod2)
result = vecFunc(M)
print(result)
result = str(result)
stringSaida = ""

for i in range(7):
	stringSaida = stringSaida + result[2 + 5*i]

saida.write(stringSaida)
arq.close()
saida.close()