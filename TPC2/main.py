import sys
from sys import stdin
import re

#Sequencias de digitos, ou seja dois ou mais numeros seguidos

def somadoronoff():

    line = input("Input: ")

    delimitadores = re.split("(?i)off", line)

    #print(delimitadores)

    total =[]
    i = 0
    resultadoasaida = False

    if "=" in line : resultadoasaida= True


    for element in delimitadores:
        if i == 0:
            # se o primeiro for off vai aparecer '' caso contrario a primeira string conta
            total.append(element) # primeiro caso porque o off vai criar a primeira string
            i += 1
            continue

        if re.findall("(?i)on", element):
            resultado = re.split("(?i)ON", element)
            if len(resultado) > 1:
                resultado.pop(0)
            total.extend(resultado)
            # ?: -> nao caputar o que esta a frente e o (?i) e para torna-lo case insensitive
            # aqui ate poderiamos usar o i: que ia dar ao mesmo, mas só funciona em python

    #print("Resultado", resultado)
    #print(f'Total : {total}')

    if resultadoasaida == True:
        soma = 0
        numeros = []

        for element1 in total:
            answer = re.findall("[0-9][0-9]+", element1)
            numeros.extend(answer)

        print(f'Lista de numeros "aceites" para a soma: {numeros}')

        if len(numeros) > 0:
            for element2 in numeros:
                soma += int(element2)

        print(f'Soma de todas as sequencias dos numeros: {soma}')



if __name__ == '__main__':
    somadoronoff()



