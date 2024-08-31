#1) Crie um programa que leia um nome completo de uma pessoa e mostre
# O nome em letras maiúsculas
# O nome em letras minúsculas
# quantas letras tem no nome todo
#Quantas letras tem no primeiro nome

nome = input("Digite um nome: ")
print(f"Seu nome em letra maiúscula é: {nome.upper()}")
print(f"Seu nome em letra minúscula é: {nome.lower()}")
nome_sem_especos = nome.replace(" ", "")
print(f"A quantidade de caracteres do seu  nome é:{len(nome_sem_especos)}")
nome_split = nome.split()
print(f"Seu primeiro nome é {len(nome_split[0])}")

#2) Crie um programa que leia o nome de uma cidade e diga
#se ela começa ou não com o nome "Santo"

nome_cidade = input("Digite o nome de uma cidade: ")
nome_cidade_split = nome_cidade.split()
print(f"O primeiro nome da cidade é {nome_cidade_split[0]}")

#3) Crie um programa que leia o nome de uma pessoa e diga se 
# ela tem "Silva"  no nome
nome2 = input("Digite um nome: ")
procura_nome = "Silva" in nome2
print(procura_nome)

#4) Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece pela ultima vez
frase = input("Digite uma frase: ")
frase_maiuscula = frase.upper()
frase_contagem = frase_maiuscula.count("A")
print(f"O seu nome tem {frase_contagem} letas 'A'")

#5) Faça um progrma que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o ultimo nome separadamente
nome3 = input("Digite um nome: ")
nome3_split = nome3.split()
print(f"Seu primeiro nome é {nome3_split[0]}e seu ultimo nome é {nome3_split[-1]}")
