# estou confuso nesta lição. Irei analisar mais os booleans

idade = int(input("Digite a sua idade: "))
tem_carteira = bool

# AND: ambas as condições precisam ser verdadeiras
print(idade >= 18 and tem_carteira)  # True

# OR: uma das condições precisa ser verdadeira
print(idade >= 18 or tem_carteira)   # True

# NOT: inverte o valor
print(not tem_carteira)              # False

