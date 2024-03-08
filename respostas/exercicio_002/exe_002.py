import os
"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""

def verifica_fibonacci(numero):
    num1, num2 = 0, 1
    while num1 <= numero:
        if num1 == numero:
            return True
        else:
            num1, num2 = num2, num1 + num2
    return False 

while True:        
    try:
        numero = int(input('Informe um numero: '))
        pertence_fibonacci = verifica_fibonacci(numero)

        if pertence_fibonacci:
            print(f'O número {numero} pertence a senquência de Fibonnaci')
            break
        else:
            print(f'O número {numero} não pertence à senquência de Fibonnaci.')
            break

    except ValueError:
        print('Por favor, insira apenas números inteiros, Grato!')
        continue



