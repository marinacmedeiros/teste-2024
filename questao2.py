"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

def fibonacci_sequence(n):
	fibonacci = [0, 1]

	while fibonacci[-1] < n:
		fibonacci.append(fibonacci[-1] + fibonacci[-2])

	return fibonacci

def check_fibonacci(number, sequence):
	if number in sequence:
		return True
	else:
		return False

number = int(input("Digite um número para verificar se ele pertence a sequência de fibonacci: "))

fibonacci_sequence = fibonacci_sequence(number)
is_fibonacci = check_fibonacci(number, fibonacci_sequence)

if is_fibonacci:
	print(f"O número {number} pertence a sequência de Fibonacci.")
else:
	print(f"O número {number} não pertence a sequência de Fibonacci.")
