Dinheiro = float(input("Dinheiro na conta: "))
PodeDirigir = bool(input("Pode dirigir: "))
PossuiAutorizacao = bool(input("Possui autorizacao: "))
PodeParcelar = bool(input("Pode parcelar:  "))

if Dinheiro >= 30000 and (PodeDirigir == True or PossuiAutorizacao == True):
    print("Pode comprar o carro novo e pode dirigir ele")
elif Dinheiro >= 30000 and PodeDirigir == False and PossuiAutorizacao == False:
    print("Pode comprar o carro novo mas nao pode dirigir")
elif Dinheiro <= 30000 and PodeParcelar == True and (PodeDirigir == True or PossuiAutorizacao == True):
    print("Pode comprar o carro parcelado e pode dirigir ele")
elif Dinheiro <= 30000 and PodeParcelar == True and PodeDirigir == False and PossuiAutorizacao == False:
    print("Pode comprar o carro parcelado mas nao pode dirigir ele")
else:
    print("Nao pode comprar um carro novo")
