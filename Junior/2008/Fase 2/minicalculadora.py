def mdc(num1, num2):
    if (num1 < num2):
        num1, num2 = inversor(num1, num2)
    fator = euclides(num1, num2)
    return(fator)

def inversor(num1, num2):
    z = num1
    num1 = num2
    num2 = z
    return(num1, num2)

def euclides(num1, num2):
    z = 0
    while (num2 != 0):
        z = num2 
        num2 = (num1 % num2)
        num1 = z
    return(num1)

analise = input('').split()
n, d, q = int(analise[0]), int(analise[1]), int(analise[2])

if n >= 1 and n <= 1000:
  if d >= 1 and d <= 268435456:
    if q >= 2 and q <= 268435456:
      fator = mdc(d, q)
      d /= fator
      q /= fator

if q > n or d > n:
  print('IMPOSSIVEL')
else:
  print(int(d), int(q))