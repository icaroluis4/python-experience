import pandas as pd

# Transforma em vetor em DataFrame

def sum_vect(v):
  num = 0
  
  for j in range(len(v)):
    num = num + v[j]
  
  return num

nme = sum_vect([1 , 3 ,5 , 12]) # Dicionarios(dictionary) ou listas 

df = pd.DataFrame( nme , columns=["Nums"]) # Transforma em DataFrame

print(df)