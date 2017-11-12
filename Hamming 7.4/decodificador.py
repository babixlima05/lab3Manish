import sys, math
import numpy as np

def mod2(x):
	return x%2

arq = open("recebido.txt", "r")
saida = open("decodificado.txt", "w")

txt = arq.read()
txt = txt.rstrip("\n")

vetor = []

for i in txt:
	vetor.append(int(i))

matrixCol = np.matrix(vetor).getT()

H = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]] 

H = np.matrix(H)
M = H*matrixCol

vecFunc = np.vectorize(mod2)
result = vecFunc(M)

result = str(result)

index = 0

for i in range(3):
	index = index + (2**i)*int(result[2+5*i])

index = index - 1

vetor[index] = (vetor[index]+1)%2
for i in vetor[:4]:
	saida.write(str(i))

arq.close()
saida.close()