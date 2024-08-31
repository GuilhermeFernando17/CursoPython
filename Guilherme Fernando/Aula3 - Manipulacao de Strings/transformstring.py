# Trocando Palavra dentro de um texto
texto =  "GUILHERME FERNANDO"
trocaTexto = texto.replace("FERNANDO" , "SANTOS")
print(trocaTexto)

#Trocar o texto totalmente em maiúsculo ou minusculo
texto2 = "SOcieDAde EspOrTIVA PalMeiRas"
textoMaiusculo = texto2.upper()
textoMinusculo = texto2.lower()
print(textoMaiusculo)
print(textoMinusculo)

# Deixar primeira letra em maiusculo
texto3 = "meu primeriro curso de python"
print(texto3.capitalize())

# Deixar primeira letra de cada palavra em maiusculo
print(texto3.title())



#Eliminar espaços inuteis (inicio e fim)
texto4 = "    Senai Mogi das Cruzes   "
print(texto4.strip())