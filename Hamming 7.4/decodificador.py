import sys, math
import numpy as np

def mod2(x):
	return x%2

arq = open("recebido.txt", "r")
saida = open("decodificado.txt", "w")

stringEntrada = arq.read()
stringEntrada = stringEntrada.rstrip("\n")

vetorEntrada = []

for i in stringEntrada:
	vetorEntrada.append(int(i))

matrixCol = np.matrix(vetorEntrada).getT()

H = [[1, 1, 1, 0, 1, 0, 0], [1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1]] 

H = np.matrix(H)
M = H*matrixCol

vecFunc = np.vectorize(mod2)
vectorError = vecFunc(M)
vectorError = str(vectorError)
stringError = ""

for i in range(3):
	stringError = stringError + vectorError[2 + 5*i]

cases = {"000":0, "001": 5, "010":6, "011": 4, "100":7, "101":2, "110":3, "111":1}
index = cases.get(stringError, 'default')

if index != 0:
	index = index - 1
	vetorEntrada[index] = (vetorEntrada[index]+1)%2

decodificado = vetorEntrada[:4]

for i in decodificado:
	saida.write(str(int(i)))

arq.close()
saida.close()