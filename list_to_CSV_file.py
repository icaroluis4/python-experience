import csv
import pandas as pd

nme = ["aparna", "pankaj", "sudhir", "Geeku"] # Dicionarios(dictionary) ou listas 

df = pd.DataFrame( nme , columns=["Names"]) # Transforma em DataFrame

df.to_csv('names.csv')

print(df[0 : 1])

