"""
N = Numero de competidores
P = numero minimo de pontos para ser convidado
X = pontuação de um competidor em cada uma das fases
Y = pontuação de um competidor em cada uma das fases

Restrições
1 ≤ N ≤ 1000
1 ≤ P ≤ 1000
0 ≤ X ≤ 400
0 ≤ Y ≤ 400

Entrada 1
3 100
50 50
100 0
49 50
"""
qntaluno = 0
entrada = input("").split()
n = int(entrada[0])
if n >= 1 and n <= 1000:

  p = int(entrada[1])
  if p >= 1 and p <= 1000:

    for cnt in range(n):
      entrada = input("").split()
      x = int(entrada[0])
      if x >= 0 and x <= 400:  
        y = int(entrada[1])
        if y >= 0 and y <= 400:
          ponto = x + y
          if ponto >= p:
            qntaluno += 1

print(qntaluno)
