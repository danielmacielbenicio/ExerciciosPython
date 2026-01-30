nome = str(input("Digite o seu nome: "))
nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
nota_3 = int(input("Digite a terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

print(nome, " a sua média foi: ", f"{media:.2f}")  
if(media > 7):
    print("Você foi aprovado!")
elif (media < 7): 
        print("Você foi reprovado!")
else: 
    print("Você está de recuperação")
