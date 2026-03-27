nota1 = float(input("digite sua primeira nota: "))
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota nota: "))
Notatotal = (nota1 + nota2 + nota3) / 3
if Notatotal == 10 :
    print("Nota perfeita")
elif Notatotal > 5 :
    print("Nota boa")
else :
    print("reprovado")
