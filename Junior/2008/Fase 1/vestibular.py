qnt_questoes = int(input(""))
gabarito = input("")
candidato_respostas = input("")
qnt_acertos = 0

if qnt_questoes >= 1 and qnt_questoes <= 80:
    for cont in range(qnt_questoes):
        if gabarito[cont] == candidato_respostas[cont]:
            qnt_acertos += 1
    print(qnt_acertos)
