import pandas as pd
#deleta linha ou coluna

impares = [1 , 3 , 5 , 7 , 9 , 11] # Precisa possuir o mesmo numero de indexações
pares = [2 , 4 , 6 , 8 , 10 , 12]
nivers = [19 , 26 , 10 , 29 , 9 , 25]

dict = {'OsImpares':impares , 'OsPares': pares , 'Nivers': nivers}

#df = pd.DataFrame(row = [impares , pares , nivers] , columns=['OsImpares' , 'OsPares' , 'Nivers'])

df = pd.DataFrame(dict)

df.drop(0 , inplace=True)

print(df)