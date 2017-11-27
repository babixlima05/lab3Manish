import sys, random

arq = open("codificado.txt", "r")

saida = open("recebido.txt", "w")

prob = float(input("Qual a probabilidade de erro do canal? "))


if prob > 0.5:
	prob = float(input("Entrada invalida, o parametro deve estar entre 0 e 0.5. Digite novamente: "))

qtd = arq.readline()
saida.write(qtd)
for i in range(int(qtd)):
	vetorEntrada = arq.readline()
	vetorEntrada = vetorEntrada.rstrip('\n')

	vetorSaida = ""

	for x in vetorEntrada:
		
		mudar = random.randint(0,100)

		if mudar < 100*prob:
			if x == "1":
				vetorSaida = vetorSaida + "0"
			
			elif x == "0": 
				vetorSaida = vetorSaida + "1"
		
		else:
			vetorSaida = vetorSaida + x

	saida.write(str(vetorSaida) + "\n")
saida.close()
arq.close()