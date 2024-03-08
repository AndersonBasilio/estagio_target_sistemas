import os

"""
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

"""
print('+----------------------+')
print('| Invertendo Palavra   |')
print('+----------------------+')

def inverte_string(string):
    print(string[::-1])

string = str(input('Informe a palavra que deseja inveter: '))

os.system('cls')

print('+----------------------+')
print('| Palavra Invertida    |')
print('+----------------------+')

inverte_string(string)