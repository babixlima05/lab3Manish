import sys, math
import numpy as np

def mod2(x):
	return x%2

arq = open("transmitido.txt", "r")
saida = open("codificado.txt", "w")

txt = arq.read()
txt = txt.rstrip("\n")

vetor = []

for i in txt:
	vetor.append(int(i))

vetor = np.matrix(vetor).getT()

G = [[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

G = np.matrix(G)
M = G*vetor

vecFunc = np.vectorize(mod2)
result = vecFunc(M)

result = str(result)
print(result[17])
resultFinal = ""
for i in range(7):
	resultFinal = resultFinal + result[2 + 5*i]

saida.write(resultFinal)
arq.close()
saida.close()