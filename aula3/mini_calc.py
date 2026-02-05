print("-===== Mini Calculadora =====-")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multilicação")
print("4 - Divisão")
print("5 - Módulo (Resto da divisão)")
print("6 - Potência")

operacao = input(" > Escolha uma operação: [1]Soma [2]Subtração [3]Multiplicação [4]Divisão [5]Módulo [6]Potência ")

numero_1 = float(input(">> Digite o primeiro valor: "))
numero_2 = float(input(">> Digite o segundo valor: "))
if operacao == "1":
    print(numero_1 + numero_2)
elif operacao == "2":
    print(numero_1 - numero_2)
elif operacao == "3":
    print(numero_1 * numero_2)
elif operacao == "4":
    while numero_1 and numero_2 != 0:
        print(">> O seu resultado é igual à: ", numero_1 / numero_2)
        break
    else:
        print(">> Erro: Divisão por zero")
elif operacao == "5":
    print(numero_1 % numero_2) 
elif operacao == "6":
    print(numero_1 ** numero_2) 