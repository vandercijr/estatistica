import math

def calcularSturges(n):
	#retorna a variavel k que representa o numero de classes da distribuicao
	#log de n na base 10
	return math.ceil(1 + 3.3 * math.log(n, 10))

def construirArrayIntervalos(valor_minimo_inicial, k, h): #controi a lista com as distribuições de classes
	intervalos = []

	limite_inferior = 0
	limite_superior = 0

	for i in range(0, k):
		limite_inferior = limite_superior
		if (i == 0):
			limite_inferior = valor_minimo_inicial

		limite_superior = limite_inferior + h

		intervalos.append({
			'limite_inferior' : limite_inferior,
			'limite_superior' : limite_superior,
			'frequencia_absoluta' : 0,
			'frequencia_relativa' : 0,
			'frequencia_acumulada' : 0
		})

	return intervalos

def calcularFrequencia(intervalos, lista):
	novo_intervalos = intervalos
	tamanho_lista = len(lista)
	frequencia_acumulada = 0

	for intervalo in novo_intervalos:
		frequencia_absoluta = 0
		for item in lista:
			if (item >= intervalo['limite_inferior'] and item < intervalo['limite_superior']):
				frequencia_absoluta += 1
			else:
				if (intervalo['frequencia_absoluta'] > 0):
					break

		frequencia_acumulada += frequencia_absoluta
		frequencia_relativa = frequencia_absoluta / tamanho_lista * 100

		novo_intervalos[novo_intervalos.index(intervalo)]['frequencia_absoluta'] = frequencia_absoluta
		novo_intervalos[novo_intervalos.index(intervalo)]['frequencia_relativa'] = frequencia_relativa
		novo_intervalos[novo_intervalos.index(intervalo)]['frequencia_acumulada'] = frequencia_acumulada

	return novo_intervalos

def calcularAmplitudeClasse(min, max, k): #apesar de ter sido definida no trabalho criei a funcao para facilitar os calculos
	#ceil arredonda uma fracao para um inteiro
	return math.ceil((max - min) / k)

def calcularTotal(intervalos):
	fabs = 0
	frelat = 0

	for intervalo in intervalos:
		fabs += intervalo['frequencia_absoluta']
		frelat += intervalo['frequencia_relativa']

	return {
		'frequencia_absoluta'	:	fabs,
		'frequencia_relativa'	:	frelat,
		'frequencia_acumulada'	:	'-'
	}

def calcularPontoMedio(max, min):#calcula o ponto medio em uma classe
	return (max + min) / 2

def calcularMedia(intervalos):#calcula a media da distribuicao
	n = 0
	soma_xi_fi = 0

	for intervalo in intervalos:
		soma_xi_fi += calcularPontoMedio( \
					intervalo['limite_superior'], \
					intervalo['limite_inferior'] \
				) * intervalo['frequencia_absoluta'] #SOMATORIO xi * fi

		n += intervalo['frequencia_absoluta']

	return soma_xi_fi / n

def calcularVariancia(intervalos):
	total = calcularTotal(intervalos)
	n = total['frequencia_absoluta']

	soma_a = 0
	soma_b = 0

	for intervalo in intervalos:
		ponto_medio = calcularPontoMedio(
			intervalo['limite_superior'],
			intervalo['limite_inferior']
		)

		soma_a += math.pow(ponto_medio, 2) * intervalo['frequencia_absoluta']

		soma_b += ponto_medio * intervalo['frequencia_absoluta']

	_b = math.pow(soma_b, 2)

	return ((n * soma_a) - _b) / (n * (n - 1))

def calcularPostoMediana(n):
	return (n + 1) / 2

def encontrarPostoMediana(posto_mediana, intervalos):
	posicao = 0
	for intervalo in intervalos:
		if (posto_mediana <= intervalo['frequencia_acumulada']):
			break
		posicao += 1

	return posicao

def calcularMediana(intervalos, _h):
	total = calcularTotal(intervalos)
	n = total['frequencia_absoluta']

	posto_mediana = calcularPostoMediana(n)
	posicao = encontrarPostoMediana(posto_mediana, intervalos)

	return intervalos[posicao]['limite_inferior'] + \
			(posto_mediana - intervalos[posicao-1]['frequencia_acumulada']) * \
			_h / \
			intervalos[posicao-1]['frequencia_absoluta']\

def calcularDesvioPadrao(intervalos):
	return math.sqrt(calcularVariancia(intervalos))

def gerarOutput(lista, intervalos):
	total = calcularTotal(intervalos)
	tamanho_lista = len(lista)
	k = calcularSturges(tamanho_lista)
	h = calcularAmplitudeClasse(lista[0], lista[tamanho_lista-1], k)

	print('Intervalos | FA | FR(%) | FAC')

	for intervalo in intervalos:
		print(intervalo['limite_inferior'], end='')
		print(' |- ', end='')
		print(intervalo['limite_superior'], end='')
		print(' | ', end='')
		print(intervalo['frequencia_absoluta'], end='')
		print(' | ', end='')
		print('{0:.02f}'.format(intervalo['frequencia_relativa']), end='')
		print(' | ', end='')
		print(intervalo['frequencia_acumulada'])

	print('TOTAL    ', end='')
	print(' | ', end='')
	print(total['frequencia_absoluta'], end='')
	print(' | ', end='')
	print(total['frequencia_relativa'], end='')
	print(' | ', end='')
	print(total['frequencia_acumulada'])
	print('\n')

	print('Estatística Descritiva')
	print('\n')

	print(
		'Media: {0:.02f}'.format(calcularMedia(intervalos))
	)

	print(
		'Variancia: {0:.02f}'.format(calcularVariancia(intervalos))
	)

	print(
		'Desvio Padrao: {0:.02f}'.format(calcularDesvioPadrao(intervalos))
	)

	print(
		'Mediana: {0:.02f}'.format(calcularMediana(intervalos, h))
	)

def main():#funcao principal
	arquivo = open('amostra.txt')

	lista = []

	for linha in arquivo:
		lista.append(
			int(
				linha.rstrip('\n')
			)
		)
	
	arquivo.close()

	tamanho_lista = len(lista)

	k = calcularSturges(tamanho_lista) #numero de classes pela regra de sturges

	h = calcularAmplitudeClasse(lista[0], lista[tamanho_lista-1], k)

	intervalos_vazio = construirArrayIntervalos(lista[0], k, h)

	intervalos = calcularFrequencia(intervalos_vazio, lista)

	gerarOutput(lista, intervalos)

main()