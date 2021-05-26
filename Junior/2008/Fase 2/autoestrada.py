comprimento = int(input(''))
tipos_de_bloco = input('')
qnt_paineis = 0

if comprimento >= 1 or comprimento <= (10**6):
  for analise in tipos_de_bloco:
    if analise == "P":
      qnt_paineis += 2
    elif analise == "C":
      qnt_paineis += 2
    elif analise == "A":
      qnt_paineis += 1
    elif analise == "D":
      pass
    else:
      pass
  print(qnt_paineis)
else:
  pass