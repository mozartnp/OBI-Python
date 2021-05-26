entrada = input("")
entrada_lista =[]
entrada_lista[:0]=entrada

gabarito = {
  'A' : 2,
  'B' : 2,
  'C' : 2,
  'D' : 3,
  'E' : 3,
  'F' : 3,
  'G' : 4,
  'H' : 4,
  'I' : 4,
  'J' : 5,
  'K' : 5,
  'L' : 5,
  'M' : 6,
  'N' : 6,
  'O' : 6,  
  'P' : 7,
  'Q' : 7,
  'R' : 7,
  'S' : 7,
  'T' : 8,
  'U' : 8,
  'V' : 8,
  'W' : 9,
  'X' : 9,
  'Y' : 9,
  'Z' : 9,
  '-' : '-',
}
if len(entrada_lista) < 16 and len(entrada_lista) > 1:

  listafinal = []
  for item in entrada_lista:
    if item in gabarito:
      listafinal.append(gabarito[item])   
    else:
      break

  for i in listafinal:
    print(i, end='')


"""
Outra possibilidade mais elegante mas tenho que melhorar

gabarito = {
  1 : [],
  2 : ['A','B','C'],
  3 : ['D','E','F'],
  4 : ['G','H','I'], 
  5 : ['J','K','L'],
  6 : ['M','N','O'],
  7 : ['P','Q','R','S'],
  8 : ['T','U','V'],
  9 : ['W','X','Y','Z'],
  0 : [],
  '*' : [],
  '#' : [],
  '-' : ['-'],
}

for item in entrada_lista:
    for k,v in gabarito.items():
        if item == k:
            print(v)
"""