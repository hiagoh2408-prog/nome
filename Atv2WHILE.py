import random
NumeroMaximo = int(input("Numero máximo para advinhar: "))
QuantidadeChances = int(input("Quantidade de chances: "))
Numero = random.randint(1, NumeroMaximo)
NumeroAdvinhado = int(input("Advinhe um número entre 1 até " + str(NumeroMaximo) + ": "))
Advinhando = False
while Advinhando == False and QuantidadeChances > 0:
    if NumeroAdvinhado == Numero:
        print("Acertou")
        Advinhando = True
    elif NumeroAdvinhado > Numero:
        print("Número maior que o secreto")   
        QuantidadeChances -= 1
    elif NumeroAdvinhado < Numero:
        print("Número menor que o secreto")
        QuantidadeChances -= 1
    if Advinhando == False:
        NumeroAdvinhado = int(input("Advinhe um número entre 1 até " + str(NumeroMaximo) + ": "))
if QuantidadeChances < 1:
    print("Acabaram as chances")
