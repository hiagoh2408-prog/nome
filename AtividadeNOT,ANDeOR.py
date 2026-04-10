idade = int(input("Digite sua idade: "))
TemIngresso = False
TemAutorização = False 
PermissãoVIP = True

if (idade >= 18 and (TemIngresso == True or PermissãoVIP == True) ) or (idade < 18 and idade > 12 and TemAutorização == True and (TemIngresso == True or PermissãoVIP == True)):
    print("Permitido entrar")
else:
    print("Não permitido entrar")
