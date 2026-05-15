Nomes = [ "Alexandre", "Arthur", "Hiago", "Pedro" ]
print("Procure seu nome na lista: Arthur, Pedro, Alexandre, Hiago")
NumeroEscolhido = int(input("Escolha um número: "))
if NumeroEscolhido > 3:
    print("Numero maior que todos na lista")
elif NumeroEscolhido == 0:
    print("Nome: Alexandre")
elif NumeroEscolhido == 1:
    print("Nome: Arthur")
elif NumeroEscolhido == 2:
    print("Nome: Hiago")
elif NumeroEscolhido == 3:
    print("Nome: Pedro")
else:
    print("Numero menor que os disponiveis na lista")
