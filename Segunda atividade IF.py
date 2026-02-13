vidainimigo = 8
quantidadeflechas = 8

if quantidadeflechas == vidainimigo :
  print("Você ganhou! Mas não sobrou nenhuma flecha")
if quantidadeflechas > vidainimigo :
  print("Você ganhou! E ainda sobraram " + str(quantidadeflechas - vidainimigo) + " flechas")
if quantidadeflechas < vidainimigo :
  print("Você perdeu! Faltaram " + str(vidainimigo - quantidadeflechas) + " flechas")
  
