#tempo gasto 10 minutos

entrada = input('').split()
c = int(entrada[0])
p = int(entrada[1])
f = int(entrada[2])

if c <= 1000 and c >= 1:
  if p <= 1000 and p >= 1:
    if f <= 1000 and f >= 1:
      if (c*f) > p:
        print("N")
      else:
        print("S")