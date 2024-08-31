#1) Crie um programa para efetuar a leitura de um núemro inteiro 
# e apresentar o resultado do quadrado deste número.
numero1 = int(input("Digite um número: "))
quadrado = numero1 **2
print(f"o quadrado do número digitado é: {quadrado}")


 #Escreve um programa que leia dois caracteres e umpra na tela
carc1 = input("Digite um caractere: ")
carc2 = input("Digite um caractere: ")
print(f"você digitou {carc1} e {carc2}")

  
# Faça um programa que leia um número inteiro e mostra na tela
# e seu sucessor e seu antecessor.
numero3 = int(input("Digite um valor: "))
antecessor = numero3 -1
sucessor = numero3 + 1
print(f"O sucessor do numero {numero3} é: {sucessor}, e o antecessor é {antecessor}")

#Crie um programa para entrar a base c a altura de um retangulo
#e imprima a area e o perimetro
base = float(input("Digite a base o retangulo: "))
altura= float(input("Digite a altura do retangulo: "))
area = base * altura
perimetro = base* 2 + altura* 2
print(f"A area do retangulo é {area} e o perimetro é: {perimetro}")


# Crie um programa que dados o valor, taxa e tempo, efetuar 
# o cálculo do valor de uma prestação em atraso, utilizando a formula
# prestacao = valor +(valor * (taxa/100)*tempo#)

valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa de atraso: "))
tempo = int(input("Digite o temp de atraso em dias:"))
prestacao = valor +(valor *(taxa/100) * tempo)
print(f"A prestação é {prestacao}")