texto = "Curso de Python"
#-------------------------------------
# pegar uma letra do texto
posicao7 = texto[6]
print(f"posição 7: {posicao7}")
#-------------------------------------
#pegar uma palavra do texto
texto_curso = texto[0:5]
#ou
texto_curso = texto[:5]

text_curso2 = texto[9:15]
#ou
texto_curso2 = texto[9:]

print(texto_curso)
print(texto_curso2)
#-------------------------------------
#Contar o número de caracteres do texto
qtdChar = len(texto)
print(f"na frase temos {qtdChar} caracteres")
#-------------------------------------
# Contar um número expecifico de letras (ex: quantos "o" tem no texto)
qtdLetraO = texto.count("o") 
print(f"Na frase possui {qtdLetraO} letras o")
#-------------------------------------
#Identifica a posição que inicia uma palavra
palavra = "Python"
posicao_palavra = texto.find(palavra)
print(f"A palavra {palavra} começa na posicao {posicao_palavra}")
#-------------------------------------
#Identifica se existe uma palavra no texto
verificaPalavra = "Python" in texto
print(verificaPalavra)
