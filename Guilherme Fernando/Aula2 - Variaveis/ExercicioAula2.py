# DESAFIO 01
# Crie um programa que leia e mostra a soma entre eles.

numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))
soma = numero1 + numero2
print(f"A soma dos valores digitados é: {soma}")


# DESAFIO 02
# Faça um programa que leia um número inteiro e mostra na tela
# e seu sucessor e seu antecessor.
numero3 = int(input("Digite um valor: "))
antecessor = numero3 -1
sucessor = numero3 + 1
print(f"O sucessor do numero {numero3} é: {sucessor}, e o antecessor é {antecessor}")


# DESAFIO 03
# Crie um algoritmo que leia um número e mostre o seu dobro,
# triplo e o seu quadrado.

import math
numero4 = int(input("Digite um número: "))
dobro = numero4 * 2
triplo = numero4 *3
quadrado = numero4 **2
raiz = math.sqrt(numero4)
print(f"O dobro do número escolhido é: {dobro}, o triplo é: {triplo}, o seu número elevado ao quadrado é: {quadrado} e a raiz é {raiz:.2f}")


# DESAFIO 04
# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostra a sua média.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 +nota2)/2
print(f"A média do Aluno é : {media}")


# DESAFIO 05
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos Dólares
# ela pode comprar.
# Considere o dólar = R$ 5,00

dinheiro = float(input("Digite quanto dinheiro você tem: "))
dollar = dinheiro/5
print(f"Você pode comprar {dollar} dollares")