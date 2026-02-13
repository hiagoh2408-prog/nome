custofrutas = 15
custoderoupas = 50
dinheirototal = 100
if dinheirototal < custofrutas :  
  print("Não vou levar as frutas pois não tenho dinheiro suficiente, preciso de mais " + str(custofrutas - dinheirototal) + " reais")
else :
  print("Vou levar as frutas, ainda vai sobrar " + str(dinheirototal - custofrutas) + " reais")
if dinheirototal < custoderoupas :
  print("Não posso levar as roupas, preciso de mais " + str(custoderoupas - dinheirototal) + " reais")
else :
  print("vou levar as roupas, pois ainda vai sobrar " + str(dinheirototal - custoderoupas) + " reais")
