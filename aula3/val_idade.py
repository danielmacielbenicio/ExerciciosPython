idade = (input("Digite a sua idade: "))
tem_carteira = (input("Você tem carteira?"))
doc = bool

if tem_carteira == "s" or tem_carteira == "S":
    doc = True
elif tem_carteira == "n" or tem_carteira == "N":
    doc = False
else:
    print("ERRO: Operação Inválida")

if doc and idade >= 18:
    print("Acesso permitido!")
else:
    print("Acesso negado!")