#tempo gasto 8 minutos 04 segundos

memoria_max = input('')
entrada = input('').split()

if int(memoria_max) > 500000 or int(entrada[0]) > 1000 or int(entrada[2]) > 1000:
    pass
else:
    operador = entrada[1]
    if operador == str('*'):
        resul = int(entrada[0]) * int(entrada[2])
    elif operador == str('+'):
        resul = int(entrada[0]) + int(entrada[2])

    if resul > int(memoria_max):
        print ('OVERFLOW')
    else:
        print('OK')