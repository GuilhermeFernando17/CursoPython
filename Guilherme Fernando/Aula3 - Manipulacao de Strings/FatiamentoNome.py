nomeCompleto = "Guilherme Fernando Pires dos Santos"
primeiroNome = nomeCompleto[0:9]
ultimoNome = nomeCompleto[29:]

print(primeiroNome)
print(ultimoNome)
#------------------------------------------------------
qtdLetras = len(nomeCompleto)
print(qtdLetras)
qtdLetraA = nomeCompleto.count('o')
print(qtdLetraA)
IniciaUltimoNome = nomeCompleto.find("Santos")
print(IniciaUltimoNome)
ProcuraNome = "Silva" in nomeCompleto or "Santos" in nomeCompleto or "Souza" in nomeCompleto
print(ProcuraNome)
