n_de_dias = int(input(''))
taxa = input('').split()
din_din_do_juninho = 100
variacao = 0
variacaomax = False

for x in range(n_de_dias-3):
  variacao = int(taxa[x]) + int(taxa[x+1]) + int(taxa[x+2]) + int(taxa[x+3])
  if variacaomax == False:
    variacaomax = variacao
  elif variacao > variacaomax:
    variacaomax = variacao
    
print(variacaomax)