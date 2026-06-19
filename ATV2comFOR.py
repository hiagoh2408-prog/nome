VidaJogador = 10
VidaInimigo = 10
PoderRaio = 1
PoderCura = 1
NumeroRodadas = 4
for i in range(4):
    if NumeroRodadas == 4:
        print("digite 1,2,3 para usar a espada, cura ou raio respectivamente, você tem 4 rodadas para eliminar o monstro e apenas 1 cura e 1 raio")
    movimento = int(input("Escolha sua ação: "))
    if movimento == 1:
        print("Usou a espada")
        VidaInimigo -= 3
    elif movimento == 2 and PoderCura == 1:
        print("Usou sua cura")
        VidaJogador += 6
        PoderCura -= 1
    elif movimento == 2 and PoderCura == 0:
        print("Usou sua cura, nada aconteceu...")
    elif movimento == 3 and PoderRaio == 1:
        print("Usou seu raio")
        VidaInimigo -= 6
        PoderRaio -= 1
    elif movimento == 3 and PoderRaio == 0:
        print("Usou seu raio, ele acabou...")
    else:
        print("Você não utilizou nenhuma habilidade")
    if VidaJogador < 1 or NumeroRodadas == 0:
        print("Você perdeu")
        print("O inimigo ainda teve " + str(VidaInimigo) +
              " de vida restante, ainda sobraram " + str(NumeroRodadas - 1) + " rodadas.")
        break
    if VidaInimigo < 1:
        print("Você ganhou")
        print("Você ainda teve " + str(VidaJogador) +
              " de vida restante, ainda sobraram " + str(NumeroRodadas - 1) + " rodadas.")
        break
    NumeroRodadas -= 1
    VidaJogador -= 5
    print("O monstro te atacou, você está com " + str(VidaJogador) + " de vida, e o inimigo está com " +
          str(VidaInimigo) + " de vida, lhe restam " + str(NumeroRodadas) + " rodadas.")
