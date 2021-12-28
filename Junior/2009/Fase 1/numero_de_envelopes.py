#tempo gasto 9 minutos 19 segundos

qnt_de_selos = input('')
entrada = input('').split()
menor = int(entrada[0])
if int(qnt_de_selos) < 1 or int(qnt_de_selos) > 1000:
    pass
else:
    for x in entrada:
        if int(x) < menor:
            menor = int(x)

    print(menor)