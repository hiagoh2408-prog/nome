Perguntas = ["Quantas atividades de sequencia já tiveram?","Quantos dias tem 1 ano comum?",  "Quanto é 10 x 5?"]
Respostas = ["3",  "355",  "50"]

Quantidade_de_acertos = 0

Numero_pergunta = 0

for pergunta in Perguntas:
    print(pergunta)
    resposta = input("Resposta pergunta: ")
    if resposta == Respostas[Numero_pergunta]:
        print("Resposta certa")
        Quantidade_de_acertos += 1
    elif resposta == "":
        print("Nao escreveu nada")
    else:
        print("Errou")
    Numero_pergunta += 1
if Quantidade_de_acertos > 1 or Quantidade_de_acertos < 1:
    print("Acertou " + str(Quantidade_de_acertos) + " vezes")
else:
    print("Acertou " + str(Quantidade_de_acertos) + " vez")
