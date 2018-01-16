import math

def calcularSturges(n):
	#retorna a variavel k que representa o numero de classes da distribuicao
	#log de n na base 10
	return math.ceil(1 + 3.3 * math.log(n, 10))

def main():
	print(calcularSturges(50) + " oi ")

main()