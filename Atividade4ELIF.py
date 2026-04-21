Idade = int(input("Idade: "))
TemExperiencia =  bool(input("Possui experiencia: "))
PossuiAntecendentesCriminais =  bool(input("Possui antecendentes criminais: "))
EnsinoSuperiorCompleto = bool(input("Completou Ensino superior: "))
FoiIndicado = bool(input("Foi indicado: "))

if Idade >= 18 and TemExperiencia == True and PossuiAntecendentesCriminais == False:
    print("Contratado")
elif (EnsinoSuperiorCompleto == True or FoiIndicado == True) and PossuiAntecendentesCriminais == False and Idade >= 18:
    print("Pode ser entrevistado")
else:
    print("Nao pode ser contratado")
