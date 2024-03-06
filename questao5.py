"""
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""
def inverter_string(string):
	inverted = ''
	for char in string:
		inverted = char + inverted
	return inverted

entrada = input("Digite uma string: ")

print("String original:", entrada)
print("String invertida:", inverter_string(entrada))
