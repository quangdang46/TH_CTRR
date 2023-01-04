def formalConvert(S):
  word = S.split()
  if word[0] == "For":
    qualifier='For all'
    D = word[3]
    P = ' '.join(word[5:])
  elif word[0] == "Exist":
    qualifier='Exist'
    D = word[3]
    P = ' '.join(word[5:])
  elif word[0] == "There":
    qualifier='Exist'
    D = word[5]
    P = ' '.join(word[7:])
  F = qualifier + ' x in ' + D + ', ' + P+'(x)'
  return D,P,F





S = "For all fishes, they need water to survive."
D,P,F = formalConvert(S)
print("D is",D)
print("P is",P)
print("Formal form:",F)
