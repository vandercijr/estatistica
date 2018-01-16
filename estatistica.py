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

def main():
	print(calcularSturges(50))
	print('\n');
	a = construirArrayIntervalos(33, calcularSturges(50), 10)

	print(a[0]['limite_inferior'])

main()