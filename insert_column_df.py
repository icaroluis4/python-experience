import pandas as pd


impares = [1 , 3 , 5 , 7 , 9 ] # Precisa possuir o mesmo numero de indexações
pares = [2 , 4 , 6 , 8 , 10 , 12]
nivers = [19 , 26 , 10 , 29 , 9 , 25]

df = pd.DataFrame( pares ,columns = ['OsPares']) # Transforma lista(vetor) em DataFrame/Coluna

print(df)

impares.append(11)

df['Impares'] = impares
df.insert(1 , "Aniversarios" , nivers , allow_duplicates = False) # Insere na coluna 1 a lista nivers sem permitir duplicações


print(df)