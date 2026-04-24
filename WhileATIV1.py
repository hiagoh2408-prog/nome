Numero = 9  
NumeroAdvinhado = int(input("Advinhe um número entre 1 a 10:  "))
Advinhando = False
while Advinhando == False:
    if NumeroAdvinhado == Numero:
        print("Acertou")
        Advinhando == True
    if NumeroAdvinhado > Numero:
        print("Número maior que o secreto")    
    if NumeroAdvinhado < Numero:
        print("Número menor que o secreto")
    NumeroAdvinhado = int(input("Advinhe um número entre 1 a 10:  "))

