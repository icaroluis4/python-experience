import pandas as pd
# importa um arquivo csv
cash = 100.0
min = 100.0
max = 100.0

close = 0
prev = 0

putcall = False
longshort = False

acertos = 0
erros = 0

lucroperda = 0

df = pd.read_csv('itau_500.csv')

#prev = df['Close'][0] - df['previsão'][1]
#print(prev)


for x in range(len(df)):
    
    putcall = False
    longshort = False

    if( x+1 == len(df)):
        break
    else:
        close = df['Close'][x]
        prev = df['previsão'][x+1]
        if(prev > close):
            putcall = True
        else:
            putcall = False

        lucroperda =  abs(df['Close'][x] - df['Close'][x+1])

        if(df['Close'][x] < df['Close'][x+1]):
            longshort = True
        else:
            longshort = False
        
        if(longshort != putcall):
            cash = cash - lucroperda 
            erros = erros + 1
            if(cash < min):
                min = cash
        else:
            cash = cash + lucroperda 
            acertos = acertos + 1
            if(cash > max):
                max = cash
        


print(cash)
print("Total:" , len(df) , " Acertos: ", acertos , " Erros: " , erros , " MAX: " , max , " MIN: ", min )
print("Valorização Buy and Hold" , df['Close'][0] , " --- " , df['Close'].iloc[-1])            #FAZER Lógica do calculo do Lucro/perda baseado encima do close , close+1 