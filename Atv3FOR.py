Palavra = (input("Escolha uma palavra: "))
Nome = "Hiago"
for letra in Palavra:
    if letra == Nome[0] or letra =="h":
        print(letra + " , é uma letra do nome")
    elif letra == Nome[1] or letra == "I":
        print(letra + " , é uma letra do nome")
    elif letra == Nome[2] or letra == "A":
        print(letra + " , é uma letra do nome")
    elif letra == Nome[3] or letra == "G":
        print(letra + " , é uma letra do nome")
    elif letra == Nome[4] or letra == "O":
        print(letra + " , é uma letra do nome")
    else:
        print(letra + " , não é uma letra do nome")
