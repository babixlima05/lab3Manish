import sys, math
import numpy as np

def mod2(x):
	return x%2

arq = open("recebido.txt", "r")
saida = open("decodificado.txt", "w")

qtd = arq.readline()

for i in range(int(qtd)):
	stringEntrada = arq.read()
	stringEntrada = stringEntrada.rstrip("\n")

	vetorEntrada = []

	for i in stringEntrada:
		vetorEntrada.append(int(i))

	matrixCol = np.matrix(vetorEntrada).getT()

	H = [[1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,1,1,0,0,1,1,0,0,1,1,0,0,1,1],[0,0,0,1,1,1,1,0,0,0,0,1,1,1,1],[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]] 

	H = np.matrix(H)
	M = H*matrixCol

	vecFunc = np.vectorize(mod2)
	vectorError = vecFunc(M)

	vectorError = str(vectorError)

	index = 0

	for i in range(4):
		index = index + (2**i)*int(vectorError[2+5*i])

	if index != 0:
		index = index - 1
		vetorEntrada[index] = (vetorEntrada[index]+1)%2
	
	vetorEntrada = np.matrix(vetorEntrada).getT()

	R = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],]

	R = np.matrix(R)
	decodificado = R*vetorEntrada
	decodificado =  vecFunc(decodificado)

	for i in decodificado:
	 	saida.write(str(int(i)))

	 saida.write("\n")

arq.close()
saida.close()