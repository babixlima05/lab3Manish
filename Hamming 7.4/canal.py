import sys, random

arq = open("codificado.txt", "r")

saida = open("recebido.txt", "w")

p = float(input("Qual a probabilidade de erro do canal? "))


if p > 0.5:
	p = float(input("Entrada invalida, o parametro deve estar entre 0 e 0.5. Digite novamente: "))

X = arq.readline()

X = X.rstrip('\n')

Y = []

for x in X:
	
	mudar = random.randint(0,100)

	if mudar < 100*p:
		if x == "1":
			Y.append("0")
		
		elif x == "0": 
			Y.append("1")
	
	else:
		Y.append(x)

saida.writelines(Y)
saida.close()
arq.close()