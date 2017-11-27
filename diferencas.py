transmitido = open("transmitido.txt", "r")
decodificado = open("decodificado.txt", "r")
saida = open("diferencas.txt", "w")

qtd = transmitido.readline()
erros = 0
bitsAvaliados = 0

for i in range(int(qtd)):
	vectorTransm = transmitido.readline().rstrip("\n")
	vectorDecod = decodificado.readline().rstrip("\n")

	bitsAvaliados = bitsAvaliados + len(vectorDecod)

	for j in range(len(vectorDecod)):
		if vectorTransm[j] != vectorDecod[j]:
			erros = erros + 1

print("porcentagem de erro eh: " + str(porcentagemErro))
